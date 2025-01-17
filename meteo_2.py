import csv 
from matplotlib.pyplot import *
ville_89 = []
with open('Q_89_1871-1949_RR-T-Vent.csv',newline="") as donnee:
    reader=csv.reader(donnee,delimiter=';')
    for row in reader:
        ville_89.append(row)

# print (donne_pluie)
del ville_89[0]
auxerre = [] 
for row in ville_89  :
    if "AUXERRE-LES-ILES" in row  and  "1949" in row[5]:
    	auxerre.append ([row[0], row[1],row[2],row [3], row [4], int(row [5]), float (row[6])]) 



chaque_jour = []
jour = 19490100
for i in range (31) :
    jour = jour + 1
    chaque_jour.append(jour)

# print (chaque_jour)


mois_annee = []
pluie= []
for mois in auxerre :
    for j in range (0,31) : 
        if chaque_jour[j] in mois : 
            mois_annee.append(mois[5])
            pluie.append(mois[6])
print (mois_annee) 
print (pluie)


figure ()
bar(mois_annee, pluie)
show ()
