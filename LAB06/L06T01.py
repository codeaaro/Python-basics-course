syöte = int(input("Syötä sekuntit: "))
seconds = syöte
hour = seconds // 3600
seconds = seconds % (24 * 3600)
seconds %= 3600
minutes = seconds // 60
seconds %= 60

def showtime():
     
    return "%d:%02d:%02d" % (hour, minutes, seconds)

print(showtime())