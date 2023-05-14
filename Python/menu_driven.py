# menu-driven is a set of display format to take organised input from user
def menu(list_of_options):
    print("Menu: ")
    for x, i in enumerate(list_of_options):
        print(f'{x+1}) {i}')
    choice = int(input("Enter your choice: "))
    return choice

li = ['To play chess','To play Tic Tac toe','To play Valorant']
print(menu(li))