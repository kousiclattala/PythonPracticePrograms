
# * Lefty keeps track of the length of each fish that he catches. 
# * Below are the lengths in inches of the fish that he caught one day:
# * 12, 13, 8, 10, 17. What is the largest fish length that lefty caught that day?
# * Solve without using conditional statements and the loop.

def largest_num(nums):
    nums.sort()
    numsLength = len(nums)

    largestNum = nums[numsLength-1]

    print(f'The largest fish length that lefty caught that day is {largestNum}')

nums = [12, 13, 8, 10, 17]
largest_num(nums)

