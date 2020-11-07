
# * Dave is 13,772,160 minutes old in age can you calculate his age in year.

# def year_in_age(ageM):
#     min_per_year = 60*24*365
#     count = 0
#     result = 0
#     while ageM > 0:
#         result = ageM - min_per_year
#         if result > 0:
#             count += 1

#         ageM = ageM - min_per_year

#     return count


# age_in_min = int(input('Enter the age in minutes: '))
# count = year_in_age(age_in_min)
# print(f'Dave is {count} years of age which is eqvialent to {age_in_min} in minutes')

# * Solution 2

min_per_year = 60*24*365
min = 13772160

age_in_year = int(min / min_per_year)
print(age_in_year)