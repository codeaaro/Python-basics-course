tuuma = 2.54

tuumamitta = float(input("Syötä tuumamäärä: "))

def show_cm():
    
    sentit = tuumamitta*tuuma
    return(f"{tuumamitta} tuumaa on {round(sentit,2)} cm")

print(show_cm())