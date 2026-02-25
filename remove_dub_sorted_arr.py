l = list(map(int,input("Enter the list elements: ").split()))
for i in range(len(l)):
    for j in range(len(l)):
        if l[j] in l:
            l.remove(l[j])
print(l)