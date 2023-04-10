# check of an input string contain special symbols or not and hence display the detected the special symbol


def chk_spchr(st):
    
    spstr = "`!~@'\"#$%^&*()_-+={[]}:;<>,.?/|\\"

    for i in st:
        if i in spstr:
            print("Special Charater detected!!!!!")
            return True
    
    print("Special Charater NOT detected!!!!!!!!")

st0 = input("ENter string: ")
chk_spchr(st0)