from flask import Flask, request, jsonify, make_response
from mutant import isMutant
# import json

app = Flask(__name__)
app.config["DEBUG"] = False

@app.route('/mutant', methods=['POST'])
def checkMutant():
    mutant = isMutant(request.get_json())
    if mutant:
        return make_response("Is mutant", 200)
    else:
        return make_response("Is not mutant", 403)


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)