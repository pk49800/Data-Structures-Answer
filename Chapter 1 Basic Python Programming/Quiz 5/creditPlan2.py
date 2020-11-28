"""
This program display a table with appropriate headers
of a payment schedule for the lifetime of the loan.
"""
def totalInterest(monthly_rate, monthly_payment, balance_remaining):
    '''get the total month and total interest for the plan'''
    month = 1
    total_interest = 0.0
    while balance_remaining > monthly_payment:
        month = month + 1
        interest = balance_remaining * monthly_rate
        total_interest += interest
        balance_remaining = balance_remaining + interest
        balance_remaining = balance_remaining - monthly_payment
    return month, round(total_interest, 2)

def printTitle():
        '''Print title'''
        print(
            'month',
            'total_balance_owed',
            'interest_owed',
            'principal_owed',
            'payment',
            'balance_remaining'
            )

def printRow(*col):
    '''Print rows'''
    string = '%5d %18.2f %13.2f %14.2f %7.2f %17.2f'%col
    print(string)



def printSchedule(apr, purchasePrice):
    '''Print purchase plan'''
    monthly_rate = apr / 12
    down_payment = purchasePrice * 0.1
    monthly_payment = (purchasePrice - down_payment) * 0.05
    month, total_interest = totalInterest(monthly_rate, monthly_payment, purchasePrice)
    balance_remaining = purchasePrice + total_interest
    printTitle()
    for month in range(1, month + 1):
        interest_owed = monthly_rate * balance_remaining
        payment = monthly_payment if monthly_payment < balance_remaining else balance_remaining
        principal_owed = monthly_payment - interest_owed
        balance_remaining = balance_remaining - payment
        total_balance_owed = balance_remaining + payment
        printRow(month,
                total_balance_owed,
                interest_owed,
                principal_owed,
                payment,
                balance_remaining
                )

def main():
    apr = 0.12
    # u can add try-except ValueError
    purchasePrice = float(input("Please input the purchase price:"))
    printSchedule(apr, purchasePrice)
    
if __name__ == "__main__":
    main()   
