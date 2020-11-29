import User from "../models/user"


export const save = (user) => {
    const newUser = new User(user);
    const promise = newUser.save();
    return promise;
}

// findByID service implementation
export const find = (id) => {
    const promise = User.find(
        {UserID:id}
    ).exec();
    return promise;
};

export const listAllUsers = ()=>{
    const promise = User.find().exec();
    return promise;
}