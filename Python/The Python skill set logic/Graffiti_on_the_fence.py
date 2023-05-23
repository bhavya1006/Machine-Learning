l = int(input())
n = int(input())
sti = 0
di = {}
for i in range(n):
    st, ed = [int(j) for j in input().split()]
    di[st] = ed
diff = 0
for i in di:
    diff += (di[i]-i)
# print(diff)
# print(len(di))
if diff == l:
    print("All painted")
else:
    for i in di:
        if i > sti:
            print(sti,i)
        if sti >= di[i]:
            di[i] = sti
        sti = di[i]

    if sti != l:
        print(di[i],l)