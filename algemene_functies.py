#opgave 8.2
def mijn_functie_1(a):
    return a * a
 
#opgave 8.3
# Met dank aan Peter :-)
def mijn_functie_2(a,b):
      uitvoer_lijst = []
      uitvoer_lijst.append(a+b)
      uitvoer_lijst.append(a-b)
      uitvoer_lijst.append(a*b)
      uitvoer_lijst.append(a/b)
      return uitvoer_lijst


print mijn_functie_2(1,2)