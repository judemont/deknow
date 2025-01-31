from flask import Flask, jsonify, request, send_file
from src.database import Database

DB_PATH = "database.db"
PORT = 5000

app = Flask(__name__)
db = Database(DB_PATH)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/pages")
def get_pages():
    pages = db.get_pages()
    pagesData = []
    for page in pages:
        pagesData.append({
            "id": page[0],
            "title": page[1],
            "content": page[2]
        })
    return jsonify(pagesData)

@app.route("/db")
def get_db():
    return send_file(DB_PATH, download_name="database.db")

@app.route("/new", methods=["POST", "GET"])
def new_page():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

    elif request.method == 'GET':
        title = request.args.get('title')
        content = request.args.get('content')

    print(title, content)
    db.new_page(title, content)
    return jsonify({"success": True})


if __name__ == '__main__':
    app.run(port=PORT)