
# * The temperature recorded at 8 A.M. is "n"deg C,
# * What is the equivalent of this temperature in degrees Fahrenheit?
# * n is user enterd value.

# * Centigrade to Fahrenheit conversion formula ==> (0degC * (9/5))+32 = 32degF

def centigrade_to_fahrenheit(temp):
    fahrenheitTemp = (temp * (9/5)) + 32

    print(f'The equivalent temperature of {temp} deg Centigrade is {fahrenheitTemp} deg Fahrenheit')

temp = int(input('Enter the Temperature in Centigrade: '))
centigrade_to_fahrenheit(temp)