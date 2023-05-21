n = int(input())
for i in range(n):
    name = input()
    lisrem = ['Dr', 'Mr', 'Mrs', 'Ms' , 'Lord', 'Lady','Sir', 'BA', 'LLB' , 'MD' , 'PhD','Jr','Snr']
    for j in lisrem:
        name = name.replace(j,'')
    for k in name.split():
        print(k[0],end='.')
    print()