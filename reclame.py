from algemene_functies import mijn_functie_2
def aanbieding_1(smaak,prijs,korting):
    korting_prijs = prijs - (prijs * korting)
    print(f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {korting_prijs:.2f} euro.")

aanbieding_1("aardbei", 4, 0.1)

def inkomsten_totaal(inkomsten,btw):
    totaal_inkomsten = sum(inkomsten)
    btw_percentage = totaal_inkomsten * btw
    return (f"Het totaal van alle inkomsten van deze week is {totaal_inkomsten} euro, waarover {btw_percentage} euro btw betaald dient te worden.")
week_inkomsten = [220, 430, 125, 160, 205, 90, 345]
btw_bedrag = 0.09

totaal = inkomsten_totaal(week_inkomsten, btw_bedrag)
print(totaal)

def laag_en_hoog(mijn_lijst):
    hoogste = max(mijn_lijst)
    laagste = min(mijn_lijst)
    return hoogste, laagste

inkomen_per_dag = [220, 430, 125, 160, 205, 90, 345]
  
laag_hoog_resultaat = laag_en_hoog(inkomen_per_dag)
print(laag_hoog_resultaat)

def gemiddelde(mijn_lijst): 
    gemiddelde_inkomsten = sum(mijn_lijst) / len(mijn_lijst)
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde_inkomsten} euro."

inkomen_per_dag = [220, 430, 125, 160, 205, 90, 345]

totaal_gemiddelde = gemiddelde(inkomen_per_dag)

print(totaal_gemiddelde)

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

invoer_getal = [10,5,3,2,1,2,9]
resultaat_meervoudig = meervoudig(invoer_getal)
print(resultaat_meervoudig)

    
def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer