# Creating Set
s = {1, 2, 3, 4}
print("Original Set:", s)
# Adding Elements
s.add(5)
print("After add():", s)

# add() only adds one element
# Updating (adding multiple elements)
s.update([6, 7])
print("After update():", s)
# Removing Elements
s.remove(7)      # error if element not found
print("After remove():", s)

s.discard(10)    # no error if element not found
print("After discard():", s)

removed = s.pop()   # removes random element
print("After pop():", s)
print("Removed element:", removed)

# Another Set for Operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Union
print("Union:", a.union(b))
print("Using | :", a | b)

# Intersection
print("Intersection:", a.intersection(b))
print("Using & :", a & b)

# Difference
print("Difference a-b:", a.difference(b))
print("Using - :", a - b)

# Symmetric Difference
print("Symmetric Difference:", a.symmetric_difference(b))
print("Using ^ :", a ^ b)

# Membership
print("2 in a?", 2 in a)

# Looping
print("Looping through set:")
for item in a:
    print(item)

# Copy
new_set = a.copy()
print("Copied Set:", new_set)

# Clear
new_set.clear()
print("After clear():", new_set)