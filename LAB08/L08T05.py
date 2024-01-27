import random

def lotto():

    luvut = []
    määrä = 0
    while len(luvut)  < 7:
        r = (random.randint(1,40))
        if r not in luvut:
            luvut.append(r)
        määrä+= 1
    luvut.sort()
    return luvut



print(lotto())