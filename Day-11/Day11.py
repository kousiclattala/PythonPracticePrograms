
# * Dan rented two movies to watch last night.
# * The first was 100 minutes long. The second 110 minutes long.
# * How many hours did it take for Dan to watch the two movies?

def total_hours(movieOneMin,movieTwoMin):
    minPerHour = 60
    totalHours = (movieOneMin + movieTwoMin) / minPerHour

    print(f'Total hours taken for Dan to watch the two movies is {totalHours} hours')

movieOneTimeInMin = 100
movieTwoTimeInMin = 110

total_hours(movieOneTimeInMin,movieTwoTimeInMin)