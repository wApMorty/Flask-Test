import os
from flask import Flask, render_template, request

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/menu&authorized=true/')
def menu():
    return render_template('menu.html')

@app.route('/result/')
def result():
    target = os.path.join(APP_ROOT, 'images/')

    if not os.path.isdir(target):
        os.mkdir(target)
    
    print ("Connected !")

    for f in request.files.getlist("input-folder-2[]"):
        filename = f.filename
        print(filename)
        destination = "/".join([target, filename])
        print(destination)
        f.save(destination)

    return render_template('analyse.html')
