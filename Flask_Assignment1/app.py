from flask import Flask
import json

app = Flask(__name__)

@app.route('/api')
def api_data():
    file = open('data.json','r')
    data = json.load(file)
    return data

if __name__ == '__main__':
    app.run(debug=True)