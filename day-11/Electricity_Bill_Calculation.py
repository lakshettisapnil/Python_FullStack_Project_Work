units = int(input("Enter The units: "))
bill = 0
Tax = 0
if units <= 100:
    bill = units * 3
    print(f'Units Consumed: {units}')
elif units <= 200:
    print(f'Units Consumed: {units}')
    bill = (100 * 3) + (units-100) * 5
elif units <= 300:
    print(f'Units Consumed: {units}')
    bill = (100 * 3) + (100 * 5) + (units - 200) * 7
else:
    bill = (100 * 3) + (100 * 5) + (100 * 7) + (units - 300) * 10
    print(f'Units Consumed: {units}')
print(f'Total bill Before The Tax: {bill}')
Tax = bill * 0.05
bill = bill + Tax
print(f'Tax amount: {Tax}')
if bill > 5000:
    bill = bill-500
    print(bill)
else:
    print(bill)

