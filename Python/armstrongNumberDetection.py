# creating a function to check
# Armstrong number;
# A number which is equal to addition of all the digit of number raised to length of the number

def chkarmstrg(n):

    # to store the property of armstrong number
    armN = 0 

    # taking each element as string
    for x in str(n):    

        # the given function below itself convert digit to int and raised to power of it's length
        # and adds up to previous as well 
        armN += int(x)**(len(str(n)))

    # condition checking to armstrong to the number itself
    if armN == n:
        print("Armstrong Number")
        return True
    
    print("Not Armstrong Number")
    return False

# testing
print("The boolean value is,",chkarmstrg(int(input("Enter a number(for, armstronmg number): "))))