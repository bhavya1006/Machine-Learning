l = int(input())
n = int(input())
diff,ist = 0,0
lst,led = [],[]
flag = False
for i in range(n):
    st, ed = [int(j) for j in input().split()]
    diff += (ed-st)
    if diff >= l:
         flag = True
         break
    if ist >= ed:
         ed = ist
    if st > ist:
        lst.append(ist)
        led.append(st)
    if i == n-1 and ed != l:
        lst.append(ed)
        led.append(l)
    ist = ed

# print(lst)
# print(led)

if flag:
        print("All painted")
else:
     for j in range(len(led)):
          print(lst[j],led[j])










































# di = {}
#     di[st] = ed
# diff = 0
# for i in di:
#     diff += (di[i]-i)
# # print(diff)
# # print(len(di))
# if diff == l:
#     print("All painted")
# else:
#     for i in di:
#         if i > sti:
#             print(sti,i)
#         if sti >= di[i]:
#             di[i] = sti
#         sti = di[i]

#     if sti != l:
#         print(di[i],l)