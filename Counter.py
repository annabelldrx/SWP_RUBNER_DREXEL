import time
from functools import wraps


def timer_decorator(func):
    @wraps(func) 
    def wrapper(*args, **kwargs):
        start_zeit = time.perf_counter()  
        ergebnis = func(*args, **kwargs)  
        end_zeit = time.perf_counter() 

        dauer = end_zeit - start_zeit
        print(f"Funktion '{func.__name__}' hat {dauer:.6f} Sekunden gebraucht.")

        return ergebnis  


    return wrapper
