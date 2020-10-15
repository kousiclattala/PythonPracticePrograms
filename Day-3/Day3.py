
# * A chef was cooking something special which required exact 200ml water but he doesn't have 200ml cup
# * he has a 500ml cup and a 300ml cup but that dish required exactly 200ml water. Can you solve this problem.

def exact_water(req_water):
    cup1 = 500
    cup2 = 300

    print(f'{cup1 - cup2}')

req_water = 200
exact_water(req_water)