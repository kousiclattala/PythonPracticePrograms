
# * Write a Python Program to convert Integer Values into Binary

def integerToBinary(num):
    num = int(num)
    if num > 0:
        binary = []
        while num > 0:
            r = num // 2
            rem = num % 2

            binary.append(rem)

            num = r

        print('The Binary number of Integer Value', num ,'is')

        binary.reverse()
        for i in binary:
            print(i,end='')

    else:
        print('Enter the Number greater than 0')


num = input('Enter the Integer Number: ')
integerToBinary(num)