# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 11:04:17 2018

@author: Nolan
"""

#Si au moins une chaine de caractère passée est vide, retourne false. Sinon, retourne true
def isTextsNotEmpty(*args):
    result=True
    for arg in args:
        if not arg:
            result=False
    return result
    
###Initialisation de toutes les variables (espece, seq, id,...)
espece="a"
name="a"
seq=""
sgRNA1=""
sgRNA2=""
choiceBox=""



#Si le bouton radio est sgRNA
if(choiceBox=="sgRNA"):
    if(isTextsNotEmpty(espece, name, seq, sgRNA1, sgRNA2)):
        print("On fait les manip nécessaires pour la recherche sgRNA")
    else:
        print("ERREUR - Pour la recherche de sgRNA, veuillez entrer une espèce, un id, une séquence, et deux brins 5' 3'")
    

#Si le bouton radio est boite de régulation
else:    
    if(isTextsNotEmpty(espece, name, seq, sgRNA1, sgRNA2)):
        print("On fait les manip nécessaires pour la boîte de régulation")
    else:
        print("ERREUR - Pour la boîte de régulation, veuillez entrer une espèce, un id et une séquence")
        
