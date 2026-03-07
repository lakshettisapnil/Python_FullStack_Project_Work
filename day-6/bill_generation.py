data = {
    1:{'products':'Rice','price': 60},
    2:{'products':'wheat','price': 40},
    3:{'products':'sugar','price': 80},
    4:{'products':'milk','price': 20},
    5:{'products':'eggs','price': 10},
    6:{'products':'coocking oil','price': 130},
    7:{'products':'bread','price': 50},
    8:{'products':'butter','price': 90},
    9:{'products':'soap','price': 70},
    10:{'products':'shampoo','price': 60}
}
print('index'.ljust(7,' '), 'Product Name'.ljust(20, ' '), 'Price'.ljust(30, ' '))
for i in data:
    print(str(i).ljust(7, ' '),data[i]['products'].ljust(20, ' '), str(data[i]['price']).ljust(30,' '))

indexes = list(map(int, input("Enter the index number").split()))
c_set = set(indexes)
print('Your Bill'.center(30,'-'))
total_bill = 0
s = set()
print('Product Name'.ljust(30,' '), 'Qty'.ljust(10,' '), 'Price'.ljust(10,' '), 'Total_Price'.ljust(10,' '))
for i in indexes:
    if i not in s:
       print(f'{data[i]['products'].ljust(30,' ')}  {str(indexes.count(i)).ljust(10, ' ')} {str(data[i]['price']).ljust(10,' ')} {data[i]['price'] * indexes.count(i)}')
       total_bill += data[i]['price'] * indexes.count(i)
       s.add(i)
print(f'Your total bill is {total_bill}\n -------Thank you for shopping-------')