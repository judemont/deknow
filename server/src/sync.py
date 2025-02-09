import requests
from .database import Database

class Sync:
    def __init__(self, friends, db_path):
        self.friends = friends
        self.db_path = db_path
    
    def sync(self):
        db = Database(self.db_path)

        print("Syncing DB with friends")

        i=0
        for friend in self.friends:
            print(f"Syncing DB with {friend}")
            print(f"{i}/{len(self.friends)}")
            response = requests.get(f"{friend}/pages")
            pages = response.json()

            for page in pages:
                title, content, last_updated = page["title"], page["content"], page["last_updated"]
                matching_pages = db.get_page(title=title)

                if len(matching_pages) == 0:    
                    db.new_page(title, content)
                else:
                    if last_updated > matching_pages[0][3]:
                        db.update_page(matching_pages[0][0], title, content)
            i+=1

        print("Sync complete")
