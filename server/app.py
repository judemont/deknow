from src.server import Server
from src.sync import Sync
import json
import time
import threading

DB_PATH = "database.db"
FRIENDS_LIST_PATH = "friends_2.json"
PORT = 5000

def auto_sync():
    while True:
        with open(FRIENDS_LIST_PATH, 'r') as f:
            friends = json.load(f)

        sync = Sync(friends, DB_PATH)
        sync.sync()
        time.sleep(10)

if __name__ == '__main__':
    try:
        with open(FRIENDS_LIST_PATH, 'r') as f:
            friends = json.load(f)
    except:
        friends = []
        with open(FRIENDS_LIST_PATH, 'w') as f:
            json.dump(friends, f)
        


    server = Server(DB_PATH)

    autosync_t = threading.Thread(target=auto_sync)
    autosync_t.start()
    server.start(PORT)