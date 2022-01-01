import text2emotion as te
from flask import Flask, jsonify, request
from flask_cors import CORS
import nltk

nltk.download('omw-1.4')

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["POST"])
def detect_emptions():
        body = request.get_json()


        for count, news in enumerate(body["corpus"]):
            body["corpus"][count]["emotions"] = te.get_emotion(news["title"]);

        return jsonify( 
            body["corpus"]
        )
