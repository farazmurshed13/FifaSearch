import soFifaScraper as sFS
import json as js

# get requested player data
bank = sFS.get_player_data()
with open(bank, 'r') as f:
    data = js.load(f)

# prompt user to search for players
while True:
    key = input("Search player name: \n").lower()
    # end prompter
    if key == "q":
        break

    c = 0
    # find and print results, if any found
    for player in data:
        if key in player['tag'].lower() or key in player['tag2'].lower():
            rat = player['ovr'] + '/' + player['pot']
            exp = ' (exp: ' + player['end'] + ')'
            print(player['name'] + ', ' + player['age'] + ', ' + rat + ', ' + player['team'] + exp)
            c += 1

    if c == 0:
        print("No results found")





