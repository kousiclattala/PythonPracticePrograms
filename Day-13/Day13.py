
# * 5th graders Kara and Rani both have lemonade stands. Kara sells her lemonade at 5 cents a glass and
# * Rani sells hers at 7 cents a glass. Kara sold 'k' number of glasses of lemonade today and rani 
# * sold 'r' number of glasses. Who made the most money and by what amount?
# * k and r are user-entered value.

def lemonadeMachine(kNumberOfGlasses,rNumberOfGlasses):
    karaChargePerGlass = 5
    raniChargePerGlass = 7

    karaSellingPrice = karaChargePerGlass * kNumberOfGlasses
    raniSellingPrice = raniChargePerGlass * rNumberOfGlasses

    if karaSellingPrice > raniSellingPrice:
        print(f'Kara made the most money and by amount of {karaSellingPrice - raniSellingPrice}')
    elif raniSellingPrice > karaSellingPrice:
        print(f'Rani made the most money and by amount of {raniSellingPrice - karaSellingPrice}')
    elif karaSellingPrice == raniSellingPrice:
        print('Kara and Rani\'s money is equal')


k = int(input('Number of glasses Kara sold: '))
r = int(input('Number of glasses Rani sold: '))

lemonadeMachine(k,r)