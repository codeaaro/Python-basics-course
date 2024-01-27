luvut = []
tiedosto = "luvut.txt"

file = open(tiedosto, "w")

while True:
    syote = input("Syötä kokonaisluku: ")
    
    if syote == "":
        break
    try:
        luku = int(syote)
        luvut.append(luku)
    except ValueError:
        print("Syötä kokonaisluku")
    
yhteensa = len(luvut)
    
for luku in luvut:
    file.write(str(luku))

file.close()

file = open(tiedosto, "r")
print(yhteensa)
file.close()