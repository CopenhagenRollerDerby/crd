import os

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    home = os.listdir('static/img/home')
    away = [f'img/away/{file}' for file in os.listdir('static/img/away')]
    print(away)
    return render_template('index.html', away=away, home=home)
