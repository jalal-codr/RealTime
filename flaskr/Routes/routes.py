from flask import  Blueprint
# from ..db import db
from ..Controllers.Uploads.imageUploads import getImages
from ..Controllers.Hello.hello import sayHello


bp = Blueprint('hello', __name__)

@bp.route('/')
def index():
    return sayHello()
       

@bp.route('/uploadImages',methods=['POST'])
def uploadImage():
    try:
        data = getImages()
        return(data)
    except Exception as e:
        return(e)
    
    
      