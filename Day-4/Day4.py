
# * Jack brought 400 hot dogs for the school picnic. if they were contained in packages of 8 hot dogs.
# * how many total packages did he but?. Create a python program without using \ or % operator.

def hotdogs(total_hotdogs, hotdogs_per_packet):
    print(f'Toatl packages he buy are {(total_hotdogs // hotdogs_per_packet)}')

total_hotdogs = 400
hotdogs_per_packet = 8

hotdogs(total_hotdogs, hotdogs_per_packet)