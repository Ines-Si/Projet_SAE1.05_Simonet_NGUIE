import csv 
from matplotlib.pyplot import *  
ville_89 = []
with open('Q_89_previous-1950-2023_RR-T-Vent.csv',newline="") as donnee:
    reader=csv.reader(donnee,delimiter=';')
    for row in reader:
        ville_89.append(row)

del ville_89[0]
auxerre = []
for row in ville_89  :
    if "AUXERRE" in row  and  "2000" in row[5]:
        auxerre.append ([int(row [5]), float (row[6]), float (row[8]), float(row[12]), row[20] ])  #5 = jour ; 6 = RR ;  8= ° min ; 12 = °max ; 20 ampli °    #  

print (auxerre) 

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

def mois_annee_29(a): 
    for i in range (29): 
        chaque_jour.append(a)
        a=a+1
    return a


chaque_jour = []
jour = 20000101   # a changer pour bon fonctionne #
#w= mois_annee_30(jour)
#print (w)


for k in range (12) : 
    if  k == 3 or k==5 or k==8  or k == 10: 
        w =mois_annee_30(jour)
        jour = jour +100
    elif k== 1 :
        w= mois_annee_29(jour)
        jour = jour +100
    else : 
        w= mois_annee_31(jour)
        jour= jour +100 
#print (chaque_jour)



annee_entier = []
pluie= []
temperature_min = []
for annee in auxerre : 
    for j in range ( 365 ) : 
        if chaque_jour[j] in annee : 
            annee_entier.append(annee[0])
            pluie.append(annee[1])
            temperature_min.append(annee[2])

#print (annee_entier) 
#print (pluie)
#print (temperature_min)


visibilite = []
brouillard =""
for l in range (365): 
    if pluie[l] > 2.0 and temperature_min[l]<3.0 :
        brouillard="True" 
        visibilite.append(brouillard) 
    else :
        brouillard = "False" 
        visibilite.append(brouillard)
#print(visibilite)

couleur = []
for m  in range (365) : 
    if visibilite[m] == "True" : 
        color = "blue"
        couleur.append(color)  

    elif visibilite[m] == "False" :  
        color = "red" 
        couleur.append(color) 

figure ()
bar (annee_entier, pluie)
show()

