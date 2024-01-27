try:
    with open("C:/ayho.txt", "w", encoding="utf-8") as file:
        file.write("Tervetuloa Windowsin C-juureen!")

    print("Tiedosto 'ayho.txt' kirjoitettu onnistuneesti Windowsin C-juureen.")

except PermissionError:
    print("Ei oikeuksia kirjoittaa tiedostoa Windowsin C-juureen. Suorita ohjelma järjestelmänvalvojana.")

except Exception as e:
    print(f"Virhe: {e}")
