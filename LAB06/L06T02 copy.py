celsius = float(input("Syötä celsius aste: "))
fahrenheit = float(input("Syötä fahrenheit aste: "))


def celtofah():

    CTOF = (celsius*9/5)+32
    return(round(CTOF,1))

print(celtofah())

def fahtocel():

    FTOC = (fahrenheit-32)*5/9    
    return(round(FTOC,1))

print(fahtocel())
