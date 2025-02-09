from flask import Flask, jsonify, request, send_file
from .database import Database
from flask_cors import CORS


class Server:
    def __init__(self, db_path):
        self.db_path = db_path
        self.app = Flask(__name__)
 
        CORS(self.app)  # Enable CORS for all routes

        self.db = Database(db_path)
        self.setup_routes()

    def setup_routes(self):
        @self.app.route("/api")
        def hi():
            return "Hello World"

        @self.app.route("/api/pages")
        def get_pages():
            pages = self.db.get_pages()
            pagesData = []
            for page in pages:
                pagesData.append({
                    "id": page[0],
                    "title": page[1],
                    "content": page[2],
                    "last_updated": page[3]
                })
            return jsonify(pagesData)

        @self.app.route("/api/db")
        def get_db():
            return send_file(self.db_path, download_name="database.db")

        @self.app.route("/api/new", methods=["POST", "GET"])
        def new_page():
            if request.method == 'POST':
                title = request.form['title']
                content = request.form['content']
            elif request.method == 'GET':
                title = request.args.get('title')
                content = request.args.get('content')

            if title is None or content is None:
                return jsonify({"success": False, "error": "Title or content not provided"})

            self.db.new_page(title, content)
            return jsonify({"success": True})
        
        @self.app.route("/api/update", methods=["POST", "GET"])
        def update():
            if request.method == 'POST':
                id = request.form['id']
                title = request.form['title']
                content = request.form['content']

            elif request.method == 'GET':
                id = request.args.get('id')
                title = request.args.get('title')
                content = request.args.get('content')

            self.db.update_page(id, title, content)
            
        


    def start(self, port):

        self.app.run(port=port)

