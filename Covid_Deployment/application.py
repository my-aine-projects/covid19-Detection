from flask import *
import os
from werkzeug.utils import secure_filename
from predict import predict_covid
IMG_FOLDER = os.path.join('static', 'images')


application=Flask(__name__)
application.config['UPLOAD_FOLDER'] = IMG_FOLDER

@application.route('/')
def upload():
    return render_template("index.html")

@application.route('/success',methods=['POST'])
def success():
    if request.method=='POST':
        f=request.files['file']
        full_filename = os.path.join(application.config['UPLOAD_FOLDER'], secure_filename(f.filename))
        f.save(full_filename)
        outcome=predict_covid(full_filename)
        return render_template('success.html', prediction=outcome,url=full_filename)
    return render_template("index.html")

if __name__=='__main__':
    application.run(debug=True)


