import express from 'express';
import userRouter from './user-router';
var router = express.Router();



export default (app) => {
  //set routes
  app.use('/',userRouter);
};
