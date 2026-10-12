import math
def begruessung():
    print("=" * 100)
    print("				PYTHON CALCULATOR v1.5")
    print("-" * 100)
    print("verfügbare Rechenarten: +, -, *, /, **")
    print("shortcuts: a für Anleitung, s zum beenden, p oder pi für Kreiszahl, e oder euler für euler´sche Zahl")
    print("=" * 100)

def anleitung():
    print("-" * 100)
    print("verfügbare Rechenarten: +, -, *, /, **")
    print("shortcuts: s zum beenden, p oder pi für Kreiszahl, e oder euler für euler´sche Zahl")
    print("-" * 100)
    
def eingabe():
    while True:
        try:
            eingabe = (input("Zahl: "))
            eingabe = eingabe.strip().lower()
            if eingabe == "s":
                return "s"
            if eingabe == "pi" or eingabe == "p":
                eingabe =(math.pi)
            if eingabe == "euler" or eingabe =="e":
                eingabe =(math.e)
            if eingabe == "anleitung" or eingabe =="a":
                anleitung()
                continue
            return float(eingabe)
        except(ValueError):
            print("Die Eingabe muss eine Zahl sein. ")
            continue
        
def berechnen(zahl1, zahl2):
    while True:
            rechenart = input("Welche Rechenart? ").strip().lower()
            if rechenart == "+" or rechenart == "plus":
                print("Ergebnis:", zahl1 + zahl2)
                return
            elif rechenart == "-" or rechenart == "minus":
                print("Ergebnis:", zahl1 - zahl2)
                return
            elif rechenart == "*" or rechenart == "mal":
                print("Ergebnis:", zahl1 * zahl2)
                return
            elif rechenart == "/" or rechenart == "dividiert":
                if zahl2 == 0:
                    print("Durch 0 kann man nicht teilen!")
                else:
                    print("Ergebnis:", zahl1 / zahl2)
                    return
            elif rechenart == "**" or rechenart == "hoch":
                print("Ergebnis:", zahl1 ** zahl2)
                return
            elif rechenart == "s":
                return "s"
            elif rechenart == "anleitung" or rechenart =="a":
                anleitung()
                continue
            else: print("Diese Rechenart kenne ich noch nicht!")
    
    
begruessung()
while True:
        zahl1 = eingabe()
        if zahl1 == "s":
            break
        zahl2 = eingabe()
        if zahl2 == "s":
            break
        antwort = berechnen(zahl1, zahl2)
        if antwort == "s":
            break
print("Ciao baba!" )
    

