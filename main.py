from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# ⚠ Hardcoded MongoDB connection details (unsecure for public repos)
MONGO_URL = "mongodb+srv://username:password@cluster0.mongodb.net/"
DB_NAME = "test"

# Connect to MongoDB
client = MongoClient(MONGO_URL)
db = client[DB_NAME]

@app.route("/")
def home():
    return "MongoDB Full Database Viewer (Render Ready - Hardcoded URL)"

@app.route("/data")
def get_full_db():
    db_data = {}
    for collection_name in db.list_collection_names():
        db_data[collection_name] = list(db[collection_name].find({}, {"_id": 0}))
    return jsonify(db_data)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
