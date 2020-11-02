
# * How many ways can four students Ram, Anuj, Deepak and Ravi line up in a line,if the order matters?
# * Print all the possible combination.

def possible_combinations(totalNoOfStudents):
    n = len(totalNoOfStudents)
    noOfPeopleTakenAtATime = n
    noOfWays = n**noOfPeopleTakenAtATime

    while noOfWays > 0:
        for i in range(n):
            temp = totalNoOfStudents[i]
            totalNoOfStudents[i] = totalNoOfStudents[n-1]
            totalNoOfStudents[n-1] = temp
        
        print(totalNoOfStudents,end='')
        print()
        noOfWays -= 1



totalNoOfStudents = ['Ram','Anuj','Deepak','Ravi']

possible_combinations(totalNoOfStudents)





