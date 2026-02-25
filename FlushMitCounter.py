from collections import Counter

from Counter import timer_decorator


@timer_decorator
def flush(farben):
    farbe_counts = Counter(farben)
    for farbe, count in farbe_counts.items():
        if count >= 5:
            return farbe
    return None
if __name__ == "__main__":
    test_hand = ['H', 'H', 'S', 'H', 'D', 'H', 'H']
    ergebnis = flush(test_hand)
    print(f"Gefundener Flush: {ergebnis}")