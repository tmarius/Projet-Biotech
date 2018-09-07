# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 14:34:26 2018

@author: Thomas
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#####################################################Recuperation des CDS a partir de l ID##########################
#A changer par l ID du gene trouve precedement
gene_id = '100232950'

#Connexion au site sur la page du gene
driver = webdriver.Chrome()
driver.get("https://www.ncbi.nlm.nih.gov/gene/")
query = driver.find_element_by_id("term")
query.send_keys(gene_id)
query.send_keys(Keys.RETURN)

time.sleep(1)
#Recupere le premier mRNA car souvent le bon, a verifié => Sinon faire comme au dessus et demander selection
mrna = driver.find_element_by_xpath("//*[@id='proteinTblId']/tbody//td[contains(text(), 'mRNA')]/following-sibling::td").text
mrna = driver.find_element_by_xpath("//*[@id='proteinTblId']/tbody//td[contains(text(), 'mRNA')]/following-sibling::td/a").click()

debut = '55'
fin = '1665'
time.sleep(1)
dropdown = driver.find_element_by_id("EntrezSystem2.PEntrez.Nuccore.Sequence_ResultsPanel.Sequence_SingleItemSupl.Sequence_ViewerGenbankSidePanel.Sequence_ViewerChangeRegion.Shutter").click()
time.sleep(1)
selected = driver.find_element_by_id("crselregion").click()
debinput = driver.find_element_by_id("crfrom")
debinput.send_keys(debut)
fininput = driver.find_element_by_id("crto")
fininput.send_keys(fin)
upd = driver.find_element_by_id("updateselregion").click()
time.sleep(2)
tofasta = driver.find_element_by_id("ReportShortCut6").click()
#sequence = driver.find_element_by_xpath("//*[@id='viewercontent1']")
sequence = driver.find_element_by_xpath("//*[contains(text(), '>')]").text
print (sequence)
driver.close()




#assert "No results found." not in driver.page_source
#recup = driver.find_element_by_xpath("//*[@id='mw-content-text']/div/div[3]/div/div").text



