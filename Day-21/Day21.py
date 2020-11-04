
# * Write a program that for a given hour and minutes values calculates an angle in degree between the hour
# * and the minute hands. Check whether the minute hand overlapping the hour hand at a given time.

# * Note that clock is a circle which is of 360deg, that means each angle represents an angle
# * the separation between them is 360/12 = 30. And at 2:00, the minute hand is on the 12 and the hour hand is on the 2. 
# * The correct answer is 2 * 30 = 60 degrees.

# * solution 1

# def findClockAngle(hH, mH):
#     angleSeperation = 360 // 12

#     if mH == 0:
#         angle = hH * angleSeperation

#         print(f'The angle between hour hand and minute hand is {angle}.')

#     elif (hH * 5) == mH or hH == 12:
#         print(f'The hour hand and minute hand are overlapping on eachother.')

#     else:
#         angle = ((11/2)*mH) - (30*hH)

#         if angle < 0:
#             angle = 360 + angle
#             print(f'The angle between hour hand and minute hand is {angle}') 
        
#         else:
#             print(f'The angle between hour hand and minute hand is {angle}') 


# hourhand = int(input('Enter the hours: '))
# minuteHand = int(input('Enter the minutes: '))
# findClockAngle(hourhand,minuteHand)

# * solution 2  
# * Formula: angle = 0.5 * ((60 * hH) - (11 * mH))
# * here 0.5 is hour hand moves 0.5deg per minute (360/12) = 30deg per minute == 30/60 = 0.5 deg per minute.
# * here 11 is by substracting minute while taking common. 
# * for further details just google as clock angle problem and look at wikipedia page.

def findAngle(hH, mH):
    angleSeperation = 360 // 12

    if mH == 0:
        angle = hH * angleSeperation

        print(f'The angle between hour hand and minute hand is {angle}.')

    elif (hH * 5) == mH or hH == 12:
        print(f'The hour hand and minute hand are overlapping on eachother.')

    else:
        angle = 0.5 * ((60 * hH) - (11 * mH))

        if angle > 180:
            angle = 360 - angle

            print(f'The angle between hour hand and minute hand is {angle}.')
        else:
            print(f'The angle between hour hand and minute hand is {angle}.')

hourHand = int(input('Enter the hours: '))
minuteHand = int(input('Enter the minutes: ')) 
findAngle(hourHand,minuteHand)
        