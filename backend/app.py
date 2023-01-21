from flask import Flask, request
import flask
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route('/users', methods=["GET", "POST"])
def users():
    print("users endpoint reached...")
    # if request.method == "GET":
    #     # Testing server json data
    #     with open("users.json", "r") as f:
    #         data = json.load(f)
    #         data.append({
    #             "username": "user4",
    #             "pets": ["hamster"]
    #         })
    #         return flask.jsonify(data)

    if request.method == "POST":
        received_data = request.get_json()
        message = received_data['data']     # message = document from user

        ########################
        # Manipulate data 
        ########################
        
        return flask.Response(status=201)

if __name__ == "__main__":
    app.run("localhost", 6969)