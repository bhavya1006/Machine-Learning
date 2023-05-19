def find_average(n): 
    return 0 if len(n)==0 else sum(n)/len(n)

n = [3,4,5,7]
print(find_average(n))
n = []
print(find_average(n))