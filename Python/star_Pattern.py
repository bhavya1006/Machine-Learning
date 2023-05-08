#creating a fuction to have star loop code
def starOddPatttern(n=5):
    for i in range(n):
        for k in range(n-i):
            print(' ',end='')
        for j in range(i):
            print('*',end='')
        for h in range(i+1):
            print('*',end='')
        print()
starOddPatttern(int(input("Enter a number: ")))