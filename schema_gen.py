from operator import concat
import os
def schema_creator(model_directory_path,schema_models_folder_name,path):
    name = input('enter name of your schema:')
    file_name = concat(name,'.js')
    os.chdir(model_directory_path)
    with open(file_name,'a') as file:
       boilerplate1 = "const mongoose = require('mongoose') \nconst Schema = mongoose.Schema \nconst {}Schema = new Schema(*Define Your Schema*) \n".format(name)
       boilerplate2 = "const {} = mongoose.model('{}', {}Schema) \n".format(name,name,name)
       boilerplate3 = "module.exports = {} \n".format(name)
       file.write(boilerplate1)
       file.write(boilerplate2)
       file.write(boilerplate3)
    os.chdir(path)
    with open('index.js','a') as file:
        boilerplate = "const {} = require(path.resolve(__dirname, './{}/{}')) \n".format(name,schema_models_folder_name,file_name)
        file.write(boilerplate)


