import express from 'express';
import path from 'path';
import cookieParser from 'cookie-parser';
import logger from 'morgan';
import mongoose, { mongo } from 'mongoose';
import routes from './routes';


const PASSWORD = "ngwbddwdh250";
const DB_NAME = "covid2019"
const uri = `mongodb+srv://tang:${PASSWORD}@info7275-group1.vfvn5.mongodb.net/${DB_NAME}?retryWrites=true&w=majority`;
// Prints "MongoError: bad auth Authentication failed."
mongoose.connect(uri, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
  useFindAndModify: false,
  useCreateIndex: true,
  serverSelectionTimeoutMS: 5000
}).catch(err => console.log(err.reason));

mongoose.connection.on('connected', () => 
    console.log("Mongoose is connected!")
);


var app = express();

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

routes(app);


export default app;
