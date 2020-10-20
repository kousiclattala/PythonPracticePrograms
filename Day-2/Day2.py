
# * can you help Alex to print double sided stair-case pattern in python.
'''         * *
            * *
          * * * *
          * * * *
        * * * * * *
        * * * * * *
      * * * * * * * *
      * * * * * * * *
    * * * * * * * * * *
    * * * * * * * * * *
'''

n = 5
starCount = 0
for i in range(n):
    step = 0
    while step < 2:
        for space in range((n-i)*2):
            print(' ', end='')

        for j in range(starCount+2):
            print('*', end='')
            print(' ', end='')

        step += 1
        print('')

    starCount += 2
