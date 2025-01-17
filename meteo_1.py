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
    	auxerre.append ([row[0], row[1],row[2],row [3], row [4], row [5], float (row[6])]) 

journee = []
for jour in auxerre :
    if "19490505" in jour : 
        journee.append(jour)
print (journee) 
figure ()
bar(journee[0][5], journee[0][6])
show ()