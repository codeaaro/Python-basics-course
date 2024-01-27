import random

tiedosto = "lotto.txt"

def lottorivi():
    luvut = []
    while len(luvut) < 7:
        r = random.randint(1, 40)
        if r not in luvut:
            luvut.append(r)
    luvut.sort()
    return luvut

def lottoRIVIT():
    riveja = int(input("Montako riviä haluat arpoa: "))
    rivit = []
    for i in range(riveja):
        rivi = lottorivi()
        rivit.append(rivi)
    return rivit

def tallenna_tiedostoon(rivit):
    with open(tiedosto, "w") as file:
        for rivi in rivit:
            file.write(" ".join(map(str, rivi)) + "\n")

rivit = lottoRIVIT()

for rivi in rivit:
    print(rivi)

tallenna_tiedostoon(rivit)
