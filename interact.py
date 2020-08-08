import scrape_fifa as sf
import json as js
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse


# display info for all players in given data
def display_all(results):
    # no results found (reduced to empty dict)
    if len(results) == 0:
        return "No results found"
    # only print # of results if more than 2 found
    elif len(results) > 1:
        msg = str(len(results)) + ' result(s) found\n'
        return msg
    # otherwise, print player info
    # appendage: "Sent from your Twilio trial account - " (38 chars)
    else:
        for player in results:
            rat = player['ovr'] + '/' + player['pot']
            exp = ' (exp: ' + player['end'] + ')'
            msg = player['name'] + ', ' + player['age'] + ', ' + rat + ', ' + player['team'] + exp + '\n'
            return msg


# perform search
def search(key, team=None):
    # store search results
    bank = sf.get_player_data(key)
    with open(bank, 'r') as f:
        data = js.load(f)

    # no results found
    if len(data) == 0:
        return "No results found"
    # option to narrow results by team if specified, and then print player info
    elif team is not None:
        reduced = []
        # narrow scope
        for player in data:
            if team in player['team_tag']:
                reduced.append(player)
        return display_all(reduced)
    # otherwise, print player info for all in data
    else:
        return display_all(data)


app = Flask(__name__)


# handle incoming sms
@app.route("/sms", methods=['GET', 'POST'])
def handle_sms():
    # Get the message the user sent to Twilio number
    body = request.values.get('Body', None)

    # reconfigure message into player name (keyword) and team name
    # init search
    entry = body.lower().split(', ')
    keyword = entry[0]
    if len(entry) > 1:
        team = entry[1]
        res = search(keyword, team)
    else:
        res = search(keyword)

    # TwiML response
    resp = MessagingResponse()
    resp.message(res)

    return str(resp)


if __name__ == "__main__":
    app.run()


