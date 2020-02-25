import os
import shutil
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
IMAGE_FOLDER = os.path.join('static','images')

app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER

@app.route('/')
@app.route('/index/')
def index():
    # Destruction de l'ancien dossier de traitement au lancement de l'appli
    if os.path.isdir(os.path.join(APP_ROOT,IMAGE_FOLDER)):
        shutil.rmtree(os.path.join(APP_ROOT,IMAGE_FOLDER))
    return render_template('index.html')

@app.route('/menu&authorized=true/')
def menu():
    return render_template('menu.html')

@app.route('/result/', methods=['POST'])
def result():

    target = os.path.join(APP_ROOT, IMAGE_FOLDER)

    if not os.path.isdir(target):
        os.mkdir(target)

    if not os.path.isdir(os.path.join(target, 'analysedPictures')):
        os.mkdir(os.path.join(target, 'analysedPictures'))

    for f in request.files.getlist("input-folder-2[]"): 
        filename = f.filename.split("/")[-1]
        destination = "/".join([target, filename])
        f.save(destination)

    os.system("python "+ os.path.join('tensorflow2','models','research','object_detection','Object_detection_image.py'))
    imageAnalysed = os.listdir(os.path.join(APP_ROOT, IMAGE_FOLDER,"analysedPictures"))
    listUrl = []
    for image in imageAnalysed:
        listUrl.append(url_for('static',filename='images/analysedPictures/' + image))

    return render_template('analyse.html',
                            lURL = listUrl,
                            lImages = imageAnalysed
                            )
                            