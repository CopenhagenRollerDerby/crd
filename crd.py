import os

from flask import Flask, render_template

app = Flask(__name__)

away_team_1 = [
    ('img/scrd/Baby Bear (line up manager).jpg', 'Baby Bear (line up)'),
    ('img/scrd/Biasutti 4.jpg', '#4 Biasutti'),
    ('img/scrd/Cat Hook (bench).jpg', 'Cat Hook (bench)'),
    ('img/scrd/Crash Landers 108.jpg', '#108 Crash Landers'),
    ('img/scrd/Emma 8.jpg', '#8 Emma'),
    ('img/scrd/Jainareign 220.jpg', '#220 Jainareign'),
    ('img/scrd/Jekyll 303.jpg', '#303 Jekyll'),
    ('img/scrd/Killer Ree 64.jpg', '#64 Killer Ree'),
    ('img/scrd/Peters 9.jpg', '#9 Peters'),
    ('img/scrd/Queen of Scheme 69.jpg', '#69 Queen of Scheme'),
    ('img/scrd/S_care Bear 256.jpg', "#256 S'care Bear"),
    ('img/scrd/Snail 5050.jpg', '#5050 Snail'),
    ('img/scrd/Victory 37.jpg', '#37 Victory'),
]

away_team_1 = sorted(away_team_1, key=lambda x: x[1])


away_team_2 = [
    ('img/wcr/07–TheQuacken.jpg', '#07 The Quacken'),
    ('img/wcr/103–SuperMarion.jpg', '#103 Super Marion'),
    ('img/wcr/10–TitsAcid.jpg', '#10 Tits & Acid'),
    ('img/wcr/12–MeanMachine.jpg', '#12 Mean Machine'),
    ('img/wcr/15–HannahHardhendt.jpg', '#15 Hanna Hardhendt'),
    ('img/wcr/2-MadDonna.jpg', '#2 Mad Donna'),
    ('img/wcr/21–Assguardian.jpg', '#21 Assguardian'),
    ('img/wcr/242–PennyViolence.jpg', '#242 Penny Violence'),
    ('img/wcr/3-VirginiaWoof!.jpg', '#3 Virginia Woof!'),
    ('img/wcr/314–Blockpicker.jpg', '#314 Blockpicker'),
    ('img/wcr/48–BloodyLongstockings.jpg', '#48 Bloody Longstockings'),
    ('img/wcr/54-PattiShit.jpg', '#54 Patti Shit'),
    ('img/wcr/55-SickDagger.jpg', '#55 Sick Dagger'),
    ('img/wcr/59–LucidLucy.jpg', '#59 Lucid Lucy'),
    ('img/wcr/5–Sunny.jpg', '#5 Sunny'),
    ('img/wcr/8-HøssyGalore.jpg', '#8 Høssy Galore'),
    ('img/wcr/blOda.jpg', 'blOda'),
    ('img/wcr/MarieFurie.jpg', 'Marie Furie'),
    ('img/wcr/MushUMayhem.jpg', 'MushU Mayhem'),
    ('img/wcr/Nefertitties.jpg', 'Nefertitties'),
]


away_team_2 = sorted(away_team_2, key=lambda x: x[1])

home_team = [
    ('img/crd/switch.jpg', '#00 Switch'),
    ('img/crd/placeholder.png', '#111 Tumbleweed'),
    ('img/crd/frix.jpg', '#12 Frix'),
    ('img/crd/amar.jpg', '#2300 Amargeddon'),
    ('img/crd/candy.jpg', '#236 Poison Candy'),
    ('img/crd/placeholder.png', '#240 Zenobia'),
    ('img/crd/sibling.jpg', '#30 Sibling'),
    ('img/crd/speeda.jpg', '#42 Speeda'),
    ('img/crd/placeholder.png', '#54 Alex'),
    ('img/crd/olivia.jpg', '#5458 Olivia'),
    ('img/crd/mcdeath.jpg', '#4145 Lady MacDeath'),
    ('img/crd/rocket.jpg', '#321 Polly Rocket'),
    ('img/crd/xena.jpg', 'Xena (bench)'),
    ('img/crd/malika.png', 'Malika (line up)'),
]

home_team = sorted(home_team, key=lambda x: x[1])


@app.route('/')
def index():
    return render_template('index_single_alt.html')

@app.route('/away_1')
def away_1():
    return render_template('away1.html', away_team=away_team_1)

@app.route('/away_2')
def away_2():
    return render_template('away2.html', away_team=away_team_2)

@app.route('/home')
def home():
    return render_template('home.html', home_team=home_team)

@app.route('/rules')
def rules():
    return render_template('rules.html')

@app.route('/schedule')
def schedule():
    return render_template('schedule.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
