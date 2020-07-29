import soFifaScraper as sFS
import json as js


# perform search
def search(key, team=None):
    # store search results
    bank = sFS.get_player_data(key)
    with open(bank, 'r') as f:
        data = js.load(f)

    # no results found
    if len(data) == 0:
        print("No results found")
    else:
        # find and print results, if any found
        if len(data) > 2:
            print(str(len(data)) + ' result(s) found\n')
        else:
            c = 0
            for player in data:
                # option to narrow by team if specified
                if team is None:
                    rat = player['ovr'] + '/' + player['pot']
                    exp = ' (exp: ' + player['end'] + ')'
                    print(player['name'] + ', ' + player['age'] + ', ' + rat + ', ' + player['team'] + exp + '\n')
                    c += 1
                else:
                    if team in player['team']:
                        rat = player['ovr'] + '/' + player['pot']
                        exp = ' (exp: ' + player['end'] + ')'
                        print(player['name'] + ', ' + player['age'] + ', ' + rat + ', ' + player['team'] + exp)
                        c += 1


# prompt user
def main():
    while True:
        # prompt user to search for players
        keyword = input("Search player name: \n").lower()
        # end prompter
        if keyword == "qq":
            break
        else:
            search(keyword)


if __name__ == "__main__":
    main()




