import sqlite3

class Database:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS pages (id INTEGER PRIMARY KEY, title TEXT, content TEXT)")

    def __del__(self):
        self.conn.close()

    def query(self, query, *args):
        self.cursor.execute(query, args)
        return self.cursor.fetchall()

    def execute(self, query, *args):
        self.cursor.execute(query, args)
        self.conn.commit()

    def new_page(self, title, content):
        self.execute("INSERT INTO pages (title, content) VALUES (?, ?)", title, content)

    def get_page(self, id):
        return self.query("SELECT * FROM pages WHERE id = ?", id)
    
    def get_pages(self):
        return self.query("SELECT * FROM pages")

    def update_page(self, id, title, content):
        self.execute("UPDATE pages SET title = ?, content = ? WHERE id = ?", title, content, id)

    def delete_page(self, id):
        self.execute("DELETE FROM pages WHERE id = ?", id)