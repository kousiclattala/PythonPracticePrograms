
# * Write a Python program to input centimetre and convert to inch, metre and kilometre.

# * centimetre to inch formula ==> divide value by 2.54
# * centimetre to metre formula ==> divide value by 100
# * centietre to kilometer formula ==> divide value by 100000

def length_conversion(centiMetre):
    centiMetre_to_inch = centiMetre / 2.54

    centiMetre_to_metre = centiMetre / 100

    centiMetre_to_kilometre = centiMetre / 100000

    print(f'{centiMetre} centimetre is equal to {centiMetre_to_inch} inches')

    print(f'{centiMetre} centimetre is equal to {centiMetre_to_metre} metres')

    print(f'{centiMetre} centimetre is equal to {centiMetre_to_kilometre} kilometres')


centiMetre = int(input('Enter the centimetre value: '))
length_conversion(centiMetre)