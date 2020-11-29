import mongoose from 'mongoose';
const Schema = mongoose.Schema;

const UserSchema = new Schema({
    UserID:{
        type: String
    },
    FirstName:{
        type: String
    },
    LastName:{
        type: String
    },
    Gender:{
        type: String
    },
    AgeGroup_ID:{
        type: String
    },
    Race_ID:{
        type: String
    },
    Occupation_ID:{
        type: String
    }
}, {collection: 'User'})

export default mongoose.model('User', UserSchema);