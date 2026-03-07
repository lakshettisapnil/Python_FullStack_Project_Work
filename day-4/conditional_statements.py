st_list = ["swapnil","Shanmukh", "dileep","ravi"]
name  = input("Enter name: ")
if name in st_list:
    print(f"{name} is found in the st_list\n check {name} acadamic details")
else:
    print(f"{name} is not found in the st_list\n add {name} in acadamic details")
amount = int(input("Enter The Amount: "))
if amount > 50000:
    print("Go for other contires like Russia")
elif amount > 20000:
    print("go for dubai")
elif amount > 10000:
    print("go for america")
elif amount > 1000:
    print("go for aus")
else:
    print("sleep at home")