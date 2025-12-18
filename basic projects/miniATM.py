balance = 1000
while True:
    print("1.check balance")
    print("2.money deposit")
    print("3.money withdrawal")
    print("4.Exit")
    choice = int(input("Enter the option: "))
    if choice == 1:
        print("balance is:",balance)
    elif choice == 2:
        amount = int(input("Enter amount to deposit: "))
        balance = amount + balance
        print("Amount deposited successfully")
    elif choice == 3:
        money = int(input("Enter amount to withdraw: "))
        if balance >= money:
            print("amount withdrawn successfully")
            balance = balance - money
            print("current balance = ",balance)
        else:
            print("Insufficient balance")
    elif choice == 4:
        print("Thanks")
        break
    else :
        print("invalid")

