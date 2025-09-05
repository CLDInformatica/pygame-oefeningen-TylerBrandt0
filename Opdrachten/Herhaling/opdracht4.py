# Bekijk de voorbeelden en verander de functies
# Maak vervolgens de opdracht hieronder
# Voorbeeld1
def rekenen1():
  getal1 = 50
  getal2 = 5
  return getal1 + getal2

def rekenen2():
  getal1 = 50
  getal2 = 5
  return getal1 - getal2

def rekenen3():
  getal1 = 50
  getal2 = 5
  return getal1 * getal2

getal = rekenen2()
print(getal)

# Voorbeeld2
def locatie(land):
  print("Ik kom uit " + land)

locatie("Amerika")

# Voorbeeld3
def kwadraat(getal):
  resultaat = getal * getal
  return resultaat

mijnKwadraat = kwadraat(4)
print(mijnKwadraat)


# Maak 5 functies die allemaal in een andere taal "Goedemorgen" printen.
# Roep daarna elke functie minimaal 2 keer aan (callen) waardoor er minimaal 10 keer "Goedemorgen" naar de console wordt geprint!

def Frans():
  frans = "Bonjour"
  print(frans)
def Duits():
  duits = "Guten morgen"
  print(duits)
def Spaans():
  spaans = "Beunos dias"
  print(spaans)
def Nederlands():
  nederlands = ("Goeiemorgen")
  print(nederlands)
def Engels():
  engels = "Good morning"
  print(engels)

Frans()
Frans()
Duits()
Duits()
Spaans()
Spaans()
Nederlands()
Nederlands()
Engels()
Engels()