# swapping without temp variable

var1 = 3
var2 = 4
print("Before Swapping values -\n")
print("Value 1:",var1,"\nValue 2:",var2)

var1 += var2
var2 = var1 - var2
var1 = var1 - var2

print("\nAfter Swapping values -\n")
print("Value 1:",var1,"\nValue 2:",var2)