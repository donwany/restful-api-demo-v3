import json
import os

import pymongo.errors
from flask import Flask, jsonify, request, Response
from pymongo import MongoClient
from bson.objectid import ObjectId, InvalidId
from bson.json_util import dumps

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

# set ENV for the mongodb
DB = os.environ.get("DB")
HOST = os.environ.get("MONGODB_HOST")
USERNAME = os.environ.get("MONGODB_USERNAME")
PASSWORD = os.environ.get("MONGODB_PASSWORD")
URL = "mongodb+srv://{0}:{1}@{2}/{3}?retryWrites=true&w=majority".format(USERNAME, PASSWORD, HOST, DB)

client = MongoClient(URL, serverSelectionTimeoutMS=5000)
db = client[f"{DB}"]


@app.route('/')
def base():
    return Response(response=json.dumps({"Status": "UP"}),
                    status=200,
                    mimetype='application/json')


@app.route("/api/v1.0/books", methods=['GET'])
def get_books():
    try:
        data = db.books.find({})
        return dumps(data)
    except Exception as e:
        return "An error occurred: {}".format(str(e)), 500


@app.route("/api/v1.0/books", methods=['POST'])
def create_book():
    data = request.get_json()
    if not data:
        return dumps({"error": "No Data Found"}), 400
    else:
        try:
            result = db.books.insert_one(data)
            output = {'Status': "Successfully Inserted", 'Document_ID': str(result.inserted_id)}
            return dumps(output), 201
        except pymongo.errors.PyMongoError as e:
            return jsonify({"error": str(e)}), 500


@app.route('/api/v1.0/books/<str:id>', methods=['GET'])
def read_book(id):
    try:
        _id = ObjectId(str(id))
    except InvalidId:
        return jsonify({"error": "Invalid ID provided"}), 400

    data = db.books.find_one({"_id": _id})
    if data is None:
        return jsonify({"error": f"Book with {_id} not found"}), 400
    return dumps(data)


@app.route('/api/v1.0/books/<str:id>', methods=['PUT'])
def update_book(id):
    try:
        _id = ObjectId(str(id))
    except InvalidId:
        return jsonify({"error": "Invalid ID provided"}), 400
    data = request.get_json()
    if not data:
        jsonify({"error": "No data provided."}), 400
    result = db.books.update_one({"_id": _id}, {'$set': data})
    output = {'Status': 'Successfully Updated' if result.modified_count > 0 else "Nothing was updated."}
    return dumps(output)


@app.route('/api/v1.0/books/<id>', methods=['DELETE'])
def delete_book(id):
    try:
        _id = ObjectId(str(id))
    except InvalidId:
        return jsonify({"error": "Invalid ID provided"}), 400
    result = db.books.delete_one({"_id": _id})
    output = {'status': 'Successfully Deleted' if result.deleted_count > 0 else "Document Not Found!"}
    return dumps(output)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
