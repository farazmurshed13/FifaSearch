import requests
from bs4 import BeautifulSoup as bs
import json


def get_player_data():
    # request page and set up parser
    url = 'https://sofifa.com/players?type=all&ptl=90'
    r = requests.get(url)
    soup = bs(r.content, 'html.parser')
    rows = soup.select('tbody tr')

    # get player stats within page
    data = []
    c = 0
    for row in rows:
        d = dict()
        d['name'] = row.select_one('.col-name .tooltip')['data-tooltip'].strip()
        d['age'] = row.select_one('.col-ae').text.strip()
        d['ovr'] = row.select_one('.col-oa').text.strip()
        d['pot'] = row.select_one('.col-pt').text.strip()
        d['team'] = row.select('.col-name')[1].text.strip()
        d['team'] = d['team'].split('\n')[0]
        d['end'] = row.select_one('.col-name .sub').text.strip()
        d['end'] = d['end'].split(' ')[-1]
        data.append(d)

    # store data in json file
    with open('player_data.json', 'w') as f:
        json.dump(data, f, indent=2)

    return 'player_data.json'
