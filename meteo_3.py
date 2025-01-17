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


def mois_annee_31(a): 
    for i in range (31): 
        chaque_jour.append(a)
        a=a+1
    return a


def mois_annee_30(a): 
    for i in range (30): 
        chaque_jour.append(a)
        a=a+1
    return a

def mois_annee_28(a): 
    for i in range (28): 
        chaque_jour.append(a)
        a=a+1
    return a


chaque_jour = []
jour = 19490101
#w= mois_annee_30(jour)
#print (w)


for k in range (12) : 
    if  k == 3 or k==5 or k==8  or k == 10: 
        w =mois_annee_30(jour)
        jour = jour +100
    elif k== 1 :
        w= mois_annee_28(jour)
        jour = jour +100
    else : 
        w= mois_annee_31(jour)
        jour= jour +100 
#print (chaque_jour)



annee_entier = []
pluie= []
for annee in auxerre : 
    for j in range ( 365 ) : 
        if chaque_jour[j] in annee : 
            annee_entier.append(annee[5])
            pluie.append(annee[6])
"""
print (annee_entier) 
print (pluie)
h = len(annee_entier) 
z = len(pluie)
print (h, z)

"""
figure ()
bar(annee_entier, pluie)
show ()


