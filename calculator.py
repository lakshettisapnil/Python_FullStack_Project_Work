def add(a,b):
    return a+b 
def sub(a,b):
    return a-b 
def mul(a,b):
    return a * b 
def div(a,b):
    return a / b
def div(a,b):
    return a % b

exp = input("Enter the expresssion: ")
for i in exp:
    if i == '+':
        a,b = exp.split('+')
        print(add(int(a),int(b)))
    elif i == '-':
        a,b = exp.split('-')
        print(add(int(a),int(b)))
    elif i =='*':
        a,b = exp.split('*')
        print(add(int(a),int(b)))
    elif i == '/':
        a,b = exp.split('/')
        print(add(int(a),int(b)))
    elif i == '%':
        a,b = exp.split('%')
        print(add(int(a),int(b)))

