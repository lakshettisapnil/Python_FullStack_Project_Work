#position arg
def display(uname,password,email):
    print(f'username: {uname}')
    print(f'password: {password}')
    print(f'email: {email}')
    
display('swapnil','Swapnil@1234', 'lakshettysapnil@gmail.com')
#key arg
def display(uname,password,email):
    print(f'username: {uname}')
    print(f'password: {password}')
    print(f'email: {email}')
    
display(uname='swapnil',password='Swapnil@1234', email='lakshettysapnil@gmail.com')
display(password='Swapnil@1234',uname='swapnil', email='lakshettysapnil@gmail.com')
display(email='lakshettysapnil@gmail.com',uname='swapnil',password='Swapnil@1234')
# default arg
def display(uname,password,email,status='absent'):
    print(f'username: {uname}')
    print(f'password: {password}')
    print(f'email: {email}')
    print(f'status: {status}')
    
display('swapnil','Swapnil@1234','lakshettysapnil@gmail.com','present')
# if we did't no the num of args
def display(*names):
    for i in names:
        print(i)
    else:
        print("end of the list")
display('swapnil')
display('sirisha', 'meghana','hema')
display('sirisha', 'meghana')
display('sirisha', 'meghana','hema','siri')
