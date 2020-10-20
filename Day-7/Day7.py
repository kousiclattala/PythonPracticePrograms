
# * The city's bus system carries 1,200,000 people,each day
# * How many people does the bus system carry each year? (1 year = 365 days)
# * solve without using *, /operator, bitwise operator or loop.
import sys

sys.setrecursionlimit(10**6)
# print(sys.getrecursionlimit())

def busSystem_carries(numberOfPeopleEachDay,daysInYear,totalPeople):
    
    try:
        if daysInYear > 0:
            totalPeople = totalPeople + numberOfPeopleEachDay
    except Exception as ex:
        print(ex)

    if daysInYear == 0:
        print(totalPeople)  

    return busSystem_carries(numberOfPeopleEachDay, daysInYear-1,totalPeople)



numberOfPeopleEachDay = 1200000
daysInYear = 365
totalPeople = 0
busSystem_carries(numberOfPeopleEachDay,daysInYear,totalPeople)