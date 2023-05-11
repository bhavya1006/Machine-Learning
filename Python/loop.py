# For running a code many times in a sequence and series, loops are used which also specifies
# the need in coding, now taking input for 100 times for student for a data storing and process,
# we may directly use loop.

# Requirement for implementing loop
# 1) Initialization for loop counter
# 2) Range/Condition till counter works
# 3) Updation in loop counter
# 4) {Code} - formatting for code must be functionalized as to run many times 


# Two ways to implement loops in python
# i)  for-loop
# ii) while-loop

# i)  for-loop 
# This doesn't require the condition rather it works under 
# a range or any datatype for taking each value possible by it

####SYNTAX####
# for var in {range(start,stop,common difference)/datatype}:
#     {CODE}

print("Example 1.1: For-Loop")
for var in range(10):
    print(var,end=' *-* ')

print("\nExample 1.2: For-Loop")
for var in range(10,0,-1):
    print(var,end=' ')

print("\nExample 2: For-Loop")
d = {1:'A',2:'B',3:'C'}
for var in d:
    print(f'Key {var} has value {d[var]}')


# i)  while-loop 
# This does require the condition and updation to avoid
# infinite loop. And code runs unless condition is false 

####SYNTAX####
# while (condition):
#     {CODE}
#     (updation)

print("\n\nExample 1.1: while-Loop")
i = 0
while i<10:
    print(i,end=' ')
    i += 1

print("\nExample 1.2: while-Loop")
i = 0
while 10-i>0:
    print(10-i,end=' > ')
    i += 1

print("\nExample 2: while-Loop")
i = 4
while True:
    if i == 0:
        print("Thanks")
        break
    else:
        print("Wait one more process!!")
        i -= 1