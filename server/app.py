from src.server import Server
from src.sync import Sync
import json
import time
import threading

DB_PATH = "database.db"
FRIENDS_LIST_PATH = "friends.json"
PORT = 5000

def auto_sync():
    while True:
        with open(FRIENDS_LIST_PATH, 'r') as f:
            friends = json.load(f)

        sync = Sync(friends, DB_PATH)
        sync.sync()
        time.sleep(10)

if __name__ == '__main__':
    open(FRIENDS_LIST_PATH, 'w').close()
    with open(FRIENDS_LIST_PATH, 'r') as f:
        try:
            friends = json.load(f)
        except:
            friends = []
            with open(FRIENDS_LIST_PATH, 'w') as f:
                json.dump(friends, f)
        


    server = Server(DB_PATH)

    t2 = threading.Thread(target=auto_sync)
    server.start(PORT)