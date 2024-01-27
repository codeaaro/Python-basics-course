
print("Valitse yksikkö: 1. Celsius 2. Fahrenheit")

for i in range(1,2):
    yksikkö = int(input("syötä valitsemasi yksikön numero: "))
    aste = float(input("syötä lämpötila: "))

CTOF = (aste*9/5)+32
FTOC = (aste-32)*5/9

if yksikkö == 1:
    def celtofah():

        return(round(CTOF,2))

    print(celtofah())

else:
    def fahtocel():

        return(round(FTOC,1))
    
    print(fahtocel())