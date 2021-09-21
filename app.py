import os
from flask import Flask
from dotenv import load_dotenv
from flask import jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId

load_dotenv()

app = Flask(__name__)

client = MongoClient(os.environ['MONGODB_URI'])
db = client.crystal
posts = db.posts


@app.route('/')
def root():
    return jsonify({
        "message": "hi!"
    })


@app.route('/posts')
def hello_world():  # put application's code here
    data = []
    cursor = posts.find()
    for i in cursor:
        i['_id'] = str(i['_id'])
        data.append(i)
    return jsonify(data)


@app.route('/post/<post_id>')
def get_post(post_id):
    post = posts.find_one({"_id": ObjectId(post_id)})
    if not post:
        return jsonify({
            'message': '404 not found'
        })

    post['_id'] = str(post['_id'])
    return jsonify(post)


if __name__ == '__main__':
    app.run()
