import json
from flask import Flask, request, Response
from src.main.controllers.controller import Controller1
from src.main.utils.core import config, loggerx

app = Flask(config.application.name)
controller = Controller1(config)

@app.route('/')
def running():
    return "Notes Running"

@app.route('/api/v1/notes/', methods=['POST'])
def create():
    try:
        if request.is_json:
            payload = request.get_json()
            result = controller.create(payload=payload)
            if result:
                return Response(json.dumps(result), status=201, mimetype='application/json')
            return Response(json.dumps({}), status=204, mimetype='application/json')
        return {}, 500
    except Exception as e:
        loggerx.error(e)
        return {}, 500

@app.route('/api/v1/notes/<id>', methods=['PUT'])
def update(id):
    try:
        if request.is_json:
            payload = request.get_json()
            result = controller.update(id=id, payload=payload)
            if result:
                return Response(json.dumps(result), mimetype='application/json')
            return Response(json.dumps({}), status=204, mimetype='application/json')
        return {}, 500
    except Exception as e:
        loggerx.error(e)
        return {}, 500

@app.route('/api/v1/notes/<id>', methods=['DELETE'])
def delete(id):
    try:
        result = controller.delete(id=id)
        if result:
            return Response(json.dumps(result), mimetype='application/json')
        return Response(json.dumps({}), status=204, mimetype='application/json')
    except Exception as e:
        loggerx.error(e)
        return {}, 500

@app.route('/api/v1/notes/<id>', methods=['GET'])
def get(id):
    try:
        result = controller.get(id=id)
        if result:
            return Response(json.dumps(result), mimetype='application/json')
        return Response(json.dumps({}), status=204, mimetype='application/json')
    except Exception as e:
        loggerx.error(e)
        return {}, 500

@app.route('/api/v1/notes/', methods=['GET'])
def get_all():
    try:
        accountId = request.args.get("accountId")
        orderBy = request.args.get("orderBy")
        offset = request.args.get("offset")
        limit = request.args.get("limit")
        result = controller.get_all(accountId=accountId)
        if result:
            return Response(json.dumps(result), mimetype='application/json')
        return Response(json.dumps({}), status=204, mimetype='application/json')
    except Exception as e:
        loggerx.error(e)
        return {}, 500

@app.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response
