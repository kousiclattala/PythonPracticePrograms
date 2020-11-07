
# * Write a Python program to takes the user for a distance (in meters) and the time was taken (as three numbers; hours, minutes and seconds)
# * and display the speed, in miles per hour.

distance = float(input('Enter the distance in meters: '))
hr = float(input('Input in hours: '))
min = float(input('Input in minutes: '))
sec = float(input('Input in seconds: '))

timeInSeconds = (hr * 3600) + (min * 60) + sec
kilometrePerHour = (distance / 1000.0) / (timeInSeconds / 3600.0)

milesPerHour = kilometrePerHour / 1.609

print(f'The Speed in miles per hour is {milesPerHour}')



