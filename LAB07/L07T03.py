class cat:
    nimi = ""
    vari = ""
    miau = "Meoooooow!"
    def __str__(self):
        return self.nimi + " " + self.vari + " "
    def cat_say(self):
        return self.miau

kissa1 = cat()
kissa1.nimi = "Kit"
kissa1.vari = "black"

kissa2 = cat()
kissa2.nimi = "Kat"
kissa2.vari = "white"

print(f"{kissa1.nimi}, color: {kissa1.vari}")
print(f"{kissa2.nimi}, color: {kissa2.vari}")
print(f"{kissa1.nimi} says: {kissa1.miau}")
print(f"{kissa2.nimi} says: {kissa2.miau}")