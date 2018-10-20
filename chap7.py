#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 22:59:28 2018

@author: occhipinti
"""

from math import pi
       

#Chapitre 7 Fonctions originales


# Exercice 7.2
# Fonction ligneCar(n, ca) qui renvoie une chaîne de n caractères ca

ca = "jo"
n = 9

def ligneCar(n , ca):
    
    ch = " "
   
    for i in range(n):
        
        ch = ch + ca
        
    return ch
    



# Exercice 7.3
# Fonction qui renvoye la surface (l’aire) d’un cercle

def surfCercle(R):
    
    return pi * R**2


#print(surfCercle(13))



# Exercice 7.4
# Fonction volBoite(x1,x2,x3) qui renvoie 
#le volume d’une boîte parallélépipédique

def volBoite(x1,x2,x3):
    
    return x1 * x2 * x3

#print(volBoite(1,3,4))



# Exercice 7.5
# Fonction maximum(n1,n2,n3) qui renvoie le plus grand de 3 nombres

def maximum(n1,n2,n3):
    
    if n1 >= n2 and n3 :
        
        return n1
    
    elif  n2 >= n3 :
        
        return n2
    
    else :
        
        return n3
    
    

#print(maximum(222,888,2))
        

# Exercice 7.9
# Fonction compteCar(ca,ch) qui renvoie le nombre de fois que 
#l’on rencontre le caractère ca dans la chaîne ch

def compteCar(ca,ch):
    

    nc = 0
    
    for k in range(len(ch)):
        
        if ch[k] == ca :
            
            nc += 1
    
    return nc

print(compteCar('o','ok'))
print()
print()

# Exercice 7.10
# Fonction indexMax(liste) qui renvoie l’index de l’élément 
# ayant la valeur la plus élevée dans la liste 

def indexMax(liste):
    
    max , i = liste[0] , 0
    
    for k in range(1,len(liste)):
        
        if max < liste[k] :
            
            max , i = liste[k] , k 
            
    return i

print(indexMax([1,3,34,2,4]))
print() 


# Exercice 7.11
# Fonction nomMois(n) qui renvoie le nom du énième mois de l’année
# Aide correction  Ok

def nomMois(n):
    t = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet',
         'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
    return t[n-1]


#Exercice 7.12
#Fonction inverse(ch) qui permet d’inverser l’ordre des caractères d’une chaîne quelconque
    
def inverse(ch):
    
    a = " "
    
    for k in range(len(ch)):
            
        a += ch[len(ch)-k-1]
            
    return a

print(inverse('key'))
print()





# Exercice 7.13
# Fonction compteMots(ph) qui renvoie 
# le nombre de mots contenus dans la phrase ph.
# Aide Correction 

def compteMots(ph):
    p = ' ' + ph + ' '           #pourquoi presence de " ' ' " au debut/fin
    t = []
    for k in range(len(p)):
        if p[k] == ' ':
            t.append(k)

    cpt = 0
    for k  in range(len(t)-1):    #pourquoi -1
        if t[k+1] - t[k] > 1:     #je ne comprends pas cette instruction
            cpt += 1

    return cpt

    
print(compteMots("la voiture rouge"))

    
#Exercice 7.14

def volboite(x1=10 ,x2=10, x3=10):
     
    return x1 * x2 * x3





    
#Exercice 7.15
#Correction vue Ok
    

#Exercice 7.16
#Correction vue Ok
    

    
#Exercice 7.17
#correction vue Ok
   
            
            
        
        
        
    
    
    
    
    


