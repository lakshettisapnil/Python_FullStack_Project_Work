name  = input("Enter The Name: ")
dob = input("Enter The dob [YYYY-MM-DD]: ")
username = name[:2]+name[-2:]+dob[-2:]+dob[2:4]
print(f" Hii {name}!\n Your User Name is {username}")