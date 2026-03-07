# data types in python
# int data type the type function which is used to disply the type of the data 
a = 10
print(type(a))
# in python we can't need to decalre type of data like int, float, string python automatically assigns data type
# float data type
b = 10.5
print(type(b))
# complex data type 
b = 3+4j
print(type(b))
# string data type the string data type is decalred in "" or in ''
st = 'Swapnil'
print(type(st))
# list data type the list is a ordered collection of different data types enclosed in [] square brackets
ls = ['swapnil', 4 , 10.5, 4+3j, (3, 4, 5), {'name':'swapnil', 'clg':'cmr'}]
print(ls)
print(type(ls))
# set data type the set data type is unordered collection of dofferent data types duplicates are not allowed enclosed in {}
# in mutable data types we can take only immutable data types like string, tuple but not list, dict
st = {2, 'swapnil', 10.5, (3, 4, 5)}
print(st)
print(type(st))
# tuple data type with is collection of oredered different mutable and immutable data types, it is an immutable 
tp = (3, 10.5, 'swapnil', [5,6,7], {'name':'swapnil'})
print(tp)
print(type(tp))
# dictionary it sore the data in key vallur pairs it is an mutable data type enclosed with {}
dt = {'name':'swapnil', 'clg':'cmr'} # name and clg are the keys and swapnil and cmr are the values
print(dt)
print(type(dt))