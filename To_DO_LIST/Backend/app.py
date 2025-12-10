from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

client = MongoClient('MONGO_URI')
db = client["todo_db"]
todo_collection = db["todo_items"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    item_name = request.form.get('itemName')
    item_description = request.form.get('itemDescription')

    todo_collection.insert_one({
        "item_name": item_name,
        "item_description": item_description
    })

    return jsonify({"message": "To-Do item saved successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
