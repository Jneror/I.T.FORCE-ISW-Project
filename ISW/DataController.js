class DataController {
    constructor(empresa,fechaInicio,fechaTermino){
        this.empresa=empresa;
        this.fechaInicio=fechaInicio;
        this.fechaTermino=fechaTermino;
        console.log('Clase Construida')
    };

    getDataFromGateway(){
        var spawn = require('child_process').spawn;
        var process = spawn('py',['./YahooData.py',
            this.empresa,
            this.fechaInicio,
            this.fechaTermino
        ]);
        process.stdout.on('data',function(data){
            console.log(data.toString());
            return data.toString();
        })
    }
}