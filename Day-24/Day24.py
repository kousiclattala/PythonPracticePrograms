
# * If Julius has j books and Nancy has n. How many books do they have altogether?
# * Convert and print as an Roman number. j and n are user entered value.
# * roman_dict = {1: 'I', 4:'IV', 5:'V', 9:'IX', 10:'X', 40:'XL', 50:'L', 90:'XC', 100:'C', 400: 'CD', 500:'D', 900:'CM', 1000:'M'}

def decimalToRomanNumber(num):
    nums = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]

    symb = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']

    i = 12

    while num:
        div = num // nums[i]
        num = num % nums[i]

        while div:
            print(symb[i],end='')
            div -= 1
        
        i -= 1

j = int(input('Enter the num of books julius had: '))
n = int(input('Enter the num of books nancy had: '))
num = j + n

decimalToRomanNumber(num)