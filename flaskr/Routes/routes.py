from flask import  (Blueprint,Flask,redirect, request)
# from ..db import db
from ..Controllers.Hello.hello import sayHello


bp = Blueprint('hello', __name__)

@bp.route('/')
def index():
    x = sayHello()
    return(x)   

@bp.route('/uploadImage')
def uploadImage():
    x = sayHello()
    return(x)  