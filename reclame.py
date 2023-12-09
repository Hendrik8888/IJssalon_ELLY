from algemene_functies import mijn_functie_2

# opgave 8.5
def aanbieding_1(smaak,prijs,korting):
    
    if smaak == "aardbei":
        return prijs * (1 - korting)

aanbieding = aanbieding_1("aardbei",4,0.1)

print (f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak aardbei, van 4 euro voor {aanbieding} euro")

'''
def inkomsten_totaal(inkomsten):
    totaal_inkomsten = sum(inkomsten)
    return totaal_inkomsten

inkomsten_per_dag = [220, 430, 125, 160, 205, 90, 345]
totaal_inkomsten = inkomsten_totaal(inkomsten_per_dag)
print (f"totaal inkomsten deze week : {totaal_inkomsten}")
'''
def inkomsten_totaal(inkomsten, btw):
    totaal_inkomsten = sum(inkomsten)
    btw_bedrag = totaal_inkomsten * btw
    totaal_bedrag_met_btw = totaal_inkomsten + btw_bedrag

    resultaat_string = (
        f"Het totaal van alle inkomsten van deze week is {totaal_bedrag_met_btw} euro, "
        f"waarover {btw_bedrag} euro btw betaald dient te worden.")
    return resultaat_string

inkomsten_per_dag = [220, 430, 125, 160, 205, 90, 345]
btw_percentage = 0.19  
resultaat = inkomsten_totaal(inkomsten_per_dag, btw_percentage)
print(resultaat)
'''
def laag_en_hoog(inkomsten):
    laagste = min(inkomsten)
    hoogste = max(inkomsten)
    resultaat_string = (
            f"De laagste waarde is {laagste} euro, "
            f"De hoogste waarde is {hoogste} euro. ")
    return resultaat_string

inkomsten_per_dag = [220, 430, 125, 160, 205, 90, 345]
resultaat2 = laag_en_hoog(inkomsten_per_dag)
print(resultaat2)
'''

def gemiddelde(inkomsten):
    gem = gemiddelde_inkomsten = sum(inkomsten) / len(inkomsten)
    resultaat_string = (
            f"De gemiddelde inkomsten deze week zijn {gem} euro, ")
    return resultaat_string

mijn_lijst = [220, 430, 125, 160, 205, 90, 345]
resultaat3 = gemiddelde(mijn_lijst)
print(resultaat3)


def hoog_en_laag(lijst):
    laagste = min(lijst)
    hoogste = max(lijst)
    return hoogste, laagste

def meervoudig(invoer_lijst):
    hoogste, laagste = hoog_en_laag(invoer_lijst)
    return [hoogste, laagste]

invoer_lijst = [10, 5, 3, 2, 1, 2, 9]

if 5 <= len(invoer_lijst) <= 11:
    resultaat4 = meervoudig(invoer_lijst)
else: resultaat4 = (f"Er zijn {len(invoer_lijst)} integers. En dat is niet tussen 5 en 10 integers.")

print("Hoogste en laagste waarden:", resultaat4)

""" 
Een opmerking i.v.m. opgave 12 van de huiswerkopgave van les 8

Als er in opgave 12 van de huiswerkopgave van les 8 gesproken wordt over het bestand aanbieding.py 
dan gaat het wel degelijk om het bestand reclame.py. 
Met andere woorden de functie mijn_functie_2() importeer je in het bestand reclame.py.
"""

def combinatie(invoer_lijst_2):
    korte_lijst = hoog_en_laag(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer
invoer_lijst_2 = [2, 3]

resultaat_combinatie = combinatie(invoer_lijst_2)

print(resultaat_combinatie) 


