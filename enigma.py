#importovanie modulu
import string

#otvorenie suboru
subor = open("tabulka_pocetnosti.txt","r")

#zadeklarovanie premennych, zoznamov a triedy
obsah = subor.read()
obsah_velky = obsah.upper()
abeceda = []
pouzite = []
nepouzite = []
statistika = {}

for i in string.ascii_uppercase: #cyklus pre znaky abecedy
    #prida do zoznamu momentalny znak abecedy
    abeceda.append(i)

for ii in obsah_velky: #cyklus pre zvacsany text
    #ak sa momentalny znak nachadza v texte
    if ii in abeceda:
        #na momentalne miesto sa do triedy vlozi pocet pouzitych pismen
        statistika[ii] = obsah_velky.count(ii)
        #ak momentalny znak nebol pouzity
        if not ii in pouzite:
            #vlozenie momentalneho znaku do zoznamu pouzitych
            pouzite.append(ii)

for iiii in abeceda: #cyklus pre znaky v abecede
    #ak momentalny znak nebol pouzity
    if not iiii in pouzite:
        #vlozenie momentalneho znaku do zoznamu nepouzitych
        nepouzite.append(iiii)

#vypisanie pozadovanych hodnot   
print(obsah)
print("Počty jednotlivých znakov v texte:")
for iii in statistika.keys():
    print(iii + "-" + str(statistika[iii]))
print("Nepoužité znaky:",*nepouzite)
