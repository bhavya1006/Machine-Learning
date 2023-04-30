# defining function to checking odd number
def chkOdd(n):
    if n % 2 != 0:
        return True
    return False


# Ranging the function to print odd numbers in it
l = int(input("Enter lower limit: "))
u = int(input("Enter lower upper: "))

for i in range(l, u+1):
    if chkOdd(i):
        print(i, end=' ')