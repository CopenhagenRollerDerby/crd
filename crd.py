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

home_team = [
    ('img/home/switch_00.jpg', '#00 Switch'),
    ('img/home/tumbleweed_111.jpg', '#111 Tumbleweed'),
    ('img/home/frix_12.jpg', '#12 Frix'),
    ('img/home/calm_storm_14.jpg', '#14 Calm Storm'),
    ('img/home/evig_hvad_1984.jpg', '#1984 Evig Hvad'),
    ('img/home/lix_2.jpg', '#2 Lix'),
    ('img/home/amargeddon_2300.jpg', '#2300 Amargeddon'),
    ('img/home/poison_candy_236.jpg', '#236 Poison Candy'),
    ('img/home/zenobia_240.jpg', '#240 Zenobia'),
    ('img/home/sibling_30.jpg', '#30 Sibling'),
    ('img/home/speeda_42.jpg', '#42 Speeda'),
    ('img/home/alex_54.jpg', '#54 Alex'),
    ('img/home/olivia_5458.jpg', '#5458 Olivia'),
    ('img/home/cosmonaut_63.jpg', '#63 Cosmonaut'),
    ('img/home/tango_maureen_855.jpg', '#855 Tango Maureen'),
    ('img/home/dana_might_311.jpg', '#311 Dana Might'),
]




@app.route('/')
def index():
    home = os.listdir('static/img/home')
    return render_template('index.html')

@app.route('/away')
def away():
    return render_template('away.html', away_team=away_team)

@app.route('/home')
def home():
    return render_template('home.html', home_team=home_team)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
