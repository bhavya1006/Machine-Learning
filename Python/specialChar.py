# Write a program in python that checks whether an input string contains special characters or not.

print("Bhavya Madan\n0901AM221026")
def chk_spchr(st):
    
    spstr = "`!~@'\"#$%^&*()_-+={[]}:;<>,.?/|\\"

    for i in st:
        if i in spstr:
            print("Special Charater detected!!!!!")
            return True
    print("Special Charater NOT detected!!!!!!!!")
    return False

st0 = input("Enter string: ")
chk_spchr(st0)