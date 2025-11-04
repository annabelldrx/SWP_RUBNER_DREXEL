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


    return gezogene


def karte_eig(gezogene):
    farben = []
    werte = []

    for i in gezogene:
        farbe = i%4
        farben.append(farbe)


    for i in gezogene:
        wert = i%13
        werte.append(wert)


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
        return "four_of_a_kind"
    elif len(three_of_kind) == 1 and len(pairs) == 1:
        return "full_house"
    elif len(three_of_kind) == 1:
        return "three_of_a_kind"
    elif len(pairs) >= 2:
        return "two_pair"
    elif len(pairs) == 1:
        return "pair"
    else:
        return None


# -----------------------------------------------------------------------------------------
# Strasse



def strasse(werte):
    geordneteWerte = sorted(set(werte))
    countStrasse = 1
    for i in range(1, len(geordneteWerte)):
        if geordneteWerte[i] == geordneteWerte[i - 1] + 1:
            countStrasse += 1
            if countStrasse >= 5:
                return True
        else:
            countStrasse = 1
    return False

def flush(farben):
    farbe_counts = Counter(farben)
    for farbe, count in farbe_counts.items():
        if count >= 5:
            return farbe
    return None

#-----------------------------------------------------------------------------------------------------------

def straightflush(werte, farben):

    if strasse(werte) and flush(farben):
        return True
    else:
        return False

def fullhouse(werte):
    counts = Counter(werte)
    three_of_kind = [wert for wert, count in counts.items() if count == 3]
    pairs = [wert for wert, count in counts.items() if count == 2]

    if (len(three_of_kind) == 1) and (len(pairs) == 1):
        return True
    else:
        return False

def royalflush(werte, farben):
    royal_values = {10, 11, 12, 13, 14}
    if set(werte) == royal_values:
        return True
    else:
        return False

def statistik(durchlaeufe=100000):

    stats = {
        "pair": 0,
        "two_pair": 0,
        "three_of_a_kind": 0,
        "straight": 0,
        "flush": 0,
        "full_house": 0,
        "four_of_a_kind": 0,
        "straight_flush": 0,
        "royal_flush": 0
    }

    for _ in range(durchlaeufe):
        kartenNr = list(range(1, 53))
        gezogene = ziehe_karte(kartenNr)
        werte, farben = karte_eig(gezogene)

        hand = pairs(werte)

        # Paare, Drillinge usw.
        if hand in stats:
            stats[hand] += 1

        # Straße
        if strasse(werte):
            stats["straight"] += 1

        # Flush
        if flush(farben):
            stats["flush"] += 1

        # Straight Flush
        if straightflush(werte, farben):
            stats["straight_flush"] += 1

        # Royal Flush
        if royalflush(werte, farben):
            stats["royal_flush"] += 1


    # Statistik anzeigen
    print("\n=== Poker Statistik ===")
    for hand, count in stats.items():
        print(f"{hand:18}: {count} ({count / durchlaeufe * 100:.6f}%)")

    return stats


# ----------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    statistik(100000)