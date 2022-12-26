#To Create the Simple REST API (FLASK and JSON) and Test with POSTMAN 

#In Memory Book Lsit Objects

#To import the libraries 

from flask import Flask, request, jsonify

app = Flask(__name__)


#To create the List of Books Objects


books_list =[
    {
        "id": 0,
        "author": "Jaya Kanthan",
        "language": "Tamil",
        "title": "Sila Nerangalil Sila Manithargal"
    },
    {
        "id": 1,
        "author": "Cyber Simman",
        "language": "Tamil",
        "title": "Nam Kalathu Nayagargal"
    },
    {
        "id": 2,
        "author": "Tiruvalluvar",
        "language": "Tamil",
        "title": "Thirukkural",
    }
]

# @app.route("/")

@app.errorhandler(404) 
def invalid_route(e): 
    return "Invalid route."

@app.route('/books', methods = ['GET', 'POST'])

#To create the function books

def books():
    if request.method == 'GET':
        if len(books_list) > 0:
            return jsonify(books_list)
        else:
            return 'Nothing Found', 404


#To create the POST method and insert to the new book details

    if request.method == "POST":
        new_author = request.form['author']
        new_language = request.form['language']
        new_title = request.form['title']
        iD = books_list[-1]['id']+1 #Auto increment
        # iD = books_list +1
        

        new_obj ={
            'id': iD,
            'author': new_author, 
            'language': new_language,
            'title': new_title     
            }

#In that new_obj we finally append the id, author, language, title object details 
# Here we use in memory list to post the data only on run time

        books_list.append(new_obj)
        return jsonify(books_list), 201 

@app.route('/book/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_book(id):
    if request.method == "GET":
        for book in books_list:
            if book['id'] == id:
                return jsonify(book)
            pass    

    if request.method == "PUT":
        for book in books_list:
            if book['id'] == id:
                book['author'] = request.form['author']
                book['language'] = request.form['language']
                book['title'] = request.form['title']

                updated_book ={
                    'id': id,
                    'author': book['author'],
                    'language':book['language'],
                    'title': book['title']
                    } 

                return jsonify(updated_book)  

    if request.method == "DELETE":
        for index, book in enumerate(books_list):
            if book['id'] == id:
                books_list.pop(index)
                return jsonify(books_list)
       

#To run the App

if __name__ == '__main__':
    app.run(debug= True)