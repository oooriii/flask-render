"""
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

##########
# https://realpython.com/python-web-applications/
##########

#from bs4 import BeautifulSoup

from flask import Flask, request


#import re
import requests
import json

URI_ODDS = 'https://www.ninjabet.es/get_data_sp.php'
URI_EVENTS = ''

books = {
 '888': '1',
 'bet365': '2',
 'betclic': '3',
 'betfair sportbook': '4',
 'betflag': '5',
 'better': '6',
 'bwin': '7',
 'eurobet': '9',
 'gazzabet': '10',
 'gioco digitale': '11',
 'interwetten': '12',
 'intralot': '13',
 'netbet': '14',
 'tornadobet': '15',
 'osnai': '16',
 'totosi': '18',
 'unibet': '19',
 'WilliamHill': '20',
 'sportYes': '21',
 'skybet': '22',
 'betflag exchange': '23',
 'stanleybet': '24',
 'paddypower': '25',
 'betuniq': '26',
 'betaland': '27',
 'goldbet': '28',
 'pokerstars': '29',
 'OuiGioco': '30',
 'domusbet.it': '32',
 'Pinterbet': '33',
 'ometiendo.it': '34',
 'LeoVegas': '35',
 'chancebet.it': '36',
 'Circus': '37',
 'Codere': '39',
 'GoldenPark': '40',
 'ijuego': '41',
 'jokerbet.es': '42',
 'interwetten.com': '43',
 'luckia': '44',
 'marcaapuestas': '45',
 'paf': '46',
 'paston.es': '47',
 'sportium': '48',
 'suertia.es': '49',
 'titanbet.es': '50',
 'Vivelasuerte.es': '51',
 'Wanabet': '52',
 'betfair sportbook 2': '53',
 'star vegas': '54',
 'marathon bet': '55',
 'betsson': '56',
 'retabet.es': '57',
 'betway': '59',
 'Gran Casino Madrid': '61',
 'Casino Barcelona': '62',
 'MondoBets': '63',
 'Kirolbet': '64',
 'Versus': '65',
 'Bethard': '66',
 'Sisal': '67',
 '1XBet': '68',
 'Winamax': '69',
 'BetFred': '70',
 'LeoVegas': '71',
 'Mr Green': '72',
 'En Racha': '73',
 'Zebet': '74',
 '777': '75',
 'Juegging': '76',
 '777 2': '77',
 'betway.com': '81',
}
bet_types = {
    'normal': 'normal',
    'freebet': 'ag',
    'reembolso': 'snr',

}

headers = {
    "authority": "www.ninjabet.es",
    "accept": "*/*",
    "accept-language": "ca-ES,ca;q=0.9",
    "cache-control": "no-cache",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Accept": "*/*",
    "origin": "https://www.ninjabet.es",
    "pragma": "no-cache",
    "referer": "https://www.ninjabet.es/oddsmatcher-sportium-amigos-mb",
    "x-requested-with": "XMLHttpRequest",
}

payload_data = {
    "combinazioni":"2",
    "action":"get_odds_data",
    "uid":"cfcd208495d565ef66e7dff9f98764da",
    "refund":"100",
    "back_stake":"100",
    "filterbookies":"",
    "bookies":"7",
    "rating-from":"",
    "rating-to":"",
    "odds-from":"",
    "odds-to":"",
    "min-liquidity":"",
    "sort-column":"4",
    "sort-direction":"desc",
    "offset":"0",
    "date-from":"",
    "date-to":"",
    "exchange":"all",
    "exchanges":"all",
    "sport":"all",
    "betfair-commission":"2",
    "matchbook-commission":"4",
    "bet-type":"",
    "rating-type":"ag",
    "roll-real-money":"100",
    "roll-bonus":"100",
    "roll-remaining":"100",
    "roll-rating":"95",
    "tz":"-120",
#    "name[]":"e487647603,e577560659,e444269169,e487706590,e693502969,e487669419,e629813592,e487652253,e579464833,e487637023,e487726950,e231782951,e487671685,e639315536,e487652411,e605413047,e487637448,e487734912,e386797675,e487678198,e666121908,e487656552,e605421260,e487638619,e522639871,e439503974,e487684532,e670541270,e487658125,e605425785,e487642991,e560025372,e439592487,e487695052,e675145184,e487665459,e605428496",
}

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def index():
    with open('index.html', 'r') as file:
        data = file.read()
    return data

#@app.route("/js/main.js", methods = ['GET'])
@app.route("/main.js", methods = ['GET'])
def get_js():
#    with open('js/main.js', 'r') as file:
    with open('main.js', 'r') as file:
        data = file.read()
    return data

@app.route("/get_odds/<name>", methods = ['POST', 'GET'])
def get_get_odds(name):
    payload = payload_data
    if request.method == 'POST':
        data = request.json
        offset = data['offset']
        payload['offset'] = offset

        bet_type = bet_types[data['bet_type']]
        payload['rating-type'] = bet_type



    return get_odds(name, payload)


def get_odds(name, payload):
        #payload = payload_data
        bookmark = 0
        if(name is not None):
            bookmark = books[name]
            payload['bookies'] = bookmark


        url = URI_ODDS
        #response = requests.post(url)
        #response = requests.post(url, data=json.dumps(payload), headers=headers)
        response = requests.post(url, data=payload, headers=headers)
        if(response.status_code == 200):
            #print("Connexió establerta")
            odds = response.json()
            #print(json.dumps(odds, indent=4))
            #return json.dumps(odds, indent=4)
            return json.dumps(odds)


"""
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
    app.run()
    #from waitress import serve
    #serve(app, host="0.0.0.0", port=8080)
    #serve(app)
"""


