from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/menu&authorized=true/')
def menu():
    return render_template('menu.html')

