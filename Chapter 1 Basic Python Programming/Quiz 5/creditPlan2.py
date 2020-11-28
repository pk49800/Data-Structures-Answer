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
    
'''
sample:

Please input the purchase price: 100
month total_balance_owed interest_owed principal_owed payment balance_remaining
    1             113.65          1.14           3.36    4.50            109.15
    2             109.15          1.09           3.41    4.50            104.65
    3             104.65          1.05           3.45    4.50            100.15
    4             100.15          1.00           3.50    4.50             95.65
    5              95.65          0.96           3.54    4.50             91.15
    6              91.15          0.91           3.59    4.50             86.65
    7              86.65          0.87           3.63    4.50             82.15
    8              82.15          0.82           3.68    4.50             77.65
    9              77.65          0.78           3.72    4.50             73.15
   10              73.15          0.73           3.77    4.50             68.65
   11              68.65          0.69           3.81    4.50             64.15
   12              64.15          0.64           3.86    4.50             59.65
   13              59.65          0.60           3.90    4.50             55.15
   14              55.15          0.55           3.95    4.50             50.65
   15              50.65          0.51           3.99    4.50             46.15
   16              46.15          0.46           4.04    4.50             41.65
   17              41.65          0.42           4.08    4.50             37.15
   18              37.15          0.37           4.13    4.50             32.65
   19              32.65          0.33           4.17    4.50             28.15
   20              28.15          0.28           4.22    4.50             23.65
   21              23.65          0.24           4.26    4.50             19.15
   22              19.15          0.19           4.31    4.50             14.65
   23              14.65          0.15           4.35    4.50             10.15
   24              10.15          0.10           4.40    4.50              5.65
   25               5.65          0.06           4.44    4.50              1.15
   26               1.15          0.01           4.49    1.15              0.00
   '''
   
