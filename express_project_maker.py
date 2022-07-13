import importlib
from ntpath import join
import os
from schema_gen import schema_creator
name = input("Enter project Name:")
parent_dir = os.getcwd()
path = os.path.join(parent_dir, name)
# creating a node project folder with the given name
os.mkdir(path)
# changing the current directory to newly made node project folder
os.chdir(path)
# heceforth path is the root directory
# installing required libraries
os.system('npm init')
os.system('npm install express')
os.system('npm install path')
os.system('npm install ejs')
os.system('npm install mongoose')
os.system('npm install body-parser')
# input name for folder containg static data
static_folder_name = input('Folder to include static CSS,image etc.:')
path_static = os.path.join(path, static_folder_name)  # path to static files
os.mkdir(path_static)
# input folder name to store schema
schema_models_folder_name = input('Folder contaning schema:')
path_models = os.path.join(path, schema_models_folder_name)  # path to schema models
os.mkdir(path_models)
# creatign the views file
views = "views"
path_views = os.path.join(path,views)
os.mkdir(path_views)
# current directory path -->path
# views folder path      -->path_views
# static folder path     -->path_static
# models folder path     -->path_models
# writing the oilerplate for index.js
port = input("preferred port in localhost:")
with open("index.js",'a') as file:
    boilerplate1 = "const express = require('express') \nconst path = require('path') \nconst app = express() \nconst ejs = require('ejs') \nconst mongoose = require('mongoose') \nconst bodyParser = require('body-parser') \n"
    file.write(boilerplate1)
    boilerplate2 = "app.use(express.static('{}')) \napp.set('view engine','ejs') \napp.listen({},()=>{{console.log( )}}) \n".format(static_folder_name,port)
    file.write(boilerplate2)
    boilerplate3 = "app.use(bodyParser.json()) \napp.use(bodyParser.urlencoded({ extended: false })) \n"
    file.write(boilerplate3)
print("Include your .ejs files in views\nYour Schema Models in {}\nYour static files in {}\n ".format(schema_models_folder_name,static_folder_name))    
choice = input("Include Schema Model(s)? Y/n:")
if choice == 'Y':
    n =int(input("No of Schema ? "))
    for i in range(n):
        schema_creator(path_models,schema_models_folder_name,path)




