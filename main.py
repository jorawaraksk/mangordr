from flask import Flask, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

# Get MongoDB URL and DB name from environment
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017/")
DB_NAME = os.getenv("DB_NAME", "test")

# Connect to MongoDB
client = MongoClient(MONGO_URL)
db = client[DB_NAME]

@app.route("/")
def home():
    return "MongoDB Full Database Viewer"

@app.route("/data")
def get_full_db():
    db_data = {}
    for collection_name in db.list_collection_names():
        db_data[collection_name] = list(db[collection_name].find({}, {"_id": 0}))
    return jsonify(db_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
