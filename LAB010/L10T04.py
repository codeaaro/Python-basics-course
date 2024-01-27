tiedoston_nimi = "names.txt"
nimi_laskuri = {}

try:

    file = open(tiedoston_nimi, "r")
    nimet = file.readlines()

    for nimi in nimet:
        loydetty_nimi = nimi.strip()

        if loydetty_nimi in nimi_laskuri:
            nimi_laskuri[loydetty_nimi] += 1
        else:
            nimi_laskuri[loydetty_nimi] = 1

    pisin = max(nimet, key=len)

    print(f"Löydetty {len(nimi_laskuri)} nimeä:")
    print(f"pisin nimi on: {pisin}")


    
    file.close()
    
except FileNotFoundError:
    print("Tiedostoa 'names.txt' ei löydy")

