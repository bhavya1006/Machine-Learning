def menu():

    print("""Welcome Sir/Ma'am,\nWhat Would You Like To Do ?\n1) Verify username & password. \n2) Register as a new User and password.\n3) Change Password.\n4) Exit.""")
    return input("\n\nEnter Your Chooice: ")

dic_user_pwd = {'user':'password'}

while True:

    c = menu()
    
    user, password = '',''

    if c == '1':
        user = input("\n\nEnter username: ")
        if user in dic_user_pwd:
            print('#'*100)
            print("\n\nUser Exist!!")
            print('#'*100)
            password = input("\n\nEnter your Password: ")
            if password == dic_user_pwd[user]:
                print('#'*100)
                print("\n\nCorrect Password !!")
                print('#'*100)
                continue
            else:
                print('-'*100)
                print("\n\nIncorrect Password !!\n\n")
                print('-'*100)
                continue
        else:
            print('*'*100)
            print("\n\nUser doesn't exist !!\n\n")
            print('*'*100)
            continue

    elif c=='2':
        
        user = input("\n\nCreate new username: ")
        if user not in dic_user_pwd:
            password = input("\n\nCreate new password: ")
            dic_user_pwd[user] = password
            # print(dic_user_pwd)
        else:
            print('%'*100)
            print("\n\nUser already exist!!\n\n")
            print('%'*100)
            continue

    
    elif c=='3':

        user = input("\n\nEnter username: ")
        if user in dic_user_pwd:
            password = input("\n\nEnter Old Password")
            if password == dic_user_pwd[user]:
                password = input("\n\nEnter new password: ")
                dic_user_pwd[user] = password
            else:
                print('!'*100)
                print('\n\nIncorrect password')
                print('!'*100)
        else:
            print('^'*100)
            print("\n\nNo user found!!")
            print('^'*100)
    
    elif c == '4':
        print('\n\n')
        print("thank you!!"*10)
        break