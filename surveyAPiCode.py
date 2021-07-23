from flask import Flask, make_response, jsonify, request

import sqlite3


app = Flask(__name__)
#db = dataset.connect('api.db')#connect the api1
db= sqlite3.connect('Surveys.db')


table = db['Surveys']


def fetch_db(name):  
    return table.find_one(name=name)


def fetch_db_all():
    surveys = []
    for survey in table:
        surveys.append(book)
    return surveys


@app.route('/api/db_populate', methods=['GET'])
def db_populate():
    table.insert({
        "name": "dh",
        "age": "22",
        "branch": "cse"
    })

    table.insert({
        "name": "ch",
        "age": "23",
        "branch": "me"
    })

    return make_response(jsonify(fetch_db_all()),
                         200)


@app.route('/api/Surveys', methods=['GET', 'POST'])
def api_Surveys():
    if request.method == "GET":
        return make_response(jsonify(fetch_db_all()), 200)
    elif request.method == 'POST':
        content = request.json
        name= content['name']
        table.insert(content)
        return make_response(jsonify(fetch_db(name)), 201)  


@app.route('/api/Surveys/<name>', methods=['GET', 'PUT', 'DELETE'])
def api_each_Surveys(name):
    if request.method == "GET":
        Surveys_obj = fetch_db(name)
        if Surveys_obj:
            return make_response(jsonify(Surveys_obj), 200)
        else:
            return make_response(jsonify(Surveys_obj), 404)
    elif request.method == "PUT":  
        content = request.json
        table.update(content, ['name'])

        Surveys_obj = fetch_db(name)
        return make_response(jsonify(Surveys_obj), 200)
    elif request.method == "DELETE":
        table.delete(id=name)

        return make_response(jsonify({}), 204)


if __name__ == '__main__':
    app.run(debug=True)
