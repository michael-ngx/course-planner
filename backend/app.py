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
        
        import spacy
        from spacy.matcher import Matcher

        with open ("learning-files/ece216.txt", "r") as f:
            text = f.read()
            
        nlp2 = spacy.load("en_core_web_sm")

        assignment_synonyms = ["labs","midterm","exam","homework","assignment"]
        matcher = Matcher(nlp2.vocab)
        pattern = [{"POS":"NOUN","TEXT":{"IN":assignment_synonyms}},
                {"ENT_TYPE": "DATE", "OP": "+"}]
        matcher.add("NOUN + DATE",[pattern],greedy="LONGEST")

        doc = nlp2(text)
        matches = matcher(doc)
        matches.sort(key = lambda x: x[1])

        for match in matches:
            print (match, doc[match[1]:match[2]])

        ## NLP results examples
        # example = {
        #     "midterm1" : "3/11/2023",
        #     "midterm2" : "4/24/2023",
        #     "assignments" : "weekly",
        # }
        
        return flask.Response(status=201)

if __name__ == "__main__":
    app.run("localhost", 6969)