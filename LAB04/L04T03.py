summa = 0
lukujen_maara = 0

while True:
    syote = input("Anna kokonaisluku ")
    
    if syote == "":
        break
    
    try:
        luku = int(syote)
        summa += luku
        lukujen_maara += 1
    except ValueError:
        print("Syötä kokonaisluku.")

print(f"Annoit {lukujen_maara} lukua.")
print(f"Lukujen summa on {summa}.")