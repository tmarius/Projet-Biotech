# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 14:34:26 2018

@author: Thomas
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException 
import time
import re

driver = webdriver.Chrome()


def searchByNameId(espece, nameId):
    driver.get("https://www.ncbi.nlm.nih.gov/gene/")
    elem = driver.find_element_by_id("term")
    elem.send_keys(espece + ' ' + nameId)
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    
    #attendre que l'utilisateur sélectionne un gène
    i=0
    while i<50:
        try:
            time.sleep(5)
            chaine_id = driver.find_element_by_xpath("//span[contains(@class,'geneid')]").text
            break
        except NoSuchElementException:
            i=i+1
            
    motif = re.compile(r'(?<=Gene ID: )[0-9]+')
    gene_id = motif.search(chaine_id)
    gene_id = gene_id.group(0)
    print (gene_id)

def searchBySeq(espece, seq):
    driver.get("https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastn&PAGE_TYPE=BlastSearch&LINK_LOC=blasthome")
    elem = driver.find_element_by_id("seq")
    elem.send_keys(seq)
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    elem = driver.find_element_by_id("qorganism")
    elem.send_keys(espece)
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    try:
        driver.find_element_by_id("b1").click()
    except NoSuchElementException:
        time.sleep(10)
    
    #attendre que l'utilisateur sélectionne un gène
    i=0
    while i<50:
        try:
            time.sleep(5)
            chaine_id = driver.find_element_by_xpath("//p[contains(@class,'itemid')]").text
            #driver.switch_to_window(driver.window_handles[1])
            break
        except NoSuchElementException:
            i=i+1
    motif = re.compile(r'(?<=GenBank: )[0-9]+')
    gene_id = motif.search(chaine_id)
    gene_id = gene_id.group(0)
    print (gene_id)

#searchByNameId("Vitis vinifera","Vvht5")
searchBySeq('Vitis vinifera (taxid:29760)','AATCAAGCATTTTATCAAATCAATTTGTTTAAACAGATGATGTGATGAAAGCCGTTTCTTTCTTACCTGTGTATTGGGAATTTAATACCGTAATATTTTGTATCATATACACACGTGTATATATATATATATATATATATATATATATGAAAATGTCTTTATCACATTA')
#driver.close()
