
# * Find the square of a number without using multiplication and division operator.

def squareOfNumber(n):
    number = n
    totalSquare = 0
    while number > 0:
        totalSquare += n

        number -= 1

    print(f'The square of number {n} is {totalSquare}')

n = 8
squareOfNumber(n)