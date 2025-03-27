def show_balance(balance):
    print(f'Your balance is £{balance:.2f}')

def deposit():
    amount = float(input('Enter an amount to be deposited: '))
    if amount < 0:
        print('That\'s not a valid amount.')
        return 0
    return amount

def withdraw(balance):
    amount = float(input('Enter the amount to withdraw: '))
    if amount > balance:
        print('Insufficient funds.')
        return 0
    elif amount < 0:
        print('Amount must be greater than 0.')
        return 0
    return amount

def display_menu():
    print(f'\n{"*" * 3} Secure Bank {"*" * 3}')
    print('1. Show Balance')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Exit')

def main():
    balance = 0  # Initial balance
    is_running = True

    while is_running:
        display_menu()
        choice = input('Enter your choice (1-4): ')

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()  # Fixed function call
        elif choice == '3':
            balance -= withdraw(balance)  # Fixed function call
        elif choice == '4':
            q = input('Press y to exit: ')
            if q.lower() == 'y':  # Make it case insensitive
                print('Exiting program...')
                is_running = False
        else:
            print('Invalid input. Please enter a number between 1 and 4.')

    print('Thank you! Have a nice day!')

if __name__ == '__main__':
    main()
