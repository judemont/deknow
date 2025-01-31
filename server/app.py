from flask import Flask, jsonify, request, send_file
from src.database import Database
from src.server import Server
import json

DB_PATH = "database.db"
FRIENDS_LIST_PATH = "friends.json"
PORT = 5000


if __name__ == '__main__':
    with open(FRIENDS_LIST_PATH, 'r') as f:
        friends = json.load(f)
    