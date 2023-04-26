# colllection type
# tuple            - immutable object
# list             - mutable object
# dictionary       - mutable objects
# set              - unique set of objects

# tuple
tup = (1, 2, 'A', tuple(), (34,'they'))
print("Tuple: ",tup)
print('\nInteger data value in above tuple:',tup[0],'&',tup[1])
print('\nString data value in above tuple:',tup[2],'&',tup[4][1])
print('\nA Tuple in data value in above tuple:',tup[3],'&',tup[4])


print('-'*100)

# list 
lis = [3, 4, 11.34, 'B', list(), [56, 'now']]
print("List: ",lis)
print('\nInteger data value in above list:',lis[0],'&',lis[1])
print('\nFloat data value in above list:',lis[2])
print('\nString data value in above list:',lis[3],'&',lis[5][1])
print('\nA List in data value in above list:',lis[4],'&',lis[5])


print('-'*100)

# dictionary
dic = {'A':1,'B':2.3,
       'C':[3,4],
       3.14:('PIE','22/7'),
       'D':{'i':90,
            'ii':56}
        }
print("Dictionary: ",dic)
print('All keys in this Dictionary: ',list(dic.keys()))
print('All values in this Dictionary: ',list(dic.values()))\


print('-'*100)

# set
st = {2,4.5,4,8,'str'}
print("Set: ",st)


print('-'*100)