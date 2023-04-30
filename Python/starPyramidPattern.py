# taking input to calculate required pyramid length
n = int(input("Enter number of rows in pyramid: "))

# Applying loop
for i in range(0,n):

    # For spacing
    for k in range(n-i,0,-1):  # 'n-i'  as row increases, required spaces decreases
        print(' ',end='')

    # For extra/odd stars
    for k in range(0,i):
        print('*',end='')

    # For remaining stars to complete the pyramid
    for j in range(0,i+1):
        print('*',end='')
    
    # For next line
    print()