## #To Create a database in MongoDB and Connect with the Python Flask Framework 

# from flask import Flask, render_template, request
# import subprocess as sp
# from pymongo import MongoClient
# from mongopass import mongopass

# app= Flask("app")

# client = MongoClient(mongopass)
# db = client.mongodb
# myCollection = db.book


# @app.route("/")
# def my_home():
    
#     return render_template("home.html")


from flask import Flask, render_template, request, jsonify
from flask_pymongo import PyMongo
import json

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mongodb' #To connect the Mongodb compass and Database (book)

mongo = PyMongo(app)

db_operations = mongo.db.book


@app.route("/", methods = ['GET', 'POST'])
def home():
    
    if request.method == "POST":
        data = request.form 
        # mongo.db.book.insert_many([dict(title=data['title']), dict(author=data['author']), dict(language= data['language'])])
        phonenos = list(data['phonenos'].split(",")) 
        mongo.db.book.insert_many([dict(title=data['title'],author=data['author'],language= data['language'], phonenos= phonenos ,dateofbirth = data['dateofbirth'])])
        


        # print(data)
    return render_template("home.html")


#To Read the Collection Details

@app.route("/read")
def read_data():

    book = db_operations.find()
    book_details = [{'Name' : data['title'], 'Author' : data['author'], 'Language': data['language']} for data in book]
    #print(output)
    return jsonify(book_details)        


#To Delete the Collection field detail

@app.route("/delete")
def delete():
    
    filter = {'author': 'Velkumar'}
    db_operations.delete_one(filter)
    print(filter)
    result = {'result': 'One detail deleted successfully'}
    return result

#To Update the Collection 


@app.route("/update")
def update():
    update_title = {"$set":{'title': 'Arunchol'}}
    filter = {'author': 'Velkumar'}
    db_operations.update_one(filter, update_title)
    result = {'result': 'Updated Successfully'}
    return result





if __name__  ==  "__main__":
    app.run(debug= True)





