import requests
from urllib.parse import quote_plus
from pprint import pprint



def getJoke():
    response = requests.get('https://08ad1pao69.execute-api.us-east-1.amazonaws.com/dev/random_joke')
    return response.json()


def getSpell(spell):
    print (quote_plus(spell))
    response = requests.get("http://dnd5eapi.co/api/spells/?name="+quote_plus(spell))
    r = response.json()
    if (r['count']==0):
        return "sorry I couldn't find that spell"
    print(r['results'][0]['url'])
    response = requests.get(r['results'][0]['url'])
    r = response.json()
    pprint(r)
    print (r['casting_time'])
    return r






