def remove_all_occarence(list_l,x):
    k = 0
    for i in range(len(list_l)):
        if list_l[i] != x:
            list_l[k] = list_l[i]
            k+=1
    return list_l[:k] 
list_l = list(map(int,input("Enter the elements: ").split()))
x = int(input("Enter the removel element: "))
res = remove_all_occarence(list_l,x)
print(res)