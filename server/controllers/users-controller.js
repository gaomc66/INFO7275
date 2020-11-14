import * as userService from "../services/users-service";
import {response, request} from "express";


// define render error function
const renderErrorResponse = (response) => {
    const callback = (error) => {
        if(error) {
            response.status(500);
            response.json({
                message: error.message
            });
        }
    };
    return callback;
}
export const save = (request, response) => {
    let body = request.body;
    // body["appSessionID"]= request.params.id;
    const newUser = Object.assign({},body);
    const resolve = (reports) => {
        response.status(200);
        response.json(reports);
    };
    userService.save(newUser)
        .then(resolve)
        .catch(renderErrorResponse(response));
}

// define get item controller
export const get = (request, response) => {
    const userID = request.params.id;

    const resolve = (theUser) => {
        response.status(200);
        response.json(theUser);
    };
    userService.find(userID)
        .then(resolve)
        .catch(renderErrorResponse(response));
};

export const list = (request, response) =>{
    const resolve = (res) => {
        response.status(200);
        response.json(res);
    };
    userService.listAllUsers()
        .then(resolve)
        .catch(renderErrorResponse(response));
}

