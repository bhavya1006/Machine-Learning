# defining a function to check spy number or not for first 10000 number check and total count

def chkspy(n):
    l = [int(x) for x in str(n)]
    sumN,prodN = sum(l),1
    for i in l:
        prodN *= i
    if prodN == sumN:
        return True
    return False

c=0
for n in range(10000):
    if chkspy(n):
        print(n,"It is a Spy Number.")
        c+=1
    else:
        print(n,"It is not a Spy Number.")
print("Total Spy number is",c)