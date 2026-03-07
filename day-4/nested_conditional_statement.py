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