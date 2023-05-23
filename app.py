from flask import Flask, render_template
from waitress import serve

#there is an install process for windows, 
# see https://www.sqlite.org/download.html
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'star'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    #creates a 'dictionary cursor', so we can ask for post['created'] instead of post[0]
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    posts = [{"id": post["id"], 'created': post['created'], "title": post["title"], "content": post["content"]} for post in posts]
    return render_template('base.html', posts=posts)

if __name__ == "__main__": 
    serve(app, host="0.0.0.0", port=8000)
