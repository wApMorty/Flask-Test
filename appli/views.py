import os
from flask import Flask, render_template, request
from tensorflow2.models.research.object_detection.Object_detection_image import analyseBoue

app = Flask(__name__, static_folder="static/images")

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
IMAGE_FOLDER = os.path.join('static','images')

app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/menu&authorized=true/')
def menu():
    return render_template('menu.html')

@app.route('/result/', methods=['POST'])
def result():

    target = os.path.join(APP_ROOT, IMAGE_FOLDER)
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)
    
    print ("Connected !")

    for f in request.files.getlist("input-folder-2[]"):
        filename = f.filename.split("/")[-1]
        print(filename)
        destination = "/".join([target, filename])
        print(destination)
        f.save(destination)
        
        # first_picture=os.listdir(target)[0]

    analyseBoue(os.path.abspath(IMAGE_FOLDER))

    return render_template('analyse.html', first_pic = os.listdir(target)[0])
