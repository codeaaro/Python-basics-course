rekisterinumerot = []

while True:
    numero = input("Syötä rekisterinumero: ")

    if numero == "":
        break
    rekisterinumerot.append(numero)

    continue

rekisterinumerot.sort()
numerot = ", ".join(rekisterinumerot)

print(numerot)