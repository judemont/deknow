from flask import Flask, jsonify, request
from src.database import Database

app = Flask(__name__)
db = Database("database.db")

@app.route("/")
def hello():
    return "Hello World"

@app.route("/pages")
def get_pages():
    pages = db.get_pages()
    return jsonify(pages)

@app.route("new", methods=["POST", "GET"])
def new_page(title, content):
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

    elif request.method == 'GET':
        title = request.args.get('title')
        content = request.args.get('content')


    db.new_page(title, content)
    return jsonify({"success": True})