def binary_search(arr,target,low,height):
    while low<=height:
        mid = (low+height)//2
        if arr[mid] == target:
            return mid
            break
        elif arr[mid] < target:
            low = mid+1
        else:
            height = mid-1
    return -1

arr = list(map(int, input("Enter list Elements: ").split()))
arr.sort()
target = int(input("Enter target: "))
low = 0
height = len(arr)-1
res = binary_search(arr,target,low,height)
if res!=-1:
    print(f'elemennt is found: {res}')
else:
    print("element is not found: ")