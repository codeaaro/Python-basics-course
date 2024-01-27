

while True:
    etunimi = input("Anna etunimi: ")
    sukunimi = input("Anna sukunimi: ")
 
    eka = etunimi[0]
    pituus = len(etunimi)
    kaanteinen = sukunimi [::-1]
    print(f"{pituus*eka} {kaanteinen}")
    break