# Taking a number as input and 'n' to perform changes
num = int(input("Enter a number: "))
n = num

# Defining sum as 0 initially
sum = 0

# Applying loop to sum values up
while n/10!=0:
    temp = n%10
    sum += temp
    n //= 10

# Showing result
print("Sum of digits of the number",num,"is: ",sum)