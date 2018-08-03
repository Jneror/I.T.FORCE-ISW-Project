class Opcion {
    constructor(tipo,strike,tiempoMaduracion,numSimulaciones,r,data){
        this.tipo=tipo;
        this.strike=strike;
        this.tiempoMaduracion=tiempoMaduracion;
        this.numSimulaciones=numSimulaciones;
        this.r=r;
        this.data=data;
        console.log('Opcion construida')
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
        console.log('calculando')
        process.stdout.on('data',function(data){
            console.log(data.toString());
        })
    }
}