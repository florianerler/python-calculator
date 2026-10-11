import math
print("=" * 100)
print("				PYTHON CALCULATOR v1.4")
print("-" * 100)
print("verfügbare Rechenarten: +, -, *, /, **")
print("shortcuts: s zum beenden, p oder pi für Kreiszahl, e oder euler für euler´sche Zahl")
print("=" * 100)
while True:
    try:
        eingabe1 = (input("Erste Zahl: "))
        eingabe1 = eingabe1.lower()
        if eingabe1 == "s":
            break
        if eingabe1 == "pi" or eingabe1 == "p":
            eingabe1 =(math.pi)
        if eingabe1 == "euler" or eingabe1 =="e":
            eingabe1 =(math.e)
        zahl1 = float(eingabe1)
        eingabe2 = (input("Zweite Zahl: "))
        eingabe2 = eingabe2.lower()
        if eingabe2 == "s":
            break
        if eingabe2 == "pi" or eingabe2 == "p":
            eingabe2 =(math.pi)
        if eingabe2 == "euler" or eingabe2 == "e":
            eingabe2 =(math.e)
        zahl2 = float(eingabe2)
    except(ValueError):
        print("Die Eingabe muss eine Zahl sein. ")
        continue

    rechenart = input("Welche Rechenart? + oder - oder * oder / oder ** oder 's' zum beenden: ")
    rechenart = rechenart.lower()
    if rechenart == "+" or rechenart == "plus":
        print("Ergebnis:", zahl1 + zahl2)
    elif rechenart == "-" or rechenart == "minus":
        print("Ergebnis:", zahl1 - zahl2)
    elif rechenart == "*" or rechenart == "mal":
        print("Ergebnis:", zahl1 * zahl2)
    elif rechenart == "/" or rechenart == "dividiert":
        if zahl2 == 0:
            print("Durch 0 kann man nicht teilen!")
        else:
            print("Ergebnis:", zahl1 / zahl2)
    elif rechenart == "**" or rechenart == "hoch":
        print("Ergebnis:", zahl1 ** zahl2)
    elif rechenart == "s":
        break
    else:
        print("Diese Rechenart kenne ich noch nicht!")
    
print("Ciao baba!" )
    

