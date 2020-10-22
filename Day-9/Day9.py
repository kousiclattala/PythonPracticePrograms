
# * Mr. Richard Tupper is purchasing gifts for his family. So far he has purchased the following:
# * 3 sweaters, each valued at $68
# * 1 computer game valued at $75
# * 2 bracelets, each valued at $43
# * Later, he returned one of the bracelets for a full refund and received a $10 rebate on the
# * computer game. What is the total cost of the gifts after the refund and rebate?
# * Calculation part of the program should be under three lines.

def totalCostOfGifts(s, c, b, cS, cC, cB):
    refundAmount = cB
    rebateAmount = 10

    totalCost = (s * cS) + (c * cC) + (b * cB) - refundAmount + rebateAmount

    print(totalCost)


sweaters = 3
computer = 1
bracelets = 2

costOfSweater,costOfComputer,costOfBracelet = 68,75,43

totalCostOfGifts(sweaters,computer,bracelets,costOfSweater,costOfComputer,costOfBracelet)