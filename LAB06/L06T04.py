summa = 0
points = []

for i in range(5):
    pisteet = int(input("Syötä hypyn pisteet (1-20): "))

    if pisteet < 1 or pisteet > 20:
        break

    try: 
        pisteet >= 1 and pisteet <= 20:
        points.append(pisteet)
        points.remove(min(points))
        points.remove(max(points))
        summa=summa+sum(points)        
        print(summa)
        print(points)

    except ValueError:
        print("Syötä kokonaisluku.")
