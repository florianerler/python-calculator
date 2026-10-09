print("Willkommen ")
while True:
    try:
        zahl1 = float(input("Erste Zahl: "))

        zahl2 = float(input("Zweite Zahl: "))
    except(ValueError):
        print("Die Eingabe muss eine Zahl sein. ")
        continue

    rechenart = input("Welche Rechenart? + oder - oder * oder / : ")

    if rechenart == "+":
        print("Ergebnis:", zahl1 + zahl2)
    elif rechenart == "-":
        print("Ergebnis:", zahl1 - zahl2)
    elif rechenart == "*":
        print("Ergebnis:", zahl1 * zahl2)
    elif rechenart == "/":
        if zahl2 == 0:
            print("Durch 0 kann man nicht teilen!")
        else:
            print("Ergebnis:", zahl1 / zahl2)
    else:
        print("Diese Rechenart kenne ich noch nicht!")
    

