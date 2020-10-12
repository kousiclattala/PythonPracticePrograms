
# * Question 1
#  ? There was a teacher in a small town who loves coding and that he wants to create a program which prints out the whole 
# ? multiplication table of an entered number for his students. Can you help him to write a program in python?.

def multiplication_table(num):
    for i in range(1,21):
        result = num * i
        print(f'{num} * {i} = {result}')

num = int(input('Enter any Number: '))
multiplication_table(num)
