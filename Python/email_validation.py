from special_char_detection import chk_spchr

while True:

    flagnu,flaglo,flagup = 0,0,0

    email_str = input("Enter your email: ")

    if email_str == 'q':
        break

    if len(email_str) <= 9:
        print("Very Short EMail!!")
        continue

    if chk_spchr(email_str):
        pass
    else:
        print("No Special Charter FOund!!")

    for i in email_str:
        if i.isupper():
            flagup = 1
        if i.islower():
            flaglo = 1
        if i.isnumeric():
            flagnu = 1
    
    if flagup != 1:
        print("No UpperCase Found !!")
        continue
    if flaglo != 1:
        print("No LowerCase Found !!")
        continue
    if flagnu != 1:
        print("No Numeric Found !!")
        continue

    print("Valid Email Address!!")