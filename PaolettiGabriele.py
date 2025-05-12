# Benvenuto e scelta del piano
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt


print("Benvenuto al McDonald's!")
print("Scegli il tuo piano:")
print("1. Hamburger - 5€")
print("2. Cheeseburger - 4.5€")
print("3. Chicken Sandwich - 6€")
piano = int(input("Inserisci il numero della tua scelta: "))
 
# Scelta del secondo
print("\nScegli il tuo secondo:")
print("1. Patatine fritte - 2€")
print("2. Anelli di cipolla - 2.5€")
print("3. Insalata - 3€")
secondo = int(input("Inserisci il numero della tua scelta: "))
 
# Scelta del dessert
print("\nScegli il tuo dessert:")
print("1. Gelato - 3€")
print("2. Torta al cioccolato - 3.5€")
print("3. Mela cotta - 2.5€")
dessert = int(input("Inserisci il numero della tua scelta: "))
 
# Determinazione delle scelte e dei prezzi
if piano == 1:
    piano_scelto = "Hamburger"
    prezzo_piano = 5
elif piano == 2:
    piano_scelto = "Cheeseburger"
    prezzo_piano = 4.5
else:
    piano_scelto = "Chicken Sandwich"
    prezzo_piano = 6
if secondo == 1:
    secondo_scelto = "Patatine fritte"
    prezzo_secondo = 2
elif secondo == 2:
    secondo_scelto = "Anelli di cipolla"
    prezzo_secondo = 2.5
else:
    secondo_scelto = "Insalata"
    prezzo_secondo = 3
if dessert == 1:
    dessert_scelto = "Gelato"
    prezzo_dessert = 3
elif dessert == 2:
    dessert_scelto = "Torta al cioccolato"
    prezzo_dessert = 3.5
else:
    dessert_scelto = "Mela cotta"
    prezzo_dessert = 2.5

# Calcolo del totale
totale = prezzo_piano + prezzo_secondo + prezzo_dessert

# Risultato finale
print("\nHai scelto:")
print(f"Piano: {piano_scelto} - {prezzo_piano}€")
print(f"Secondo: {secondo_scelto} - {prezzo_secondo}€")
print(f"Dessert: {dessert_scelto} - {prezzo_dessert}€")
print("\nIl TOTALE DA PAGARE EURO:")
print(totale)
# Totale
# scriviamo il risultato su un file assieme alla data odierna:
dataoggi=dt.datetime.now()

conta = 0;
if totale > 0:
    conta = conta + 1

print("\nDATA ODIERNA:")

print(dataoggi)

plt.xlabel('fascia oraria')
plt.ylabel('menù')
plt.hist(dataoggi.hour)
plt.hist(conta)

plt.show()



