Monthly_Salary = int(input("Enter The Salary: "))
Existing_loan_amount = int(input("Enter The Existing Loan Amount: "))
Credit_Score = int(input("Enter The Credit Score: "))

if Monthly_Salary > 30000 and Credit_Score > 700 and Existing_loan_amount < 50000:
    print("Your Eligible For Loan")
else:
    print("Your Not Eligible For The Loan")