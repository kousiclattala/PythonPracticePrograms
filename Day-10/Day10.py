
# * Salesperson Rita drives 2,052 miles in 6 days. stopping at 2 towns each day.
# * How many kilometers does she average between stops?

def kilometersPerStop(tk,td,hp):
    kilometerPerDay = tk // td

    avgMiles = kilometerPerDay // hp

    kmPerMile = 1.60934

    avgKM = avgMiles * kmPerMile

    print(f'she drives average of {avgKM} km between every stop')

totalKilometersTravelled = 2052
totalDays = 6
haltingPlaces = 2

kilometersPerStop(totalKilometersTravelled,totalDays,haltingPlaces)