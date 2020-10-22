
# * on a certain day, the nurses at a hospital worked the following number of hours:
# * Nurse Howard worked for 8 hours.
# * Nurse pease worked for 10 hours.
# * Nurse grace worked for 8 hours.
# * Nurse McCarthy worked for 7 hours.
# * Nurse Murphy worked for 12 hours.
# * what is the average number of hours worked per nurse on this day?. Average should be as a float value.

def avg_number_hours(nurses):
    result = 0
    avg_hours = 0

    for value in nurses.values():
        result += value

    avg_hours = result / len(nurses)

    print(f'The average total number of hours nurses worked are {avg_hours}')

nurses = {
    "Howard":8,
    "pease": 10,
    "grace": 8,
    "McCarthy": 7,
    "Murphy": 12
}

avg_number_hours(nurses)