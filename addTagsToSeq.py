# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 11:04:17 2018

@author: Nolan
"""

#Initialisation des 2 etiquettes 5' 3' donnés par l'utilisateur
etiqDirect="ATTT"
etiqComplem="AAAC"

#Initialisation des 4 séquences. De base, sont situés dans un tableau à 2 dimensions. 
#Il est nécessaire de les récuperer, en faisant deux boucles for : for i.. for j..
seqDirect1="AATGCGATTTAGC"
seqComplem1="TTACGCTAAATCG"
seqDirect2="GGTGCCAGTAAAA"
seqComplem2="CCACGGTCATTTT"


#Reverse des sequences complementaires     
seqComplem1Reverse=""
seqComplem2Reverse=""

for lettre in reversed(seqComplem1):
    seqComplem1Reverse += lettre

for lettre in reversed(seqComplem2):
    seqComplem2Reverse += lettre


#Ajout des etiquettes aux sequences
resultDirect1= etiqDirect + seqDirect1
resultComplem1= etiqComplem + seqComplem1Reverse 
resultDirect2= etiqDirect + seqDirect2
resultComplem2= etiqComplem + seqComplem2Reverse 

#Affichage des equences avec tags
print(resultDirect1)
print(resultComplem1)
print(resultDirect2)
print(resultComplem2)
