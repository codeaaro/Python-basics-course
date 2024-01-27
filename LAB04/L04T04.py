
a = int(input("Anna numero väliltä 1-10: "))

if 1 <= a <=10:
    for i in range(1,a+1):
        nelio = i * i   
        print(f"Luvun {i} neliö:{nelio}")
else:
    print("Syötä luku väliltä 1-10")
    