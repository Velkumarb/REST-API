#To Create the new database books (mysql)

import pymysql

conn = pymysql.connect(
       host='sql6.freesqldatabase.com',
       database='sql6586572',
       user='sql6586572',
       password='bXcQh859jp',
       charset='utf8mb4',
       cursorclass=pymysql.cursors.DictCursor # To get the result in dictionary
)
cursor = conn.cursor()
sql_query = """ CREATE TABLE book (
        id integer PRIMARY KEY, 
        author text NOT NULL, 
        language text NOT NULL,
        title text NOT NULL
)"""
cursor.execute(sql_query)
conn.close() #To Close the Database Connection

