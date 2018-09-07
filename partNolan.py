# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 11:04:17 2018

@author: Nolan
"""
from selenium import webdriver  
import time 
import re




driver = webdriver.Chrome()

#PARTIE 1
#Permet de récupérer les positions de début et fin du CDS
#On a par exemple CDS 55..1870 , on veut que begin=55 et end=1870
#driver.get("https://www.ncbi.nlm.nih.gov/nuccore/66016960")
time.sleep(2)
positions=driver.find_element_by_xpath("//span[contains(text(),'..')]/following-sibling::span/following-sibling::span").text
motif = re.compile(r'((\d+)\.\.(\d+))', re.IGNORECASE)
res = motif.findall(positions)
begin=res[0][1]
end=res[0][2]
print(begin)
print(end)

#PARTIE 2
#Permet de récuperer le CDS en fasta
driver.get("https://www.ncbi.nlm.nih.gov/nuccore/AY538261.1?report=fasta&from=55&to=1665")
seq=driver.find_element_by_xpath("//pre").text



