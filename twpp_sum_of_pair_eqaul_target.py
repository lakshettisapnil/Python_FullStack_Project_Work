# time complexity o(n) space is o(1)
def sum_of_pair(list_elements,target):
    left, right = 0,len(list_elements)-1
    while left < right:
        sum = list_elements[left] + list_elements[right]
        if sum == target:
            return True 
        elif sum < target:
            left+=1
        else:
            right-=1
    return False 

list_elements = list(map(int,input("Enter the elements: ").split()))
target = int(input("Enter the target: "))
res = sum_of_pair(list_elements,target)
if res:
    print("True")
else:
    print("False")