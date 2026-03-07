# for loop if we know the how many times to iterat we will go with for loop
# if we dont know how many times to iterate we will go with while loops
s = [2, 3, 4, 5, 2]
for i in s:
    print(i)
# iterating using the range start from 0 to n-1 
for i in range(len(s)):
    print(s[i])
# in list we dont no how many times the 2 will occurs thats why we are using while loop
while 2 in s:
    s.remove(2)
print(s)