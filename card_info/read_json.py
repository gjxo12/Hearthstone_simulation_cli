from urllib.request import Request, urlopen
import json


URL_CARDS_JSON = "https://api.hearthstonejson.com/v1/83143/koKR/cards.json"

s = Request(URL_CARDS_JSON,headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(s).read().decode('utf-8')
webpage = json.loads(webpage)

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(webpage, f, ensure_ascii=False, indent=4)

print("-----------------------------------------------------")
