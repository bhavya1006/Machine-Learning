print("Arithmetic Operators:")
a = 10
b = 3

print("Addition:", a + b)       
print("Subtraction:", a - b)    
print("Multiplication:", a * b) 
print("Division:", a / b)       
print("Floor Division:", a // b)  
print("Modulo:", a % b)         
print("Exponentiation:", a ** b)

print("\nAssignment Operators:")
x = 5
print("x =", x)

x += 3  
print("After x += 3, x =", x)

x -= 2   
print("After x -= 2, x =", x)

x *= 4  
print("After x *= 4, x =", x)

x /= 2  
print("After x /= 2, x =", x)

x //= 3  
print("After x //= 3, x =", x)

x %= 2   
print("After x %= 2, x =", x)

x **= 5  
print("After x **= 5, x =", x)

print("\nComparison Operators:")
a = 5
b = 3
print("a == b:", a == b) 
print("a != b:", a != b)   
print("a > b:", a > b)     
print("a < b:", a < b)   
print("a >= b:", a >= b)   
print("a <= b:", a <= b) 
print("\nLogical Operators:")
x = True
y = False
print("x and y:", x and y)   
print("x or y:", x or y)    
print("not x:", not x)       
print("\nBitwise Operators:")
a = 5   
b = 3   
print("a & b:", a & b)   
print("a | b:", a | b)   
print("a ^ b:", a ^ b)   
print("~a:", ~a)         
print("a << 1:", a << 1) 
print("a >> 1:", a >> 1) 
print("\nPrecedence of Operators:")
print("Highest Precedence: ** (Exponentiation)\n\
Next: *, /, //, %\n\
Next: +, -\n\
Next: <<, >>\n\
Next: &\n\
Next: ^\n\
Next: |\n\
Next: ==, !=, >, <, >=, <=\n\
Next: not\n\
Lowest Precedence: and, or")
