
vuosiluku = int(input("syötä vuosiluku: "))

try:
    if (vuosiluku % 4 == 0 and vuosiluku % 100 != 0) or (vuosiluku % 400 == 0):
        print(f"{vuosiluku} on karkausvuosi")
    else:
        print(f"{vuosiluku} ei ole karkausvuosi")

except ValueError:
    print("syötä vuosiluku")