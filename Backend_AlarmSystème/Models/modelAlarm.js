const mongoose = require('mongoose');  

const alarmSchema =  mongoose.Schema({
    zone1:String,
    zone2: String,
    zone3: String,
    zone4: String,
    alarmOn:String,
    reset:String,
    dateHeure:String,
    
});

module.exports = mongoose.model('alarm', alarmSchema);

