import os
from flask import Flask, request
from .Routes.routes  import bp as routes


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)

    UPLOAD_FOLDER = 'uploads/'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    @app.route('/upload', methods=['GET', 'POST'])
    def upload_file():
        if request.method == 'POST':
            # Check if the post request has the file part
            if 'file' not in request.files:
                return 'No file part'
            
            file = request.files['file']

            # If the user does not select a file, the browser submits an empty file without a filename
            if file.filename == '':
                return 'No selected file'
            
            if file:
                # Save the file to the specified directory
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                file.save(file_path)
                return f'File successfully uploaded to {file_path}'

        return '''
        <!doctype html>
        <title>Upload an Image</title>
        <h1>Upload an Image</h1>
        <form method=post enctype=multipart/form-data>
        <input type=file name=file>
        <input type=submit value=Upload>
        </form>
        '''


    app.register_blueprint(routes)

    return app