kilometrit = int(input("Syötä ajetut kilometrit: "))
keskikulutus = float(input("Syötä keskikulutus: "))
litrahinta = float(input("Syötä polttoaineen hinta: "))
kustannus = kilometrit*(keskikulutus/100)*litrahinta

def get_cost():

    return(f"{round(kustannus,2)}€")

print(get_cost())