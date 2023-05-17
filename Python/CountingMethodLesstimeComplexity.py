# Time Complexity : Time complexity is defined as the amount of time taken by an 
#                    algorithm to run, as a function of the length of the input.

# for example: Write a Program to count number of e plus one for the given respective string
example_stings = ['Heisenberg','interchangeable','ElectrophorEsis']

def countE(strings):
    c = 1                         # extra value to count extra
    for i in strings:               # taking a letter by letter
        if i.lower() == 'e':          # checking for 'e'
            c+=1                        # incrementing by 1 if true
    return c                        # return requirement

def countE2(strings):                 
    li = strings.lower().split('e')         # making a list splitted respectively by 'e' all in lowercase
    return len(li)                          # returning length of list (this gives extra by itself)

def countE3(strings):               
    word = strings.lower()                  # making all in lowercases
    cnt = word.count('e')+1                 # counting e by count function directly and increasing 1
    return cnt                              # returning the requirement


# testing all cases at once
for i in example_stings:
    print("1st function: ",countE(i),"for",i)
    print("2nd function: ",countE2(i),"for",i)
    print("3rd function: ",countE3(i),"for",i)

# in this code we have seen countE() can be reduce to countE2() and countE3()