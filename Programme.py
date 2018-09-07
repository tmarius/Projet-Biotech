# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 08:47:25 2018

@author: Thomas
"""

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
from os import chdir,getcwd 
import time
import re
import json


#####################################################FIND GENE ID#########################"
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
    return (gene_id)

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
        pass
    
    #attendre que l'utilisateur sélectionne un gène
    i=0
    while i<50:
        try:
            time.sleep(60)
            driver.switch_to_window(driver.window_handles[1])
            chaine_id = driver.find_element_by_xpath("//p[contains(@class,'itemid')]").text
            break
        except NoSuchElementException:
            i=i+1
            print(i)
    motif = re.compile(r'(?<=GenBank: )([A-Za-z]|[0-9])+')
    gene_id = motif.search(chaine_id)
    gene_id = gene_id.group(0)
    return (gene_id)


#########################################################FIND CDS##########################################
    

def findCDS(gene_id):
    driver.get("https://www.ncbi.nlm.nih.gov/gene/")
    query = driver.find_element_by_id("term")
    query.send_keys(gene_id)
    query.send_keys(Keys.RETURN)
    time.sleep(1)
    #Recupere le premier mRNA car souvent le bon, a verifié => Sinon faire comme au dessus et demander selection
    mrna = driver.find_element_by_xpath("//*[@id='proteinTblId']/tbody//td[contains(text(), 'mRNA')]/following-sibling::td").text
    mrna = driver.find_element_by_xpath("//*[@id='proteinTblId']/tbody//td[contains(text(), 'mRNA')]/following-sibling::td/a").click()
    #PARTIE 1
    #Permet de récupérer les positions de début et fin du CDS
    #On a par exemple CDS 55..1870 , on veut que begin=55 et end=1870
    #driver.get("https://www.ncbi.nlm.nih.gov/nuccore/66016960")
    time.sleep(2)
    positions=driver.find_element_by_xpath("//span[contains(text(),'..')]/following-sibling::span/following-sibling::span").text
    motif = re.compile(r'((\d+)\.\.(\d+))', re.IGNORECASE)
    res = motif.findall(positions)
    debut=res[0][1]
    fin=res[0][2]    
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
    time.sleep(2)
    #sequence = driver.find_element_by_xpath("//*[@id='viewercontent1']")
    #PARTIE 2
    #Permet de récuperer le CDS en fasta
#    driver.get("https://www.ncbi.nlm.nih.gov/nuccore/AY538261.1?report=fasta&from=55&to=1665")
    seq=driver.find_element_by_xpath("//pre").text
    return (seq)

#######################################################MOITIER SUP#########################################
def moitieCDS(seq):
    long = len(seq)
    longmoitie = int(long/2)
#    print(longmoitie)
    moitie = seq[0:longmoitie]
    return (moitie)


#######################################################CRISPR SGRNA###########################################
def findSGRNA(seq):
    
    #Change le path de download
    path = getcwd(); 
    path = path + '\\tmp' ;
    print (path);
    
    chrome_options = webdriver.ChromeOptions()
    prefs = {'download.default_directory' : path }
    chrome_options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(chrome_options=chrome_options)
    
    
    
    driver.get("https://crispr.dbcls.jp/")
    
#    seq="ATGATTCATTCAATTGTTGGTGCCATTACTGGCGAAAATGATAAGAAGAAGATCAAGGGAACTGTTGTGTTGATGAAGAAGAATGTGTTGGATTTTAATGACTTCAATGCATCGGTTCTGGACCGGGTTCATGAGCTGTTGGGACAGGGAGTCTCTCTGCAGCTCGTCAGTGCTGTTCATGGTGATCCTGCAAATGGGTTACAGGGGAAACTTGGGAAACCAGCATACTTGGAAGACTGGATTACCACAATTACTTCTTTAACCGCTGGCGAGTCTGCATTCAAGGTCACGTTCGACTGGGATGAGGAGATTGGAGAGCCAGGGGCTTTCATAATTAGAAACAATCACCACAGTGAGTTTTACCTCAGGACTCTCACTCTTGAAGATGTTCCTGGGTGTGGCAGAATTCA CTTTGTTTGTAATTCCTGGGTCTACCCTGCTAAGCACTACAAAACTGACCGTGTTTTCTTCACTAATCAGACATATCTTCCAAGTGAAACACCAGGGCCACTGCGCAAGTACAGAAAAGGGGAACTGGTGAATCTGAGGGGAGATGGAACCGGAGAGCTTAAGGAATGGGATCGAGTGTATGACTATGCTTACTATAATGATTTGGGGAATCCAGACAGGGATCTCAAATACGCCCGCCCTGTGCTGGGAGGATCTGCAGAGTATCCTTATCCCAGGAGGGGAAGAACTGGTAGACCACCATCTGAAAAAGATCCCAACACCGAGAGCAGATTGCCACTTGTGATGAGCTTAAACATATATGTTCCAAGAGATGAACGATTTGGTCACCTCAAGATGTCAGACTTCCTGGCTTATGCCCTGAAATCCATAGTTCAATTCCTTCTCCCTGAGTTTGAGGCTCTATGTGACATCACCCCCAATGAGTTTGACAGCTTCCAAGATGTATTAGACCTCTACGAAGGAGGAATCAAGGTCCCAGAGGGCCCTTTACTTGACAAAATTAAGGACAACATCCCTCTTGAGATGCTCAAGGAACTTGTTCGTACTGATGGGGAACATCTCTTCAAGTTCCCAATGCCCCAAGTCATCAAAGAGGATAAGTCTGCATGGAGGACTGACGAAGAATTTGCTAGAGAAATGCTGGCTGGACTCAACCCAGTTGTCATCCGACTACTCCAAGAGTTTCCTCCAAAAAGCAAGCTGGATCCTGA"
#    
    elemchampseq = driver.find_element_by_id("useq")
    elemchampseq.clear()
    elemchampseq.send_keys(seq)
    elemspecificitycheck = driver.find_element_by_id("crisprdirect-combobox-dblist-inputEl")
    elemspecificitycheck.clear()
    elemspecificitycheck.send_keys("Grape (Vitis vinifera) genome, IGGP_12x (Jun, 2011)")
    elemspecificitycheck.send_keys(Keys.RETURN)
    
    #driver.find_element_by_xpath("//div[contains(@id,'boundlist-1010-listEl')]/ul/li").click()
    
    driver.find_element_by_xpath("//*[@id='ext-gen1018']/form/div[1]/p[5]/input").click()
    #driver.find_element_by_xpath("//input[contains(@type,'submit')]")
    time.sleep(1)
    #driver.find_element_by_xpath("//input[contains(@id,'filter_highlight')]").click()
    #driver.find_element_by_xpath("//*[@id='ext-gen1018']/a[2][contains(text(),'Download')]").click()
    driver.find_element_by_xpath("//*[@id='ext-gen1018']/form/div[4]/ul/li[2]/a[2]").click()
    #driver.find_element_by_xpath("//a[contains(@type,'submit')]")
    time.sleep(9)
    config = json.loads(open(path+'\CRISPRdirect.json').read())
    results=config['results']

#######################################################DEBUT PROGRAMME##############################################
driver = webdriver.Chrome()  

gene_id = searchByNameId("Vitis vinifera","Vvht5")
print (gene_id)

seq = findCDS(gene_id)
print (seq)

CDS = moitieCDS(seq)
print (CDS)
findSGRNA(CDS)



