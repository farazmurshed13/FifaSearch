import requests
from bs4 import BeautifulSoup as bs
import json
import unidecode


# return json with SoFifa player data for specified search key
# results limited to first page of results on SoFifa
def get_player_data(key):
    # request page and set up parser
    url = 'https://sofifa.com/players?keyword=' + key
    r = requests.get(url)
    soup = bs(r.content, 'html.parser')
    rows = soup.select('tbody tr')

    # get player stats within page
    data = []
    for row in rows:
        d = dict()
        # store player name
        d['name'] = row.select_one('.col-name .tooltip')['data-tooltip'].strip()

        # store age, overall rating, potential rating
        d['age'] = row.select_one('.col-ae').text.strip()
        d['ovr'] = row.select_one('.col-oa').text.strip()
        d['pot'] = row.select_one('.col-pt').text.strip()

        # store team and contract end date
        d['team'] = row.select('.col-name')[1].text.strip()
        d['team'] = d['team'].split('\n')[0]
        d['team_tag'] = d['team'].lower()
        d['team_tag'] = unidecode.unidecode(d['team_tag'])
        d['end'] = row.select_one('.col-name .sub').text.strip()
        d['end'] = d['end'].split(' ')[-1]

        data.append(d)

    # store data in json file
    with open('player_data.json', 'w') as f:
        json.dump(data, f, indent=2)

    return 'player_data.json'
