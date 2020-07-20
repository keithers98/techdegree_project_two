import constants

print("""
Basketball Team Stats Tool \n
----MENU---- \n
Here are your choices:
1) Display Team Stats
2) Quit \n
""")

menu_option = input("Enter an option >>>   ")
players_copy = constants.PLAYERS[:] #this is known as slicing sytax for copying


def clean_data(module):
    for dicti in players_copy:
        if dicti['experience'] == 'YES':
            players_copy[players_copy.index(dicti)]['experience'] = True
            #dict['experience'] = True
        elif dicti['experience'] == 'NO':
            players_copy[players_copy.index(dicti)]['experience'] = False
            #dict['experience'] = False

        dicti['height'] = int(dicti['height'][0:2])
    return players_copy

if __name__ == '__main__':
    clean_data(players_copy)
