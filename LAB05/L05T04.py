kilometrit = 0
keskikulutus = 0
polttoaine = 0
kilometrit = int(input("Syötä ajetut kilometrit: "))
keskikulutus = float(input("Syötä keskikulutus: "))
polttoaine = kilometrit*(keskikulutus/100)

round(polttoaine,2)
def get_fuel():
    
    return(f"{round(polttoaine,1)}ltr")

print(get_fuel())