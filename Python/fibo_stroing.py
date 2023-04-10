# generate fibonacci series and store the element in a dictionary and list

def fibo(n):
    f = 0
    s = 1

    lis_fibo = []
    dic_fibo = {}
    for i in range(0,n):
        print(f,end=' ')
        lis_fibo.append(f)
        dic_fibo[i] = f

        temp = f
        f = s
        s += temp

    return lis_fibo, dic_fibo


inp_fibo = int(input("Enter no of elements for fibo: "))
fibo(inp_fibo)

