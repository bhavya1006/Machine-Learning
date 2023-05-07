# creating a function whoch take arguments, by default value =4
def abcPatternAsc(n=4):
    # ranging for number of rows
    for i in range(0,n):
        # for decreasing space
        for j in range(n-i):
            print(" ",end='')
        # for alphabet in order format
        for k in range(i+1):
            print(chr(65+k),end=' ')
        print()

abcPatternAsc(int(input("Enter no of rows : ")))
