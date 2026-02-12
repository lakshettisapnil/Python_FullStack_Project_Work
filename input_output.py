customer_name = input("Enter The Customer Name: ")
mobile_number = int(input("Enter The Mobile Number: "))
product_1 = input("Enter Product Name_1: ")
price_1 = float("Enter Price_1: ")
product_2 = input("Enter Product Name_2: ")
price_2 = float("Enter Price_2: ")
product_3 = input("Enter Product Name_3: ")
price_3 = float("Enter Price_3: ")

print(f"{customer_name} Your Bill")
print(f"customer mobile number {mobile_number}")
print(f"{product_1}: ${price_1}")
print(f"{product_2}: ${price_2}")
print(f"{product_3}: ${price_3}")
Total_bill = price_1+price_2+price_3 
print(f"Total Bill is: {Total_bill}")
 
