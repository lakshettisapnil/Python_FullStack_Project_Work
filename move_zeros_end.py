def move_zeros_end(l):
    j = 0
    for i in range(len(l)):
        if l[i] != 0:
            l[j],l[i] = l[i],l[j]
            j+=1
    return l
l = list(map(int,input("Enter the elements: ").split()))
res = move_zeros_end(l)
print(res)