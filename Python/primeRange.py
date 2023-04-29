# Taking prime function from a python file
from prime import *

# Taking range from user
l = int(input("Enter Lower Limit: "))
u = int(input("Enter Upper Limit: "))

# Checking and displaying prime of range lower to upper limits
for i in range(l,u+1):
    if chkPrime(i):
        print(i,end=' ')