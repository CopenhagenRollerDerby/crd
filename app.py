import os

from flask import Flask, render_template

app = Flask(__name__)

away_team = [
    ('img/away/kattriarken_11.jpg', '#11 Kattriarken'),
    ('img/away/bumblebee_26.jpg', '#26 Bumblebee'),
    ('img/away/zyltan_rr_08.jpg', '#08 Zyltan RR'),
    ('img/away/survival_of_the_fittigast_23.jpg', '#23 Survival of the Fittigast'),
    ('img/away/ouch_417.jpg', '#417 Ouch'),
    ('img/away/grim_29.jpg', '#29 Grim'),
    ('img/away/chips_6.jpg', '#6 Chips'),
    ('img/away/high_five_5.jpg', '#5 High Five'),
    ('img/away/seq_and_destroy_1894.jpg', '#1894 Seq and Destroy'),
    ('img/away/laylow_14.jpg', '#14 Laylow'),
    ('img/away/arty_85.jpg', '#85 Arty'),
    ('img/away/sugar_high_2.jpg', '#2 Sugar High'),
    ('img/away/bloody_guthrie_82.jpg', '#82 Bloody Guthrie'),
    ('img/away/exe_qt_403.jpg', '#403 Exe QT'),
    ('img/away/rullknufs_357.jpg', '#357 Rullknufs'),
]

away_team = sorted(away_team, key=lambda x: x[1])


@app.route('/')
def index():
    home = os.listdir('static/img/home')
    return render_template('index.html')

@app.route('/away')
def away():
    away = [f'img/away/{file}' for file in os.listdir('static/img/away')]
    return render_template('away.html', away_team=away_team)

@app.route('/home')
def home():
    away = [f'img/home/{file}' for file in os.listdir('static/img/home')]
    return render_template('home.html', away_team=away_team)
