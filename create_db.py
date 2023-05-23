#this is creating the space that others will interact with
#Unlike HTML, we can let everyone read and write to the database.

import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)", ('First Post!', 'Content for 1st Post'))
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)", ('2nd Post :P', 'Content for 2nd Post!'))

#commit is necessary for when we have other readers of the database
connection.commit()
connection.close()
