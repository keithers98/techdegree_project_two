import constants
import copy

players = copy.deepcopy(constants.PLAYERS) #every shallow copy will change all the existing dictionaries

teams = [{constants.TEAMS[0]:[]}, {constants.TEAMS[1]:[]}, {constants.TEAMS[2]:[]}]

def clean_data(player_stats):
    for player in player_stats:
        if player['experience'] == 'YES':
            #player_stats[player_stats.index(player)]['experience'] = True #same result as line above but way too complicated!
            player['experience'] = True
        elif player['experience'] == 'NO':
            #player_stats[player_stats.index(player)]['experience'] = False #same result as line above but way too complicated!
            player['experience'] = False

        player['height'] = int(player['height'][0:2])
    return player_stats

def balance_teams(player_stats, teams):
    players_per_team = int(len(player_stats) / len(teams))
    teams[0][constants.TEAMS[0]].append(player_stats[0:players_per_team])
    teams[1][constants.TEAMS[1]].append(player_stats[len(teams[0][constants.TEAMS[0]][0]):(players_per_team * 2)])
    teams[2][constants.TEAMS[2]].append(player_stats[len(teams[1][constants.TEAMS[1]][0]) * 2:(players_per_team * 3)])


#def display_stats(yes_no):



if __name__ == '__main__':
    print("""
    Basketball Team Stats Tool \n
         ----MENU---- \n
    Here are your choices:
    1) Display Team Stats
    2) Quit \n
    """)

    menu_option = input("Enter an option >>>   ")
    clean_data(players)
    balance_teams(players, teams)
