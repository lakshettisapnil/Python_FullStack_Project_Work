import csv

def find_max(a, b, c):
    return max(a, b, c)

with open('facttc.csv', 'r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        a = int(row['inp1'])
        b = int(row['inp2'])
        c = int(row['inp3'])
        expected = int(row['out'])

        if find_max(a, b, c) == expected:
            print("Test case passed for:", a, b, c)
        else:
            print("Test case failed for:", a, b, c)