from datetime import date

nykyinen_vuosi = date.today().year

try:
    syntymavuosi = int(input("Syötä syntymävuotesi: "))    

    if syntymavuosi <=0 or syntymavuosi>date.today().year:
        print("Virheellinen syntymävuosi.")
    else:
        ika = nykyinen_vuosi - syntymavuosi
        print(f"Olet nyt {ika} vuotta vanha.")
except ValueError:
    print("Virheellinen syöte. Syötä vuosiluku numeroina.")
    

def kerro3(age):

    if age < 1:
        return("baby")
    elif age < 13:
        return("child")
    elif age < 13 or age < 19:
        return("teen")
    elif age < 20 or age < 65:
        return("adult")
    else:
        return("senior")

print(kerro3(ika))
