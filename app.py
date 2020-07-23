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
        for name in team:
            for player in player_stats:
                if name in player:
                    avg_height = avg_height + int(player['height'])
        return avg_height



    def ask_again(main_menu):
        menu_option = input("\n{}\nWould you like to (C)ontinue or (Q)uit? >>   ".format(main_menu))
        try:
            if menu_option == 'c':
                menu_option = '1'
            elif menu_option == 'q':
                menu_option = '2'
            elif menu_option != 'c' or 'q':
                raise ValueError("\n\nWhoops, enter 'c' to continue or 'q' to quit.\n")
        except ValueError as err:
            print(err)
            menu_option = ask_again(main_menu)
        return menu_option


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
            print(avg_height(player_stats, team1))
            print('\nTeam Name: {}\n -------------------'.format(team_names[0]))
            print('Experienced Players: {}\nNon-experienced Players: {}'.format(len(team1[0]),len(team1[1])))
            print('Team Members:\n {}, {}, {}, {}, {}, {}'.format(team1[0][0], team1[0][1], team1[0][2], team1[1][0], team1[1][1], team1[1][2]))
            menu_option = ask_again(main_menu)

        elif team_choice == '2':
            print('\nTeam Name: {}\n -------------------'.format(team_names[1]))
            print('Experienced Players: {}\nNon-experienced Players: {}'.format(len(team2[1]), len(team2[0])))
            print('Team Members:\n {}, {}, {}, {}, {}, {}'.format(team2[0][0], team2[0][1], team2[0][2], team2[1][0], team2[1][1], team2[1][2]))
            menu_option = ask_again(main_menu)

        elif team_choice == '3':
            print('\nTeam Name: {}\n -------------------'.format(team_names[2]))
            print('Experienced Players: {}\nNon-experienced Players: {}'.format(len(team3[0]), len(team3[1])))
            print('Team Members:\n {}, {}, {}, {}, {}, {}'.format(team3[0][0], team3[0][1], team3[0][2], team3[1][0], team3[1][1], team3[1][2]))
            menu_option = ask_again(main_menu)


if __name__ == '__main__':
    player_stats, noobs, not_noobs = clean_data(players)
    panthers, bandits, warriors = balance_teams(teams, noobs, not_noobs)
    display_stats(panthers, bandits, warriors, team_names, player_stats)
