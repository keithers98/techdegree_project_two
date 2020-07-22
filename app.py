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
    return teams[0]['Panthers'], teams[1]['Bandits'], teams[2]['Warriors']

def display_stats(team1, team2, team3):
    print("""
    Basketball Team Stats Tool \n
         ----MENU---- \n
    Here are your choices:
    1) Display Team Stats
    2) Quit \n
    """)

    menu_option = input("Enter an option >>>   ")

    while menu_option != 0:
        print('''

        1)Panthers \n
        2)Bandits \n
        3)Warriors\n\n''')
        team_choice = input('Enter an option>>>   ')
        if team_choice == '1':
            print(team1)
        elif team_choice == '2':
            print(team2)
        else:
            print(team3)



if __name__ == '__main__':
    player_stats = clean_data(players)
    panthers, bandits, warriors = balance_teams(players, teams)
    display_stats(panthers, bandits, warriors)
