  class ATM:
    def __init__(self, account_number, balance, pin):
      self.account_number = account_number
      self.balance = balance
      self.pin = pin


    def deposit(self, amount):
      self.balance  += amount
      print(f"Deposit {amount} bath successful!")
      print(f"Your balance is {self.balance} bath.")

    def withdraw(self, amount):
      if amount > self.balance:
          raise ValueError("Insufficient funds")
      self.balance -= amount
      print(f"Withdraw {amount} bath successful!")
      print(f"Your balance is {self.balance} bath.")

    def transfer(self, to_account_number, amount):
      if amount > self.balance:
          raise ValueError("Insufficient funds")
      self.balance -= amount
      print(f"Transfer {amount} bath to {to_account_number} successful!")
      print(f"Your balance is {self.balance} bath.")

    def check_balance(self):
      print(f"Your balance is {self.balance} bath.")

    def change_pin(self, pin):
      self.pin = pin
      print("Change Pin successful")
      print(f"Your new pin is {pin}")


import pandas as pd
from tabulate import tabulate

  def ATM_item():
    # create data frame
    transaction_list = []
    transaction_df = pd.DataFrame(transaction_list , columns=['Transaction Number', 'Account Number', 'Transaction', 'Amount', 'Balance', 'Pin'])

    def print_statement():
      #print(f"Total transaction of {transaction_number - 1} items.")
      #print(transaction_df)

      table = tabulate(transaction_df, headers='keys', tablefmt='psql')
      print(f"Total transaction of {transaction_number - 1} items.")
      print(table)

    # start ATM
    transaction_number = 1
    print("Welcome to ATM!")
    account_number = input("Please input Account number :")
    balance = int(input("Please input Balance :"))
    pin = input("Please input your pin :")
    atm = ATM(account_number, balance, pin)
    transaction_df.loc[transaction_number, 'Transaction Number'] = transaction_number
    transaction_df.loc[transaction_number, 'Account Number'] = account_number
    transaction_df.loc[transaction_number, 'Transaction'] = 'Add account'
    transaction_df.loc[transaction_number, 'Amount'] = balance
    transaction_df.loc[transaction_number, 'Balance'] = balance
    transaction_df.loc[transaction_number, 'Pin'] = pin
    print(f"Add account {account_number} total {balance} and pin {pin} successful!")
    print(f"Your balance is {balance} bath.")

    while True:
      transaction_number = transaction_number + 1
      transaction = input("Please enter number of transaction below\n1 : Deposit\n2 : Withdraw\n3 : Transfer\n4 : Balance check\n5 : Change Pin\nq : quit\n")
      if transaction == 'q':
        print("End of transaction")
        print_statement()
        break
      elif transaction == '1':
        amount = int(input("Please input deposit amount :"))
        atm.deposit(amount)
        transaction_df.loc[transaction_number, 'Transaction Number'] = transaction_number
        transaction_df.loc[transaction_number, 'Account Number'] = atm.account_number
        transaction_df.loc[transaction_number, 'Transaction'] = 'Deposit'
        transaction_df.loc[transaction_number, 'Amount'] = amount
        transaction_df.loc[transaction_number, 'Balance'] = atm.balance
        transaction_df.loc[transaction_number, 'Pin'] = atm.pin
      elif transaction == '2':
        amount = int(input("Please input withdraw amount :"))
        atm.withdraw(amount)
        transaction_df.loc[transaction_number, 'Transaction Number'] = transaction_number
        transaction_df.loc[transaction_number, 'Account Number'] = atm.account_number
        transaction_df.loc[transaction_number, 'Transaction'] = 'Withdraw'
        transaction_df.loc[transaction_number, 'Amount'] = amount
        transaction_df.loc[transaction_number, 'Balance'] = atm.balance
        transaction_df.loc[transaction_number, 'Pin'] = atm.pin
      elif transaction == '3':
        to_account_number = input("Please input account number to transfer :")
        amount = int(input("Please input transfer amount :"))
        atm.transfer(to_account_number ,amount)
        transaction_df.loc[transaction_number, 'Transaction Number'] = transaction_number
        transaction_df.loc[transaction_number, 'Account Number'] = atm.account_number
        transaction_df.loc[transaction_number, 'Transaction'] = 'Transfer'
        transaction_df.loc[transaction_number, 'Amount'] = amount
        transaction_df.loc[transaction_number, 'Balance'] = atm.balance
        transaction_df.loc[transaction_number, 'Pin'] = atm.pin
      elif transaction == '4':
        atm.check_balance()
        transaction_df.loc[transaction_number, 'Transaction Number'] = transaction_number
        transaction_df.loc[transaction_number, 'Account Number'] = atm.account_number
        transaction_df.loc[transaction_number, 'Transaction'] = 'Balance check'
        transaction_df.loc[transaction_number, 'Amount'] = '-'
        transaction_df.loc[transaction_number, 'Balance'] = atm.balance
        transaction_df.loc[transaction_number, 'Pin'] = atm.pin
      elif transaction == '5':
        pin = int(input("Please input new pin :"))
        atm.change_pin(pin)
        transaction_df.loc[transaction_number, 'Transaction Number'] = transaction_number
        transaction_df.loc[transaction_number, 'Account Number'] = '-'
        transaction_df.loc[transaction_number, 'Transaction'] = 'Change Pin'
        transaction_df.loc[transaction_number, 'Amount'] = '-'
        transaction_df.loc[transaction_number, 'Balance'] = '-'
        transaction_df.loc[transaction_number, 'Pin'] = atm.pin
      else:
        transaction_number = transaction_number - 1
        print("You enter wrong key ,please try again!")

ATM_item()
