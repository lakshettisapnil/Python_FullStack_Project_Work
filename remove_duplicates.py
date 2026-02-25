list_l = list(map(int,input().split()))
k = 1
for i in range(1,len(list_l)):
    if list_l[i] != list_l[i-1]:
        list_l[k] = list_l[i]
        k+=1
print(list_l[:k])

