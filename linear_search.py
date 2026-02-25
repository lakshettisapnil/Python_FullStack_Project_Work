def linear_search(arr,val):
    for i in range(len(arr)):
        if arr[i] == val:
            return arr[i]
    else:
        return -1
arr = list(map(int,input().split()))
val = int(input())
result = linear_search(arr,val)
if result == -1:
    print("The Value is not found in the array: ")
else:
    print(f'the value is found {result}')
