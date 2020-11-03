
# * Write a program to get the sum of "n" number?
# * Eg. sum of 123 is 6. "n" is user entered value.

def sumOfNumber(number):
    strippedNumber = list(number)
    result = 0
    for i in number:
        result += int(i)

    print(f'The sum of {number} is {result}')

number = input('Enter the number: ')
sumOfNumber(number)