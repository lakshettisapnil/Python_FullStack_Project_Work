# Creating Dictionary
d = {"name": "Swapnil", "age": 22, "city": "Mumbai"}
print("Original Dictionary:", d)
# Accessing Values
print("Access name:", d["name"])
print("Using get():", d.get("age"))
# Adding New Key-Value
d["course"] = "Python"
print("After Adding:", d)
# Updating Value
d["age"] = 23
print("After Updating Age:", d)
# update() Method
d.update({"city": "Pune"})
print("After update():", d)
# Removing Elements
d.pop("city")             # remove specific key
print("After pop():", d)
d.popitem()               # remove last inserted item
print("After popitem():", d)
# Adding Again for Demo
d["salary"] = 50000
d["company"] = "TCS"
# keys(), values(), items()
print("Keys:", d.keys())
print("Values:", d.values())
print("Items:", d.items())

# Checking Membership
print("name in dict?", "name" in d)

# Looping Through Dictionary
print("Looping Keys:")
for key in d:
    print(key)

print("Looping Values:")
for value in d.values():
    print(value)

print("Looping Key-Value:")
for key, value in d.items():
    print(key, ":", value)

# copy()
new_d = d.copy()
print("Copied Dictionary:", new_d)

# clear()
new_d.clear()
print("After clear():", new_d)

# setdefault()
d.setdefault("country", "India")
print("After setdefault():", d)