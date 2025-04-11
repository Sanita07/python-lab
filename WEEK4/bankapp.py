def credit(bal,transactions):
      amount=int(input("Enter amount to credit"))
      bal+=amount
      transactions.append(amount)
      print("Credited amount:",amount)
      return bal,transactions
def debit(bal,transactions):
        amount=int(input("Enter amount to debt:"))
        if amount<bal:
           bal-=amount
           transactions.append(-amount)
           print("Debited amount",amount)
           return bal,transactions
        else:   
            print("Invalid")
def check_balance():
        print("Current Balance",bal)
def last_5_transactions(transactions):
        for transaction in transactions:
            print(transaction)
bal=0
transactions=[]
while True:
    print("Bank Applications")
    print("1.Credited\n2.Debited\n3.Check balance\n4.Last 5 transactions\n5.Exit")
    choice=int(input("Enter your choice"))
    if choice==1:
        bal,tran=credit(bal,transactions)
    elif choice==2:
        bal,tran=debit(bal,transactions)
    elif choice==3:
        check_balance(bal)
    elif choice==4:
        last_5_transactions(transactions)
    elif choice==5:
        print("Thank you.....")
        break
    else:
       print("Wrong choices")
