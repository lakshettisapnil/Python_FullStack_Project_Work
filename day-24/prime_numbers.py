import csv
def is_prime(n):
    for i in range(2,n//2+1):
        if n%i == 0:
            return 'Not a prime number'
    return 'Prime number'
with open('primetc.csv','r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        if is_prime(int(row['input']) == row[' output']):
            print(row['input'], "test Case Passed")
        else:
            print(row['input'], "Test Case Failed")
            