arvosanat = [ ]
luku = 0

while True:
    luku = input("Syötä arvosana (0-5): ")

    if luku == "":
        break
    else:

        try:
            muunnettu = int(luku)
            if muunnettu < 0 or muunnettu > 5:
                print("Syötä arvosana väliltä (0-5)")
            else:
                arvosanat.append(muunnettu)
                numerot = ", ".join(luku)

        except ValueError:
            print("ei voia muttaa")

print(f"Arvosanoja syötettiin yhteensä: {len(arvosanat)}")
if len(arvosanat) == 0:
    print("keskiarvo 0")

else:

    keskiarvo = sum(arvosanat)/len(arvosanat)
    print(arvosanat)
    print(f"Arvosanojen keskiarvo {keskiarvo}")


