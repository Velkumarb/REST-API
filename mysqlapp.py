# #To Create a database in Sqlite and Connect with the Python Flask Framework 


# #To Create the Simple REST API (FLASK and JSON) and Test with POSTMAN 


from flask import Flask, request, jsonify
import json
import pymysql




app = Flask(__name__)


def db_connection():
    conn = None
    try:
        conn = pymysql.connect(host='sql6.freesqldatabase.com',
                                database='sql6586572',
                                user='sql6586572',
                                password='bXcQh859jp',
                                charset='utf8mb4',
                                cursorclass= pymysql.cursors.DictCursor)
    except pymysql.error as e:
        print(e)
    return conn


@app.route("/books", methods=["GET", "POST"])
def books():
    conn = db_connection()
    cursor = conn.cursor()
    
    
    if request.method == "GET":
        cursor = conn.execute("SELECT * FROM book")
        books = [
            dict(id=row['id'], author=row['author'], language=row['language'], title=row['title'])
            for row in cursor.fetchall()
        ]
        if books is not None:
            return jsonify(books)

    if request.method == "POST":
        new_author = request.form["author"]
        new_lang = request.form["language"]
        new_title = request.form["title"]
        sql = """INSERT INTO book (author, language, title)
                 VALUES (%s, %s, %s)"""
        cursor = cursor.execute(sql, (new_author, new_lang, new_title))
        conn.commit()
        return "Book with the id:  created successfully", 201


@app.route('/book/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_book(id):
    conn = db_connection()
    cursor = conn.cursor()
    book = None
    if request.method == "GET":
        cursor.execute("SELECT * FROM book WHERE id=%s", (id,))
        rows = cursor.fetchall()
        for r in rows:
            book = r
        if book is not None:
            return jsonify(book), 200 
        else:
            return "Something Wrong", 404
 

    if request.method == "PUT":
        sql = """UPDATE book
                SET author=?,
                    language=?,
                    title=?
                WHERE id=? """

        author = request.form["author"]
        language = request.form["language"]
        title = request.form["title"]
        updated_book = {
            "id": id,
            "author": author,
            "language": language,
            "title": title,
        }
        cursor.execute(sql, (author, language, title, id))
        conn.commit()
        return jsonify(updated_book)

    if request.method == "DELETE":
        
        sql = """ DELETE FROM book WHERE id=5 """
        print("hi" + sql)
        cursor.execute(sql)
        conn.commit()
        return "success.".format(id), 200
     
    # if request.method == "DELETE":
    #     sql = """ DELETE FROM book WHERE id=? """
    #     cursor.execute(sql, (id,))
    #     conn.commit()
    #     return "The book with id:  has been deleted.".format(id), 200


#To run the App

if __name__ == '__main__':
    app.run(debug= True)