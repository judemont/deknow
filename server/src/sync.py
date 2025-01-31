import requests
from database import Database

class sync:
    def __init__(self, friends, db_path):
        self.friends = friends
        self.db_path = db_path
    
    def sync(self):
        db = Database(self.db_path)

        print("Syncing DB with friends")

        for friend in self.friends:
            print(f"Syncing DB with {friend}")
            response = requests.get(f"{friend}/pages")
            pages = response.json()

            for page in pages:
                
            
            
            
