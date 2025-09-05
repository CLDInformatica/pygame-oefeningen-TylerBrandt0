# Gegeven is een functie met 2 argumenten:
#   - getal1
#   - getal2

# Return de grootste van deze 2 getallen.
# Voer de functie daarna uit met verschillende waarden en print de uitkomst

def grootste(getal1, getal2):
    if getal1 > getal2:
        return getal1
    elif getal2 > getal1:
        return getal2
    
print(grootste(2, 3))
print(grootste(2399, 2342))
print(grootste(1, 0))
print(grootste(10000, 10001))