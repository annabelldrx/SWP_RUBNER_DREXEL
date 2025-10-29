def ListComp():
    return [i * i for i in range(1, 11)]

def SetComp():
    namen = ["lukas", "lukas", "anna", "anna", "joana", "fitz", "fitz", "mario"]
    newName = {name for name in namen if name != "lukas"}
    return newName

def DicComp():
    inventar = {"äpfel": "3kg", "pringles": 12, "RedBull": 72}

    ergebnis = [
        "Genug Pringles" if inventar["pringles"] > 20
        else "Wenig Pringles" if inventar["pringles"] > 0
        else "Keine Pringles"
    ]

def DicAlphabet():
    alphabet = {chr(97 + i): i + 1 for i in range(26)}
    print(alphabet)

if __name__ == "__main__":
    print("Quadratzahlen:", ListComp())
    print("alle namen außer lukas", SetComp())
    print("Inventar ", DicComp())
    DicAlphabet()

