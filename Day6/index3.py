class Lab_account:
    account_balance = 100000
    

class Showroom_account:
    account_balance = 500000

class Service_center_account:
    account_balance = 200000

class Main_account:
    account_balance = (Lab_account.account_balance + Showroom_account.account_balance + Service_center_account.account_balance)


show_total_balance = Main_account()
print("Total balance in main account is:", show_total_balance.account_balance)