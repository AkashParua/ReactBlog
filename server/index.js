const express = require('express') 
const path = require('path') 
const app = express() 
const ejs = require('ejs') 
const mongoose = require('mongoose') 
const bodyParser = require('body-parser') 
app.use(express.static('assets')) 
app.set('view engine','ejs') 
app.listen(8000,()=>{console.log( )}) 
app.use(bodyParser.json()) 
app.use(bodyParser.urlencoded({ extended: false })) 
const Post = require(path.resolve(__dirname, './models/Post.js')) 
mongoose.connect('mongodb://0.0.0.0/React_Database',{useNewUrlParser:true})
//POST response to take to create new Post
app.post('/post', async (req,res)=>{
    var {postTitle} = req.body
    var {postAuthor} = req.body
    var {postBody}   = req.body
   await Post.create({Title:postTitle,Author:postAuthor, Body:postBody},(error,Post)=>{console.log(error)})
    res.redirect('/')
})
//takes id and deletes the particular post
app.get('/delete/:postId',async (req,res)=>{
    var {postId} = req.params
    await Post.findByIdAndDelete(postId)
    res.redirect('/')
})
//takes id and updates the particular post
app.post('/update/:postId',async (req,res)=>{
    var {postId} = req.params
    var {postTitle} = req.body
    var {postAuthor} = req.body
    var {postBody}   = req.body
   await Post.findByIdAndUpdate(postId,{Title:postTitle,Author:postAuthor,Body:postBody})
   res.redirect('/')

})
//sending list of posts
app.get('/',async (req,res)=>{
       var Posts =await Post.find({})
       res.send(Posts)
})
//making search query
app.get('/search/:query', async (req,res)=>{
    var {query} = req.params
    query = query.trim()
    query = query
    console.log(query)
    var Posts = await Post.find({$or:[{Author:query},{Title:query},{Body:query}]})
    res.send(Posts)
})