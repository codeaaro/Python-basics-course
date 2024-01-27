tiedoston_nimi = "nimet.txt"
nimi_laskuri = {}


file = open(tiedoston_nimi, "r")
nimet = file.readlines()

for nimi in nimet:
    loydetty_nimi = nimi.strip()

    if loydetty_nimi in nimi_laskuri:
        nimi_laskuri[loydetty_nimi] += 1
    else:
        nimi_laskuri[loydetty_nimi] = 1

print(f"Löydetty {len(nimi_laskuri)} eri nimeä:")
for nimi, maara in nimi_laskuri.items():
    print(f"{nimi}: {maara} kertaa")

file.close()
