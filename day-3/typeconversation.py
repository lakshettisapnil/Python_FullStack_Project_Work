# type Conversion is a converting from one data type to another data type 
# int, float, complex, string, list, tuple, set, dict, bool, None
# 1st into to float Conversion
a = 10
a = float(a)
print(a)
print(type(a))
# into to string
a = 20
a = str(a)
print(a)
print(type(a))
# into to complex 
a = 10
a = complex(a)
print(a)
print(type(a))
# int to list into to list Conversion
'''a = 20
a = list(a)
print(a)
print(type(a)) # typeError object is not iterable '''
# into to tuple into to tuple conversion is not possible 
'''a = 19
a = tuple(a)
print(a)
print(type(a))'''
# into to set is not possible 
'''a = 10
a = set(a)
print(a)
print(type(a))'''
# into to dict also not possible 
'''a = 10
a = dict(a)
print(a)
print(type(a))'''
# into to bool is possible 
a = 10 
a = bool(a)
print(a)
print(type(a))
# 2nd float conversion 
# float to into is possible 
a = 10.5
a = int(a)
print(a)
print(type(a))
# float to string is possible 
a = 10.5
a = str(a)
print(a)
print(type(a))
# float to complext is possible 
a = 10.5
a = complex(a)
print(a)
print(type(a))
# float to list is not possible
'''a = 10.5
a = list(a)
print(a)
print(type(a))'''
# float to tuple, set, dict, not possible 
# float to bool possible
a = 10.5
a = bool(a)
print(a)
print(type(a))
# 3rd string to into not possible and string to float is also not possible 
'''a = 'swapnil'
a = int(a)
print(a)
print(type(a))
a = float(a)
print(a)'''
# string to complex not possible
'''a = 'sp'
a = complex(a)
print(a)
print(type(a))'''
# string to list possible 
a = 'swapnil'
a = list(a)
print(a)
# string to tuple possible 
a = 'swapnil'
a = tuple(a)
print(a)
print(type(a))
# string to set possible
a = 'swapnil'
a = set(a)
print(a)
print(type(a))
# string to dict not possible 
'''a = 'swapnil'
a = dict(a)
print(a)
print(type(a))'''
# string to bool possible 
a = 'swapnil'
a = bool(a)
print(a)
# 4th list to to int, float, copmplex, not possible 
# list to string possible 
a = [2, 3, 'swapnil']
a = str(a)
print(a)
print(type(a))
# list to tuple possible 
a = [2, 3, 4, 'swapnil']
a = tuple(a)
print(a)
print(type(a))
# list to set possible 
a = [2, 3, 4, 'swapnil']
a = set(a)
print(a)
print(type(a))
# list to dict is not possible 
'''a = [2, 3, 4, 'swapnil']
a = dict(a)
print(a)
print(type(a))'''
# list to bool posible 
a = [2, 3, 4, 'swapnil']
a = bool(a)
print(a)
print(type(a))
# 5th tuple to int, float, complex, dict not possible 
# tuple to string possible 
a = (2, 3, 4, 'swapnil')
a = str(a)
print(a)
print(type(a))
# tuple to list possible 
a = (2, 3, 4, 'swapnil')
a = list(a)
print(a)
print(type(a))
# tuple to set possible 
a = (2, 3, 4, 'swapnil')
a = set(a)
print(a)
print(type(a))
# 6th set to int, float, complex, dict, not possible 
# set to string, tuple, list, possible 
# 7th dict to list possible 
a = {'name':'swapnil'}
a = list(a)
print(a)
print(type(a))
# dict to set possible 
a = {'name':'swapnil'}
a = set(a)
print(a)
print(type(a))
# dict to tuple possible 
a = {'name':'swapnil'}
a = tuple(a)
print(a)
print(type(a))

