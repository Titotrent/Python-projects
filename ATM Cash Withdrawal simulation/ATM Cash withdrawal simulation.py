
def simulate_withdrawal(balance):

    while True:
        name=input('What is your name(or enter 0 to exit):')
        if name=='0':
            print('Exiting...')
            break

        print(f'Hello {name.strip()}')
        print('\nPress 0 to exit at any time')

        while True:
            try:
                withdrawal_amt=int(input("\nEnter withdrawal amount: "))
            except ValueError:
                print('Invalid input(enter a number)')
                continue


            if withdrawal_amt==0:
               print('Exiting session...')
               return balance
            elif withdrawal_amt<0:
                print('Invalid input(You cannot withdraw negative amounts)')
                continue
            elif withdrawal_amt%100!=0:
                print('Invalid input format(Withdrawal amount must be a multiple of 100)')
                continue
            elif withdrawal_amt>balance:
                print('Insufficient amount')
                continue


            balance=balance -withdrawal_amt
            print(f'Your balance is KES: {balance}')
                

customer1=simulate_withdrawal(80000)
print(f'Customer1 balance is {customer1}')