const express = require('express');
const cors = require('cors');  
const app = express();
app.use(cors());

const mongoose = require('mongoose');
const connection = mongoose.connection;

var bodyParser = require('body-parser'); 
const Alarm = require('./Models/modelAlarm');
app.use(bodyParser.json());                            
app.use(bodyParser.urlencoded({ extended: true })); 

mongoose.connect('mongodb://localhost:27017/AlarmBd',{ useUnifiedTopology: true, useNewUrlParser: true });

//mongoose.connect('mongodb://mngassa:mngassa@10.30.40.121:27017/mngassa',{​​​​​​​ useUnifiedTopology: true, useNewUrlParser: true }​​​​​​​  );

/*const PORT = 3019;
app.listen(PORT,()=>{                                  
    console.log("j'écoute le port 3019!!");
});*/
const PORT = 3535;
app.listen(PORT,()=>{                                  
    console.log("j'écoute le port 3535!!");
});                                                     

connection.once('open',()=>{
    console.log("connected to MongoDb");
});

 app.post('/alarm',(req, res)=>{                  
    console.log('req.body', req.body);             
    const alarmAdd = new Alarm(req.body);        
    alarmAdd.save((err, alarmAdd)=>{                 
        if(err){
            return res.status(500).json(err);           
        }
        res.status(201).json(alarmAdd);                
    });
}); 

app.get('/alarmInfo',(req,res)=>{
    Alarm.find()
    .exec()
    .then(alarm => res.status(200).json(alarm));
});

 
 