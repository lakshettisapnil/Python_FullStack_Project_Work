'''st_list = ["swapnil","Shanmukh", "dileep","ravi"]
name  = input("Enter name: ")
if name in st_list:
    print(f"{name} is found in the st_list\n check {name} acadamic details")
else:
    print(f"{name} is not found in the st_list\n add {name} in acadamic details") '''
'''amount = int(input("Enter The Amount: "))
if amount > 50000:
    print("Go for other contires like Russia")
elif amount > 20000:
    print("go for dubai")
elif amount > 10000:
    print("go for america")
elif amount > 1000:
    print("go for aus")
else:
    print("sleep at home") '''
'''to access the dict or nested dict data data is a dicct and user is a nested list now data[user] = we will get the all the data of the user 
if need he is writeen exam or not data[user]['status'] example is below'''
data = {
    'Swapnil': {'status': True, 'Python': 80, 'SQL': 40, 'java': 90},
    'Abhi': {'status': True, 'Python' : 60, 'SQL': 39, 'java': 99},
    'shanu': {'status': True, 'Python' : 50, 'SQL' : 80, 'java': 70}
}
user = input()
if user in data:
    if data[user]['status']:
        sum = data[user]['Python'] + data[user]['SQL'] + data[user]['java']
        avg = sum/3
        if avg > 80:
            print(f"{user} have good knowlegde\n got 'A' Rank")
        elif avg > 60:
            print(f"{user} average\ngot 'B' Rank")
        elif avg > 40:
            print(f"{user} need to improve\n got 'c' Rank")
        else:
            print(f"{user} is failed")
    



