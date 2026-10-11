print("=" * 40)
print("	PYTHON CALCULATOR v1.3")
print("-" * 40)
print("Grundrechenarten: +, -, *, /")
print("Zum Beenden 's' eingeben.")
print("=" * 40)

while True:
    try:
        eingabe1 = (input("Erste Zahl: "))
        if eingabe1 == "s":
            break
        zahl1 = float(eingabe1)
        eingabe2 = (input("Zweite Zahl: "))
        if eingabe2 == "s":
            break
        zahl2 = float(eingabe2)
    except(ValueError):
        print("Die Eingabe muss eine Zahl sein. ")
        continue

    rechenart = input("Welche Rechenart? + oder - oder * oder / oder 's' zum beenden: ")

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
    elif rechenart == "s":
        break
    else:
        print("Diese Rechenart kenne ich noch nicht!")
    
print("Auf Wiedersehen!" )
    

