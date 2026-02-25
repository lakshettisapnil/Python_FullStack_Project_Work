def atm_withdraw(balance):
    if amount == 0:
        print("Enter valid amount")
    else:
        while True:
            if amount >= balance:
                print("insuficiant balance")
                break
            else:
                balance-=amount
                print(f'your withdrawn balance is: {amount}')
                print(f'Your main account balance is: {balance}')

balance = 10000
amount = int(input("Enter amount: "))
res = atm_withdraw(balance)