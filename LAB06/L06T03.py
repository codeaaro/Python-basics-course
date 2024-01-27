oppilaat = []


while True:
    nimi = input("Anna oppilaan nimi: ")

    if nimi == "":
        break
    oppilaat.append(nimi)

    continue
maara = len(oppilaat)
nimet = ", ".join(oppilaat)
print(f"Oppilaita: {maara}")
print(nimet)
    













