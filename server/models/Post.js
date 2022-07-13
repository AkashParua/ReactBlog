const mongoose = require('mongoose') 
const Schema = mongoose.Schema 
const PostSchema = new Schema({Title: String,Author: String,Body: String}) 
const Post = mongoose.model('Post', PostSchema) 
module.exports = Post 
