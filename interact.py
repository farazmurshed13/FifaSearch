import soFifaScraper as sFS
import json as js


# display info for all players in given data
def display_all(results):
    # no results found (reduced to empty dict)
    if len(results) == 0:
        print("No results found")
    # only print # of results if more than 2 found
    elif len(results) > 2:
        print(str(len(results)) + ' result(s) found\n')
    # otherwise, print player info
    else:
        for player in results:
            rat = player['ovr'] + '/' + player['pot']
            exp = ' (exp: ' + player['end'] + ')'
            print(player['name'] + ', ' + player['age'] + ', ' + rat + ', ' + player['team'] + exp + '\n')


# perform search
def search(key, team=None):
    # store search results
    bank = sFS.get_player_data(key)
    with open(bank, 'r') as f:
        data = js.load(f)

    # no results found
    if len(data) == 0:
        print("No results found")
    # option to narrow results by team if specified, and then print player info
    elif team is not None:
        reduced = []
        # narrow scope
        for player in data:
            if team in player['team_tag']:
                reduced.append(player)
        display_all(reduced)
    # otherwise, print player info for all in data
    else:
        display_all(data)


# prompt user
def main():
    while True:
        # prompt user to search for players
        entry = input("Search: \n").lower().split(', ')
        keyword = entry[0]

        # end prompter
        if keyword == "qq":
            break
        # allow for team specification as well
        elif len(entry) > 1:
            team = entry[1]
            search(keyword, team)
        else:
            search(keyword)


if __name__ == "__main__":
    main()




