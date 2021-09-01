import os
import json
import random, string
from flask import Flask, jsonify, render_template, url_for
from flask import abort
from flask import make_response
from flask import request
from datamanager import DataManager
import configparser
from multiprocessing import Process

app = Flask(__name__)
dataManager = DataManager()

    
@app.route('/classes', methods=['GET'])
def getAllData():
    return jsonify(dataManager.getAllData())
    
@app.route('/classes/<node>')
def get_node(node):
    r = dataManager.getNode(node, request.args.to_dict())
    if r == None:
        return abort(404)
    else:
        return jsonify(r)
        
@app.route('/classes/<node>/<row_id>', methods=['GET'])
def get_node_id(node,row_id):
    r = dataManager.getObjectForId(node,row_id)
    if len(r) == 0:
        abort(404)
    else:
         return jsonify(r)
         
@app.route('/classes/<node>', methods=['POST'])
def create(node):
    if not request.json:
        abort(400)
    return jsonify(dataManager.addRow(node,request.json))
    
@app.route('/classes/<node>/<row_id>', methods=['PUT'])
def update(node,row_id):
    if not request.json:
        print("non ce richiesta " + str(request.json))
        abort(400)
    return jsonify(dataManager.editRow(node,row_id,request.json))
    
@app.route('/classes/<node>/<row_id>', methods=['DELETE'])
def delete(node,row_id):
    return jsonify(dataManager.delete(node,row_id))
    
@app.route('/classes/logs/<mode>', methods=['GET'])
def import_logs(mode):
    if mode != "all" and mode != "new":
        return jsonify(dataManager.getNode("logs", {"objectId":mode}))
    edit = True
    if request.args.to_dict():
        for key,value in request.args.to_dict().items():
            if key == "edit":
                if value == "0":
                    edit = False
    return jsonify(dataManager.importLogs(mode, edit))
    
@app.route('/classes/devicename', methods=['GET'])
def getDeviceName():
    return dataManager.getDeviceName() + "\n"


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(500)
def internal_error(error):
    return make_response(jsonify({'error': 'Internal Server Error'}), 500)

@app.route('/')
def index():
    return "Time Attendence Rest API" + "\n"

def randomword(length):
	return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))
   

def runServer():
    app.use_reloader = False
    app.run(debug=False, host='0.0.0.0')
    
if __name__ == '__main__':
    runserver()
	
