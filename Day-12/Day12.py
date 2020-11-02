
# * The number of red blood corpuscles in one the cubic millimetre is about 5,000,000 
# * and the number of white blood corpuscles in one cubic the millimetre is about 8,000.
# * What, is the ratio of white blood corpuscles to red blood corpuscles?
# * Aspect Ratio should be as an int value.

def greatestCommonFactor(rbc,wbc):
    if rbc == 0:
        return wbc
    else:
        return greatestCommonFactor(wbc % rbc,rbc)

redbloodCorpuscles = 5000000
whitebloodCorpuscles = 8000

factor = greatestCommonFactor(redbloodCorpuscles,whitebloodCorpuscles)

whiteRatio = int(whitebloodCorpuscles / factor)
redRatio = int (redbloodCorpuscles / factor)

print(f'Aspect ratio {whiteRatio}:{redRatio}')