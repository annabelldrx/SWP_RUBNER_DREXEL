import time
from functools import wraps


def timer_decorator(func):
    @wraps(func)  # Behält den Namen und die Docstrings der Originalfunktion bei
    def wrapper(*args, **kwargs):
        start_zeit = time.perf_counter()  # Startzeit vor dem Aufruf
        ergebnis = func(*args, **kwargs)  # Die eigentliche Funktion ausführen
        end_zeit = time.perf_counter()  # Endzeit danach

        dauer = end_zeit - start_zeit
        print(f"Funktion '{func.__name__}' hat {dauer:.6f} Sekunden gebraucht.")

        return ergebnis  # Das Originalergebnis zurückgeben

    return wrapper