import random
from collections import Counter


def ziehe_karte(kartenNr):
    gezogene = []
    for i in range(5):
        index = random.randint(0, len(kartenNr) - 1 - i)
        gezogeneZahl = kartenNr[index]

        # Zahl von der letzten noch nicht gezogenen Stelle holen
        last_index = len(kartenNr) - 1 - i
        kartenNr[index] = kartenNr[last_index]  # Tauschen
        kartenNr[last_index] = gezogeneZahl     # Gezogene Zahl ans Ende legen

        gezogene.append(gezogeneZahl)

    print("Gezogene Zahlen:", gezogene)
    print("Neue Kartenreihenfolge:", kartenNr)
    return gezogene


def karte_eig(gezogene):
    farben = []
    werte = []

    for i in gezogene:
        farbe = i%4
        farben.append(farbe)
    print("Farben",farben)

    for i in gezogene:
        wert = i%13
        werte.append(wert)
    print("Werte:", werte)

    return werte, farben

# --------------------------------------------------------------------------------------------
# pairs
# double pairs
# three of a kind
# four of a kind

def pairs(werte):

    werte_counts = Counter(werte)
    pairs = [werte for werte, count in werte_counts.items() if count >= 2]
    # schaut wie oft die einzelnen Farben vorkommen und wenn die 2 sind = ein pair
    # werden dann zu Liste hinzu un wenn pairs == 2 eann double pairs
    three_of_kind = [werte for werte, count in werte_counts.items() if count == 3]
    four_of_kind = [werte for werte, count in werte_counts.items() if count == 4]
    if len(four_of_kind) == 1:
        print(f"Four of a kind mit Wert {pairs}")
    elif len(three_of_kind) == 1:
        print(f"Three of a Kind mit Karte {pairs}")
    elif len(pairs) == 1:
        print(f"Pair mit Karte {pairs[0]}")
    elif len(pairs) >= 2:
        print(f"Double Pair mit Karte {pairs}")
    else:
        print("Kein Pair")

# -----------------------------------------------------------------------------------------
# Strasse

def strasse(werte):
    geordneteWerte = sorted(set(werte))  # doppelte Werte entfernen + sortieren
    countStrasse = 1  # zählt aufeinanderfolgende Karten

    for i in range(1, len(geordneteWerte)):
        if geordneteWerte[i] == geordneteWerte[i - 1] + 1:
            countStrasse += 1
            if countStrasse >= len(geordneteWerte):
                print("Wir haben eine Straße!")
                return True
    return False

#---------------------------------------------------------------------------------------------------------------

def flush(farben):

    flushY = 0
    farbe_counts = Counter(farben)
    flush = [farbe for farbe, count in farbe_counts.items() if count == len(farben)]

    if len(flush) == 1:
        print(f"Flush mit der Farbe {flush}" )
        flushY = 1
    return flushY



#------------------------------------------------------------------------------------------------------

#def straightflush(farben, werte):
 #   if flushy == 1 and strasse(werte):
  #      print("Straight Flush!")
   #     return True
    #else:
     #   print("Kein Straight Flush.")
      #  return False











if __name__ == "__main__":
    for i in range(1):

        kartenNr = list(range(1, 53))  # 1 bis 52
        gezogene = ziehe_karte(kartenNr)

        werte, farben = karte_eig(gezogene)

        pairs(werte)
        strasse(werte)
        flush(farben)
