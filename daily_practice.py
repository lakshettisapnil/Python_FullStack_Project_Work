'''with open('sample.txt','r') as file:
    content = file.read()
    print(content)'''
'''with open('sample.txt', 'w') as file:
    file.write('Hello swapnil\n')
    file.write('how are you')'''
'''with open('sample.txt','r') as file:
    content = file.read()
    print(content)'''
'''with open('sample.txt','a') as file:
    file.write("who about you\n")'''
'''with open('sample.txt','r') as file:
    for line in file:
        print(line)'''
# csv file operations
import csv
'''with open('sample.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'age', 'city'])
    writer.writerow(['swapnil', 20, 'hyd'])
    writer.writerow(['sham', 21, 'delhi'])'''
'''with open('sample.csv','r') as file:
    reader = csv.reader(file)
    for cn in reader:
        print(cn)'''
'''with open('sample.csv', 'a', newline="") as file:
    writer = csv.writer(file)
    writer.writerow(['hema', 22, 'mumbai'])'''

'''with open('sample.csv','r') as file:
    reader = csv.reader(file)
    for cn in reader:
        print(cn)'''

'''data = [
    {"Name":"Rahul","Age":20,"City":"Delhi"},
    {"Name":"Anu","Age":22,"City":"Mumbai"}
]
with open('sample.csv','w',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(data)'''
'''with open('sample.csv','r') as file:
    reader = csv.reader(file)
    for cn in reader:
        print(cn)'''
# json 
import json

'''data = {'name':'swapnil','age':20,'city':'bhr'}
with open('sample.json','w') as file:
    json.dump(data,file,indent=4)'''
'''with open('sample.json', 'r') as file:
    data = json.load(file)
    print(data.values())'''
'''new_data = {'name':'hema','age':20,'city':'delhi'}
with open('sample.json', 'r') as file:
    data = json.load(file)
data.append(new_data)'''
'''data =  {'Title':'Python basics','Author':'Jon Deo','Price':600}
with open('data.json','w',newline='') as file:
    json.dump(data,file,indent=4)
for key, value in data.items():
    print(key, value)'''

'''char = set()
char.add()
print(char)'''
'''count = 0
for i in range(1,11):
    if i % 2 == 0:
        count+=i
print(count)'''
m = [1,2]
n = [3,4,5]
print(m+n)





