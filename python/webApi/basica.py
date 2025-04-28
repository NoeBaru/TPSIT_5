from flask import Flask, jsonify, request
import requests

app = Flask(__name__)
@app.route('/api/v1/resources/books', methods = ['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id"
    
    results = []

    for book in books:
        if book['id'] == id:
            results.append(book)

    return jsonify(results)