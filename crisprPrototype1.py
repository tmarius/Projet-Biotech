import time
import json


def reverse(chaineantisens):
    chainesens = ""#chaine inversée
     
    for lettre in reversed(chaineantisens):
        chainesens += lettre
         
    return(chainesens)

    
def deuxMaxTm(objectswithtmlist):
    list2max=[]    
    tmp = float('0')
    for objectwithtmlist in objectswithtmlist:
        tmp = float(objectwithtmlist['tm'])
        print(tmp)
        
        if (len(list2max) == 0):
            list2max.append(objectwithtmlist)    
           
        elif (len(list2max) == 1):
            if tmp >= float(list2max[0]['tm']):
                list2max.append(list2max[0]) 
                list2max[0] = objectwithtmlist
            else:
                list2max.append(objectwithtmlist)
        else:
            if tmp >= float(list2max[0]['tm']):
                list2max[1] = list2max[0]
                list2max[0] = objectwithtmlist
            elif tmp >= float(list2max[1]['tm']):
                list2max[1] = objectwithtmlist
    return(list2max)


def complementaire(seq):
    compl = ''
    for i in seq:
        if i == 'A':
            compl += 'T'
        elif i == 'T':
            compl += 'A'
        elif i == 'C':
            compl += 'G'
        elif i == 'G':
            compl += 'C'
        else:
            print ('sequence corompue')
    return (compl)


config = json.loads(open('C:/Users/ivan/Downloads/CRISPRdirect.json').read())
results=config['results']
specificresults=[]
sgrnalist=[]

allstringlistsgrna=[]
for result in results:
    #specificité
    if((int(result['hit_20mer']) <= 1) and (int(result['hit_12mer']) <=1)):
        specificresults.append(result)
        
    
        
        
sgrnalist=deuxMaxTm(specificresults)


for sgrna in sgrnalist:  
    stringlistsgrnacomps=[]
    if(sgrna['strand'] == '-'):
        stringlistsgrnacomps.append(reverse(sgrna['sequence']))
    else:
        stringlistsgrnacomps.append(sgrna['sequence'])
    stringlistsgrnacomps.append(complementaire(sgrna['sequence']))
    allstringlistsgrna.append(stringlistsgrnacomps)
print(allstringlistsgrna)     





