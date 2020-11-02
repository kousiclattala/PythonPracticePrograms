
# * Lucille spent 12% of her weekly earnings on DVDs and deposited the rest into her savings
# * account. if she spent $42 on DVDs, How much did she deposit into her savings account?

# * formula is Y/P% = X ==> Y/(P/100) = X
# * X is total earnings, Y is amount spent, P% is percent amount spent

def lucilleEarnings(P,Y):
    X = Y//(P/100)

    totalSavingsAmount =  X - Y

    print(f'The total amount lucille deposited in her savings account is {totalSavingsAmount}')

percentSpent = 12
amountSpent = 42

lucilleEarnings(percentSpent,amountSpent)