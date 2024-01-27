nimet = []


for i in range(10):
    nimi =  input("Anna 10 nimeä: ")
    if nimi == "":
        break
    nimet.append(nimi)

    
tyypit = ", ".join(nimet)

kaannettu_nimet = nimet[::-1]
kaannettu_tyypit = ", ".join(kaannettu_nimet)

print(tyypit)
print(kaannettu_tyypit)

