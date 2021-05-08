const express =require('express')
const mongoose=require('mongoose')
const cors=require("cors")
const app=express();
const port=3001;
mongoose.connect("mongodb+srv://D1togphkosSm1fSC:D1togphkosSm1fSC@cluster0.cncks.mongodb.net/MessageData?retryWrites=true&w=majority", {
    useNewUrlParser: true,
    useUnifiedTopology: true
}).then(()=> console.log("MongoDb connected"))
.catch(err=>console.log(err))

app.use(cors())
const UserSchema=new mongoose.Schema({
    name:{
        type:String,
        required:true
    },
    age:{
        type:Number,
        required:true
    }},
    {collection : 'Test'}
)
const DataSchema= new mongoose.Schema({
   DataRequest:{
       type:String
   },
    data_Tomsk_ambulance:{
        data:[String],
        raiting:[Number],
        result:Number
    },
    data_google_okb_tomsk:{
        data:[String],
        raiting:[Number],
        result:Number
    },
    data_okpb_Tomsk:{
        data:[String],
        raiting:[Number],
        result:Number
    },
    data_OGAYZ_Hospital_2:{
        data:[String],
        raiting:[Number],
        result:Number
    },
    data_klinikal_Hospital_3:{
        data:[String],
        raiting:[Number],
        result:Number
    }},
    {collection : 'MessageColls'}
)
const Data=mongoose.model('MessageColl',DataSchema)



const User=mongoose.model('Test', UserSchema)


User.find({}, function(err, data){
    console.log(">>>> " + data );
});


app.get('/', (req,res)=>{
     Data.find()
         .then(data=>res.send(data))
         .catch(err=>res.send(err))
 })


app.listen(port,()=>console.log(`server is up port:${port} `))