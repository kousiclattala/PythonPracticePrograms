
# * Write a Python program that accepts two integers from the user and then prints the sum, the difference, the product, the average.
# * the maximum (the larger of two integers) and the minimum (smaller of the two integers)

class MultipleFunctions:
    def __init__(self,num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        sum = self.num1 + self.num2
        print(f'The sum of {self.num1} and {self.num2} is {sum}')

    def difference(self):
        if self.num1 > self.num2:
            diff = self.num1 - self.num2
            print(f'The difference of {self.num1} and {self.num2} is {diff}')
        
        else:
            diff = self.num2 - self.num1
            print(f'The difference of {self.num1} and {self.num2} is {diff}')

    def product(self):
        prod = self.num1 * self.num2
        print(f'The product of {num1} and {num2} is {prod}')

    def average(self):
        avg = (self.num1 + self.num2) // 2
        print(f'The average of {num1} and {num2} is {avg}')

    def maximum(self):
        if self.num1 > self.num2:
            print(f'The maximum number is {self.num1}')
        else:
            print(f'The maximum number is {self.num2}')

    def minimum(self):
        if self.num1 < self.num2:
            print(f'The minimum number is {self.num1}')
        else:
            print(f'The minimum number is {self.num2}')

num1 = int(input('Enter number1: '))
num2 = int(input('Enter number2: '))
multiplefunctions = MultipleFunctions(num1,num2)
multiplefunctions.addition()
multiplefunctions.difference()
multiplefunctions.product()
multiplefunctions.average()
multiplefunctions.maximum()
multiplefunctions.minimum()