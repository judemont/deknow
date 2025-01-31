from flask import Flask, jsonify, request, send_file
from database import Database

class Server:
    def __init__(self, db_path):
        self.db_path = db_path
        self.app = Flask(__name__)
        self.db = Database(db_path)
        self.setup_routes()

    def setup_routes(self):
        @self.app.route("/")
        def hello():
            return "Hello World"

        @self.app.route("/pages")
        def get_pages():
            pages = self.db.get_pages()
            pagesData = []
            for page in pages:
                pagesData.append({
                    "id": page[0],
                    "title": page[1],
                    "content": page[2]
                })
            return jsonify(pagesData)

        @self.app.route("/db")
        def get_db():
            return send_file(self.db_path, download_name="database.db")

        @self.app.route("/new", methods=["POST", "GET"])
        def new_page():
            if request.method == 'POST':
                title = request.form['title']
                content = request.form['content']
            elif request.method == 'GET':
                title = request.args.get('title')
                content = request.args.get('content')

            print(title, content)
            self.db.new_page(title, content)
            return jsonify({"success": True})

    def start_server(self, port):
        self.app.run(port=port)

