class Account:
    saldo = ""
    
    def __init__(self, saldo):
        if saldo < 0:
            raise ValueError("Saldo ei voi olla negatiivinen.")
        self.saldo = saldo

    def add(self, money):
        if money < 0:
            raise ValueError("Lisättävän summan täytyy olla positiivinen.")
        self.saldo += money

    def withdraw(self, money):
        if money < 0:
            raise ValueError("Nostettavan summan täytyy olla positiivinen.")
        if money > self.saldo:
            raise ValueError("Ei riittävästi saldoa nostoon.")
        self.saldo -= money

pankkitili = Account(2000)

print(f"Pankkitilin saldo: {pankkitili.saldo} €")

try:
    lisattava_summa = float(input("Kuinka monta euroa lisätään saldoon? "))
    
    pankkitili.add(lisattava_summa)
    
    print(f"Pankkitilin saldo nyt: {pankkitili.saldo} €")

    nostettava_summa = float(input("Kuinka monta euroa haluat nostaa? "))
    
    pankkitili.withdraw(nostettava_summa)
    
    print(f"Pankkitilin saldo nyt: {pankkitili.saldo} €")

    uusi_nostettava_summa = float(input("Kuinka monta euroa haluat nostaa uudelleen? "))
    
    pankkitili.withdraw(uusi_nostettava_summa)

except ValueError as e:
    print(f"Virhe: {e}")