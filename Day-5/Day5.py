
# * During the last week of track training.
# * Shoshanna achieves the following times in sec-rounds; 66,57,54,53,64,52, and 59.
# * found her best score use bubble sort.

sec_rounds = [66,57,54,53,64,52,59]

n = len(sec_rounds)

for i in range(n):
    for j in range(n-i-1):
        if sec_rounds[j] > sec_rounds[j+1]:
            sec_rounds[j],sec_rounds[j+1] = sec_rounds[j+1],sec_rounds[j]

        
print(f'Her best score is {sec_rounds[0]}')