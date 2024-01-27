sukunimet = []
tiedosto = "sukunimet.txt"

file = open(tiedosto , "w")

while True:
    nimet = input("Syötä sukunimi: ")

    if nimet == "":
        break
    sukunimet.append(nimet)
    
    sukunimet.sort()

for nimet in sukunimet:
    file.write(nimet + "\n")
     
file.close()
print(tiedosto + " luotu onnistuneesti.")

