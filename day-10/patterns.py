''''n = int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        print(j,end=' ')
    print()'''
'''n = int(input())
for i in range(n):
    for j in range(n):
        print(i,end=' ')
    print()'''

'''n = int(input())
num = 0
for i in range(n):
    for j in range(n):
        print(num,end=' ')
        num+=1
    print()'''
'''num = 0
for i in range(n):
    for j in range(n):
        print(i+j,end=' ')
    print()'''
'''for i in range(n):
    for j in range(n):
        if i+j%2 == 0:
            print('0')
        else:
            print('x')
    print()'''
'''for i in range(n):
    for j in range(i+1):
        print('* ')'''
'''for i in range(n):
    for j in range(n-i):
        print('* ',end=' ')
    print()'''
'''n = int(input())
for i in range(n):
    spaces = (n-i) * " "
    for j in range(i+1):
        stars = j * "* "
        print(spaces+stars)
    print()'''
'''n = int(input())
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i==n-1 or j == n-1:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()'''
'''n = int(input())
for i in range(n):
    for j in range(n):
        if i == 0 or j == n-1 or i+j==n-1 :
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()'''
'''n = int(input())
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i==n-1 or j == n-1 or i == n//2 or j==n//2 :
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()'''
 
