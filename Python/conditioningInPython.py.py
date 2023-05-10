# Hello friends, in this file you will learn about the conditioning in python
# the term conditioning can be for checking variable with any equation, comparison 
# and getting result in boolean expression which is checker by keywords 'if' or 'elif'
# and like other way 'else' for last exceptional case.


  ####SYNTAX####
# if (condition):
#     {code}
# elif (condition):                   'elif': Is use in nested conditions,
#     {code}                                  and can be more than one
# else:
#     {code}


# Example 1: simple condition
x = 8
if x == 8:
    print('variable is equal to 8')
else:
    print('variable is not equal to 8')


# Example 2.1: nested condition
a = 8
b = 3
c = 9
if a>b:
    if a>c:
        print("Variable 'a' is greatest.")
    else:
        print("Variable 'c' is greatest.")
else:
    if b>c:
        print("Variable 'b' is greatest.")
    else:
        print("Variable 'c' is greatest.")


# Or, Example 2.2: 
a = b
c = b
if a>b and a>c:
    print("Variable 'a' is greatest.")
elif b>a and b>c:
    print("Variable 'b' is greatest.")
elif c>b and c>a:
    print("Variable 'c' is greatest.")
else:
    print("Are they equal !!!!!")