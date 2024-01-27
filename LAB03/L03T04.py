a = int(input("Pisteet: "))

if a>=0 and a<=1 :
    print(f"Arvosana 0 ")
elif a>=2 and a<=3 :
    print(f"Arvosana 1")
elif a>=4 and a<=5 :
    print(f"Arvosana 2")
elif a>=6 and a<=7 :
    print(f"Arvosana 3")
elif a>=8 and a<=9 :
    print(f"Arvosana 4")
elif a>=10 and a<=12 :
    print(f"Arvosana 5")

else:
    print("Virheellinen pistemäärä")