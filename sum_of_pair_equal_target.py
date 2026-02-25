def sum_pair(list_elements,target):
    for i in range(len(list_elements)):
        for j in range(i+1,len(list_elements)):
            if list_elements[i] + list_elements[j] == target:
                return True
    return False  
list_elements = list(map(int,input("Enter the elemts: ").split()))
target = int(input('Enter the target: '))
res = sum_pair(list_elements,target)
if res:
    print("True")
else:
    print("False")

