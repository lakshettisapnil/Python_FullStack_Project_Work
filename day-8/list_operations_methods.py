# list operations 
s = [4, 5, 6, 7]
b = [7, 8, 9]
# concatination
print(s+b)
# repeatation 
print(s * 2)
# lenght check 
print(len(s))
# indexing
print(s[0])
# slicing
print(s[1:3])
# membership check 
rs = 5 in s
print(rs)
# iteration of the list 
for i in s:
    print(i)
# list methods 
# adding  an element to the list (append, insert, extend)
# append which adds an element at end of the list
s.append(8)
print(s)
# insert the element at specific position 
s.insert(1,9)
print(s)
# extend which adds the multiple elemnts to the list 
s.extend(b)
print(s)
# count which counts occurance of the elemts 
print(s.count(8))
# index finds the index of the value 
print(s.index(8))
# sort and sorted if use sorted then only perment change not effect to the original list used in tuple, set, string dict
# if u use sort then it will change the original list and sort only method in list not in tuple, set, string 
s = sorted(s)
print(s)
s = s.sort()
print(s)
# reverse the list 
s.reverse()
# pop removes the elemet from lst pop(1) removes the element of index 1  value 
# remove the last element from the list 
s.remove()
s.remove(2) # remove the 1st occerence of value 2 
