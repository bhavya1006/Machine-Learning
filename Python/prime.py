# defining a function to check prime
def chkPrime(n):

    # if number is 0 or 1
    if n==0 or n==1:
        return False
    
    # if number is 2
    elif n==2:
        return True
    
    # checking prime for other digits
    else:
        for i in range(2,n):
            if n%i == 0:
                return False
        return True

# Showing results from 0 to 200
for j in range(0,200):
    if chkPrime(j):
        print(j,end=' ')