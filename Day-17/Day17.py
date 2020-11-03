
# * There are 10 students in a class some students names are same to other students,
# * print the names that occur more than one time. All names should be in a single string.
# * Eg. str = "Aman Ankit Deepak Arjun Nakul Amit Priyanshu Vansh Rajat Sagar";

def studentWithCommonNames(studentList):
    commonNames = []
    n = len(studentList)
    for i in range(n):
        for j in range(i+1,n):
            if studentList[i] == studentList[j]:
                commonNames.append(studentList[i])
    # * converting a list to string using join and map method.
    namesList = ' '.join(map(str,commonNames))
    print(f'{namesList}')

studentList = input('Enter the Student Names with space seperated: ').split(' ')
studentWithCommonNames(studentList)