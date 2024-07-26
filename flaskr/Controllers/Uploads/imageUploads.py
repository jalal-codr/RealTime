import os
from flask import  request,jsonify


# def saveImage():

#     return

def getImages():
    data = request.get_json()
    return jsonify({"data":data})
  