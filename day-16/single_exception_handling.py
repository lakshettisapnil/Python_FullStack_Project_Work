# single exception
'''try:
    if a>10:
        print("Good")
except NameError:
    print("a is not defined")
else:
    print("There is no error")
finally:
    print("Always executed")'''
# multiple exception
'''try:
   a = [1,2,3,4]
   print()
except NameError:
    print("a is not defined")
except ValueError:
    print("please give the correct input")
except TypeError:
    print("the int type and the str type can not added")
except IndexError:
    print("access the value inside the range of list")
except KeyError:
    print("the key is not there in dict")
except ZeroDivisionError:
    print("we can't divid anything with the zero")
else:
    print("There is no error")
finally:
    print("Always executed")'''
# handle using single except
'''try:
    a = a+'p'
except (NameError,ValueError,TypeError,ZeroDivisionError,IndexError,KeyError) as e:
    print(f'Error Occured: {e}')
else:
    print("No Errors")
finally:
    print("End of block")'''
'''try:
    a = a+'p'
except Exception as e:
    print(f'Error Occured: {e}')
else:
    print('No Erros')
finally:
    print("Always execute the finall block")'''
# raise exception 
'''try:
    a = int(input())
    if a<0:
        raise Exception('Enter the positive value')
except Exception as e:
    print(f'Error Occured: {e}')
else:
    print('No Erros')
finally:
    print("Always execute the finall block")'''
while True:
    print("\n-- ATM Simulation Menu ---")
    print("1. Check Average Transactions (ZeroDevisionErros)")
    print("2. Withdraw With Invalid Input (ValueError)")
    print("3. Desposite with invalid data type (TypeError)")
    print("4. Acess invalid trascation history (IndexError)")
    print("5. Access Non-Existent Account (KeyError)")
    print("6. Read missing transaction log file (FileNotFoundError)")
    print("7. Exit")
    choice = input("Enter the chloice (1-7): ")
    if choice == '1':
        Zero_devision_error_case()
    elif choice == '2':
        Value_Error()
    elif choice == '3':
        type_error()
    elif hoice == '4':
        index_error()
    elif choice == '5':
        key_error()
    elif choice == '6':
        file_not_found_error()
    elif choice == '7':
        exit_block()
def Zero_devision_error_case():
    try:
        trans = []
        avg_trans = sum(trans) / len(trans)
        print("Average Transaction: ", avg_trans)
    except ZeroDivisionError:
        print("Eooe: Cannot caluclate the avg transcation")
def Value_Error():
    try:
       w_amount = int('100 /')
       print("Withdraw amount: ", w_amount)
    except ValueError:
        print("Error: Invalid value Entered. Please enter a numeric amount")
def type_error():
    try:
        balance = 500
        d_balance = '100'
        new_balance = balace+d_balace
        print("new Balance: ", new_balance)
    except TypeError:
        print("Error: can't add string and int data types")
def index_error():
    try:
        t_history = [200, -150, 300]
        print("Last_transaction history: ", t_history[5])
    except IndexError:
        print("Error: There is not 5 transactions")
def key_error():
    try:
        accounts = {'1234': {'Pin':4567, 'balance':1000,}}
        ac_number = '234567'
        print("Account Balance: ", acounts[ac_number]['balance'])
    except KeyError:
        print("Error: The account not Exist please enetr valid account number")
def file_not_found_error():
    try:
        with open("trasaction_log.tex",'r') as file:
            



