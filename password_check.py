pwd = input("Enter The Password: ")
if len(pwd) >= 8:
    s = set()
    for i in pwd:
        if i.isupper():
            s.add("upper")
        elif i.islower():
            s.add("lower")
        elif i.isdigit():
            s.add("digit")
        else:
            s.add("special")
    if len(s) == 4:
        print("Strong Password")
    else:
        print("Weak Password")
else:
    print("Lenth needs to be >= 8")