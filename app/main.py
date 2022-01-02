import text2emotion as te
from flask import Flask, jsonify, request
from flask_cors import CORS
import nltk

# https://www.geeksforgeeks.org/deploy-python-flask-app-on-heroku/


# Example payload
# {
#     "corpus": [
#         {
#             "title": "Covid-19 : quelles sont les restrictions sanitaires mises en place à l'étranger ?"
#         },
#         {
#             "title": "Covid-19 en France : le variant Omicron, une menace pour l'hôpital ? • FRANCE 24"
#         },
#         {
#             "title": "happy new year 2022"
#         }
#     ]
# }

nltk.download('omw-1.4')

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["POST"])
def detect_emptions():
        body = request.get_json()

        for keyMedia in body.keys():
            for count, news in enumerate(body[keyMedia]):
                body[keyMedia][count]["emotions"] = te.get_emotion(news["description"]);
        
        
        return jsonify( 
            body
        )
