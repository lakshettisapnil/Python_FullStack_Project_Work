# string operations 
# concatination 
a = 'swapnil'
b = 'swapnil'
print(a+b)
# repeatation 
print(a * 5)
# indexing 
print(a[0])
# slicing 
print(a[1:4])
# membership check 
print('s' in a)
# lenght check
print(len(a))
# string methods 
# upper, lower
a.upper()
print(a)
a.lower()
print(a)
# strip methodd which remove the spaces
a.strip()
print(a)
# slpit method which is used to devide the string into small parts 
a.split()
# converts the first letter of string to upper case
txt = 'python programming'
x = txt.capitalize()
print(x)
# converst the upper to lower case
txt = 'PYTHON proGramming'
x = txt.casefold() # lower
print(x)

# center the string
txt = 'python programming'
x = txt.center(30,'-')
print(x)

# count count the number of times a specific value occurs

txt = 'python programming'
x = txt.count('p')
print(x)

# find the position of the character same as index but index throws an exception error 
txt = 'python programming'
x = txt.find('m')
print(x)

# isalnum return the true if the all the values are alpha and numeric if space in b/w them then returns false
txt = 'pythonprogramming32'
x = txt.isalnum()
print(x)
# tile makes first char as capital case 
x = txt.title()
print(x)

