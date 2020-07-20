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
    for dict in players_copy:
        if dict['experience'] == 'YES':
            players_copy[dict.index()['experience']] = True
            #dict['experience'] = True
        elif dict['experience'] == 'NO':
            players_copy[dict.index()['expereince']] = False
            #dict['experience'] = False

        dict['height'] = int(dict['height'][0:2])
    return players_copy

if __name__ == '__main__':       
    clean_data(players_copy)