class Opcion {
    constructor(empresa,fechaInicio,fechaTermino,tipo,strike,tiempoMaduracion,numSimulaciones,r){
        this.empresa=empresa;
        this.fechaInicio=fechaInicio;
        this.fechaTermino=fechaTermino;
        this.tipo=tipo;
        this.strike=strike;
        this.tiempoMaduracion=tiempoMaduracion;
        this.numSimulaciones=numSimulaciones;
        this.r=r;
    }
    
    calcular(){
        var spawn = require('child_process').spawn;
        var process = spawn('py',['./calcular.py',
            this.empresa,
            this.fechaInicio,
            this.fechaTermino,
            this.tiempoMaduracion,
            this.numSimulaciones,
            this.r,
            this.strike,
            this.tipo
        ]);
        process.stdout.on('data',function(data){
            console.log(data.toString());
        })
    }
}