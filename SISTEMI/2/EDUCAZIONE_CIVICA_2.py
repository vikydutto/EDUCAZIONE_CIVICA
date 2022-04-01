import matplotlib.pyplot as mpl
import csv

file_emissions = open("CO2_emissions.csv")     #apertura file csv
righe_emissions = file_emissions.readlines()     #scrive in righe tutte le righe del file
file_anomalie = open("Temperature_Anomaly.csv")
righe_anomalie = file_anomalie.readlines()

anno_anomalie = []
anno_emissions = []
anomalie = []
total_emissions = []

for riga in righe_anomalie[5:]:
    divisore = riga.split(",")
    anno_anomalie.append(int(divisore[0]))
    anomalie.append(float(divisore[1]))

for riga in righe_emissions[131:]:
    divisore = riga.split(",")
    anno_emissions.append(int(divisore[0]))
    total_emissions.append(float(divisore[1]))

fig, ax = mpl.subplots(nrows = 4,ncols = 1,figsize = (10, 10))
fig.subplots_adjust(hspace = 1)

ax[0].plot(anno_emissions, total_emissions, 'r-')
ax[0].set_title("Emissioni di CO2 globali")
ax[0].grid()

ax[1].plot(anno_emissions, total_emissions, 'ro', markersize = 3)
ax[1].set_title("Emissioni di CO2 globali - DISPERISIONE")
ax[1].grid()

ax[2].plot(anno_anomalie, anomalie, 'b-')
ax[2].set_title("Anomalie temperatura globale")
ax[2].grid()

ax[3].plot(anno_anomalie, anomalie, 'bo', markersize = 3)
ax[3].set_title("Anomalie temperatura globale - DISPERSIONE")
ax[3].grid()
mpl.show()

