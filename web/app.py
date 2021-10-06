import spacy
from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class Detect(Resource):
    """
    Takes a post request and calculates the similarity score of the string values.
    INPUT: JSON object
    OUTPUT: JSON object
    EXAMPLES:
    """

    def post(self):
        """
        Extracts the string values based on the keys from the json object.
        The extracted values are then passed on the trained spacy model which
        computes their similarity score
        STRING INPUT CASE:
            text1 = "Cosine similarity"
            text2 = "Cosine similarity"
            text1 = similarity_score_model(text1)
            text2 = similarity_score_model(text2)
            OUTPUT = (text1.similarity(text2))
            print (type(OUTPUT))
            <class 'float'>
            print (len(OUTPUT))
            1
            print (OUTPUT)
            0.326332
        """
        try:
            postedData = request.get_json()
            text1 = postedData["text1"]
            text2 = postedData["text2"]

            similarity_score_model = spacy.load('en_core_web_sm')
            text1 = similarity_score_model(text1)
            text2 = similarity_score_model(text2)

            similarity_score = text1.similarity(text2)  # calculates similarity of our given sentences
            retJson = {
                "status": 200,
                "similarity": similarity_score,
                "msg": "Similarity score calculated succesfully"
            }
            return jsonify(retJson)
        except TypeError:
            retJson = {
                "status": 303,
                "msg": "text fields cannot be empty"
            }
            return jsonify(retJson)


api.add_resource(Detect, '/detect')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
