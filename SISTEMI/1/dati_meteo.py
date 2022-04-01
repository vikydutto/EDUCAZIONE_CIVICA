import matplotlib.pyplot as mpl
import csv

file = open("./dati_meteo.csv")     #apertura file csv
righe = file.readlines()            #scrive in righe tutte le righe del file

mesi = []
t_med = []
giorni_giacca = []
giorni_videogame = []
giorni_scolastici = []



for riga in righe[1:]:
    divisore = riga.split(",")
    mesi.append(divisore[0])
    t_med.append(divisore[3])
    giorni_giacca.append(divisore[5])
    giorni_scolastici.append(divisore[6])
    giorni_videogame.append(divisore[7])

