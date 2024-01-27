class human:    
    Nimi = ""
    Ika = ""
    
    def __str__(self):
        return self.Nimi + " " + self.Ika + " "

human1 = human()
human1.Nimi = "Adam"
human1.Ika = "19"

human2 = human()
human2.Nimi = "Eva"
human2.Ika = "18"

print("Nimi:",human1.Nimi,"Ikä: ", human1.Ika)
print("Nimi:",human2.Nimi,"Ikä: ", human2.Ika)


    
