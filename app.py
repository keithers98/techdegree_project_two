import constants
import copy

players = copy.deepcopy(constants.PLAYERS) #every shallow copy will change all the existing dictionaries
team_names = constants.TEAMS
teams = [{constants.TEAMS[0]:[]}, {constants.TEAMS[1]:[]}, {constants.TEAMS[2]:[]}]

def clean_data(player_stats):
    noobs = []
    not_noobs = []
    for player in player_stats:
        if player['experience'] == 'YES':
            not_noobs.append(player['name'])
            player['experience'] = True
        elif player['experience'] == 'NO':
            noobs.append(player['name'])
            player['experience'] = False

        player['height'] = int(player['height'][0:2])
    return player_stats, noobs, not_noobs


def balance_teams(teams, noobs, not_noobs):

    def players_taken(noobs, not_noobs):
        del(noobs[0:3])
        del(not_noobs[0:3])
        return noobs, not_noobs

    # team one comp
    noob_balance = int((len(player_stats) / len(teams)) / 2)
    teams[0][constants.TEAMS[0]].append(noobs[0:noob_balance])
    teams[0][constants.TEAMS[0]].append(not_noobs[0:noob_balance])
    noobs, not_noobs = players_taken(noobs, not_noobs)

    #team two comp
    teams[1][constants.TEAMS[1]].append(noobs[0:noob_balance])
    teams[1][constants.TEAMS[1]].append(not_noobs[0:noob_balance])
    noobs, not_noobs = players_taken(noobs, not_noobs)

    #team three comp
    teams[2][constants.TEAMS[2]].append(noobs[0:noob_balance])
    teams[2][constants.TEAMS[2]].append(not_noobs[0:noob_balance])
    noobs, not_noobs = players_taken(noobs, not_noobs)

    return teams[0]['Panthers'], teams[1]['Bandits'], teams[2]['Warriors']

def display_stats(team1, team2, team3, team_names, player_stats):
    main_menu = ("""
    Basketball Team Stats Tool \n
         ----MENU---- \n""")

    choices = ("""\n     Here are your choices:
    1) Display Team Stats
    2) Quit \n
    """)
    print(main_menu, choices)
    menu_option = input("\nEnter an option >>>   ")


    def avg_height(player_stats, team):
        avg_height = 0
        team_length = 0
        for listi in team[0:2]:
            for player in player_stats:
                for name in listi:
                    if player['name'] == name:
                        avg_height = avg_height + player['height']
                        team_length += 1
        avg_height = round(avg_height / team_length, 2)
        return avg_height



    def ask_again(main_menu):
        menu_option = input("\n{}\nWould you like to (C)heck out another team or (Q)uit? >>   ".format(main_menu))
        try:
            if menu_option.lower() == 'c':
                menu_option = '1'
            elif menu_option.lower() == 'q':
                menu_option = '2'
            elif menu_option != 'c' or 'q':
                raise ValueError("\n\nWhoops, enter 'c' to choose another team or 'q' to quit.\n")
        except ValueError as err:
            print(err)
            menu_option = ask_again(main_menu)
        return menu_option


    def print_stats(team, team_name):
        print('\nTeam Name: {}\n -------------------'.format(team_name))
        print('The average height of the team is: {} inches.'.format(avg_height(player_stats, team)))
        print('Experienced Players: {}\nNon-experienced Players: {}'.format(len(team[0]),len(team[1])))
        print('Team Members:\n {}, {}, {}, {}, {}, {}'.format(team[0][0], team[0][1], team[0][2], team[1][0], team[1][1], team[1][2]))


    while menu_option != '2':
        print('''

        1)Panthers \n
        2)Bandits \n
        3)Warriors\n\n''')
        team_choice = input('Enter an option >>>   ')
        try:
            if int(team_choice) > 3:
                print('Oops, there are only three teams. Please try again.')
        except ValueError as err:
                    print('Oops, please enter a valid number. (1, 2, 3)')
                    continue
        if int(team_choice) < 0:
            print("Oops, that wasn't a valid choice, Please try again.")

        elif team_choice == '1':
            print_stats(team1, team_names[0])
            menu_option = ask_again(main_menu)

        elif team_choice == '2':
            print_stats(team2, team_names[1])
            menu_option = ask_again(main_menu)

        elif team_choice == '3':
            print_stats(team3, team_names[2])
            menu_option = ask_again(main_menu)


if __name__ == '__main__':
    player_stats, noobs, not_noobs = clean_data(players)
    panthers, bandits, warriors = balance_teams(teams, noobs, not_noobs)
    display_stats(panthers, bandits, warriors, team_names, player_stats)
