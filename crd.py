import os

from flask import Flask, render_template

app = Flask(__name__)

away_team_1 = [
    ('img/msf/108_princess_evi.jpg', '#108 Princess Evi'),
    ('img/msf/161_leilah_zerteilah.jpg', '#161 Leilah Zerteilah'),
    ('img/msf/27_electric_sheep.jpg', '#27 Electric Sheep'),
    ('img/msf/28_careless_ness.jpg', '#28 Careless Ness'),
    ('img/msf/3_motorännah.jpg', '#3 Motorännah'),
    ('img/msf/42_twisted_demon.jpg', '#42 Twisted Demon'),
    ('img/msf/635_peetroleum_on_fire.jpg', '#635 Peetroleum On Fire'),
    ('img/msf/667_jane_rambo.jpg', '#667 Jane Rambo'),
    ('img/msf/69_filthy_fay.jpg', '#69 Filthy Fay'),
    ('img/msf/707_lady_klopperfield.jpg', '#707 Lady Klopperfield'),
    ('img/msf/7125_mac_gayver.png', '#7125 Mac Gayver'),
    ('img/msf/713_hooks.jpg', '#713 Hooks'),
    ('img/msf/802_futura_fearless.jpg', '#802 Futura Fearless'),
    ('img/msf/heep_of_trouble.jpg', '#55 Heep of Trouble'),
]

away_team_1 = sorted(away_team_1, key=lambda x: x[1])

away_team_2 = [
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


away_team_2 = sorted(away_team_2, key=lambda x: x[1])

#home_team = [
#    ('img/crd_a/switch_00.jpg', '#00 Switch'),
#    ('img/crd_a/tumbleweed_111.jpg', '#111 Tumbleweed'),
#    ('img/crd_a/frix_12.jpg', '#12 Frix'),
#    ('img/crd_a/calm_storm_14.jpg', '#14 Calm Storm'),
#    ('img/crd_a/evig_hvad_1984.jpg', '#1984 Evig Hvad'),
#    ('img/crd_a/lix_2.jpg', '#2 Lix'),
#    ('img/crd_a/amargeddon_2300.jpg', '#2300 Amargeddon'),
#    ('img/crd_a/poison_candy_236.jpg', '#236 Poison Candy'),
#    ('img/crd_a/zenobia_240.jpg', '#240 Zenobia'),
#    ('img/crd_a/sibling_30.jpg', '#30 Sibling'),
#    ('img/crd_a/speeda_42.jpg', '#42 Speeda'),
#    ('img/crd_a/alex_54.jpg', '#54 Alex'),
#    ('img/crd_a/olivia_5458.jpg', '#5458 Olivia'),
#    ('img/crd_a/cosmonaut_63.jpg', '#63 Cosmonaut'),
#    ('img/crd_a/tango_maureen_855.jpg', '#855 Tango Maureen'),
#]

home_team = [
    ('img/crd_b/00_switch.jpg', '#00 Switch'),
    ('img/crd_b/07_annabiotics.jpg', '#07 Annabiotics'),
    ('img/crd_b/1337_mc_rowhammer.jpg', '#1337 MC Rowhammer'),
    ('img/crd_b/19_brutalis.jpg', '#19 Brutalis'),
    ('img/crd_b/236_poison_candy.jpg', '#236 Poison Candy'),
    ('img/crd_b/256_oxytoxin.jpg', '#256 Oxytoxin'),
    ('img/crd_b/30_sibling.jpg', '#30 Sibling'),
    ('img/crd_b/321_polly_rocket.jpg', '#321 Polly Rocket'),
    ('img/crd_b/390_falke.jpg', '#390 Falke'),
    ('img/crd_b/4_ea.jpg', '#4 Ea'),
    ('img/crd_b/5458_olivia.jpg', '#5458 Olivia'),
    ('img/crd_b/69_bethamphetamine.jpg', '#69 Bethamphetamine'),
    ('img/crd_b/74_møjn.jpg', '#74 Møjn'),
    ('img/crd_b/855_tango_maureen.jpg', '#855 Tango Maureen'),
    ('img/crd_b/89_malika.jpg', '#89 Malika'),
    ('img/crd_b/95_xena.jpg', '#95 Xena'),
    ('img/crd_a/tumbleweed_111.jpg', '#111 Tumbleweed'),
]


@app.route('/')
def index():
    return render_template('index_triple_header.html')

@app.route('/away_1')
def away_1():
    return render_template('away1.html', away_team=away_team_1)

@app.route('/away_2')
def away_2():
    return render_template('away.html', away_team=away_team_2)

@app.route('/home')
def home():
    return render_template('home.html', home_team=home_team)

@app.route('/rules')
def rules():
    return render_template('rules.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
