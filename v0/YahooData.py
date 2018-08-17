# -*- coding: utf-8 -*-

# To make print working for Python2/3
from __future__ import print_function

# Use six to import urllib so it is working for Python2/3
from six.moves import urllib
# If you don't want to use six, please comment out the line above
# and use the line below instead (for Python3 only).
#import urllib.request, urllib.parse, urllib.error

import time

# Build the cookie handler
cookier = urllib.request.HTTPCookieProcessor()
opener = urllib.request.build_opener(cookier)
urllib.request.install_opener(opener)

# Cookie and corresponding crumb
_cookie = None
_crumb = None

# Headers to fake a user agent
_headers={
    'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'
}

def _get_cookie_crumb():
    # Perform a Yahoo financial lookup on SP500
    req = urllib.request.Request('https://finance.yahoo.com/quote/^GSPC', headers=_headers)
    f = urllib.request.urlopen(req)
    alines = f.read().decode('utf-8')

    global _crumb
    cs = alines.find('CrumbStore')
    cr = alines.find('crumb', cs + 10)
    cl = alines.find(':', cr + 5)
    q1 = alines.find('"', cl + 1)
    q2 = alines.find('"', q1 + 1)
    crumb = alines[q1 + 1:q2]
    _crumb = crumb

    # Extract the cookie from cookiejar
    global cookier, _cookie
    for c in cookier.cookiejar:
        if c.domain != '.yahoo.com':
            continue
        if c.name != 'B':
            continue
        _cookie = c.value

    # Print the cookie and crumb
    #print('Cookie:', _cookie)
    #print('Crumb:', _crumb)

def load_yahoo_quote(ticker, begindate, enddate, info = 'quote'):
	'''
	This function load the corresponding history/divident/split from Yahoo.
	'''
	# Check to make sure that the cookie and crumb has been loaded
	global _cookie, _crumb
	if _cookie == None or _crumb == None:
		_get_cookie_crumb()

	# Prepare the parameters and the URL
	tb = time.mktime((int(begindate[0:4]), int(begindate[4:6]), int(begindate[6:8]), 4, 0, 0, 0, 0, 0))
	te = time.mktime((int(enddate[0:4]), int(enddate[4:6]), int(enddate[6:8]), 18, 0, 0, 0, 0, 0))

	param = dict()
	param['period1'] = int(tb)
	param['period2'] = int(te)
	param['interval'] = '1d'
	if info == 'quote':
		param['events'] = 'history'
	elif info == 'dividend':
		param['events'] = 'div'
	elif info == 'split':
		param['events'] = 'split'
	param['crumb'] = _crumb
	params = urllib.parse.urlencode(param)
	url = 'https://query1.finance.yahoo.com/v7/finance/download/{}?{}'.format(ticker, params)
	req = urllib.request.Request(url, headers=_headers)

	# Perform the query
	# There is no need to enter the cookie here, as it is automatically handled by opener
	f = urllib.request.urlopen(req)
	alines = f.read().decode('utf-8')
	return alines.split('\n')

def load_quote(ticker, date1, date2):
	print('===', ticker, '===')
	data = load_yahoo_quote(ticker, date1, date2)
	data = [i.split(',') for i in data][1:-1]
	data = []
	for i in range(len(data)):
		data[i] = [data[i][0],] + list(map(lambda x: float(x), data[i][1:]))
	return data
	#[string Date, float Open,float High,float Low,float Close,float Adj Close,float Volume]
	#print(load_yahoo_quote(ticker, date1, date2, 'dividend'))
	#print(load_yahoo_quote(ticker, date1, date2, 'split'))
    

def test():
	# Download quote for stocks
	#load_quote('QCOM','20170501', '20170517')
	load_quote('C','20170501', '20170517')

	# Download quote for index
	#load_quote('^DJI')

if __name__ == '__main__':
	test()