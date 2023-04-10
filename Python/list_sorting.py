# take no.s from user and place them in 3 list representing even, oddd and prime

def chk_prime(n):

    if n in [0,1]:
        return False
    if n == 2:
        return True
    
    flag = 1
    for i in range(2,n):
        if n%i == 0:
            flag=0

    if flag==1:
        return True
    else:
        return False
    
list_odd = []
list_even = []
list_prime = []
cmd = 'n'
while(cmd=='n'):
    inp = int(input("Enter element: "))
    if inp%2==0:
        list_even.append(inp)
    else:
        list_odd.append(inp)
    
    if chk_prime(inp):
        list_prime.append(inp)

    cmd = input("Want to quit yes(y) or no(n): ")

print(list_even)
print(list_odd)
print(list_prime)



