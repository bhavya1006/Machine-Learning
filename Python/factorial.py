def fact(n):
    if n<=1:
        return 1             # returning (1) at end
    return n*fact(n-1)       # returning (n) and value as per recurssion for (n-1)

print("Factorial is: ",fact(int(input("Enter number for factorial: "))))  # showing result