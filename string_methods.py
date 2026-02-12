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


