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

    if request.method == "POST":
        received_data = request.get_json()
        message = received_data['data']     # message = full document from user

        ########################
        # Manipulate data 
        ########################

        ## NLP results examples
        example = {
            "midterm1" : "3/11/2023",
            "midterm2" : "....date",
            "assignment 1" : "asdasdasd",
        }
        
        return flask.Response(status=201)

if __name__ == "__main__":
    app.run("localhost", 6969)