const url = require('url');
const path = require('path');

const {app,BrowserWindow} = require('electron');

let win;

function createWindow() {
    win = new BrowserWindow({whith: 800, height: 600})
    win.webContents.openDevTools();
    win.loadURL(url.format({
        pathname: path.join(__dirname,'index.html'),
        protocol: 'file',
        slashes: true
    }));
};
app.on('ready', createWindow);