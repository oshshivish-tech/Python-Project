# Banking Program

def show_balance():
    print("*****************************")
    print(f"Your current balance is: $ {balance:.2f}")
    print("*****************************")  


def deposit():
    print("*****************************")
    amount = float(input("Enter the amount to deposit: "))
    print("*****************************")
    if amount<0:
        print("*****************************")
        print("Deposit amount must be positive.")
        print("*****************************")
        return 0
    else:
        return amount
    


def withdraw():
    print("*****************************")
    amount = float(input("Enter the amount to withdraw: "))
    print("*****************************")
    if amount > balance:
        print("*****************************")
        print("Insufficient funds.")
        print("*****************************")
        return 0
    elif amount<0:
        print("*****************************")
        print("Withdrawal amount must be positive.")
        print("*****************************")
        return 0
    else:
        return amount



balance=0
is_running=True

while is_running==True:
    print("*****************************")
    print("Welcome to the Banking Program")
    print("*****************************")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("*****************************")

    choice = input("Please choose an option (1-4): ")

    if choice == '1':
        show_balance()
    elif choice == '2':
         balance+=deposit()
    elif choice == '3':
         balance-=withdraw()
    elif choice == '4':
        is_running = False
        
    else:
        
        print("Invalid choice, please try again.")
        
    
    print("Thank you for using the Banking Program!")
    
    