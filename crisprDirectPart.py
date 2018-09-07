from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json
import os

def reverse(chaineantisens):
    chainesens = ""#chaine inversée
     
    for lettre in reversed(chaineantisens):
        chainesens += lettre
         
    return(chainesens)
    
def deuxMaxTm(objectswithtmlist):
    maxTm1 = float('0')
    maxTm2 = float('0')
    tmp = float('0')
    for objectwithtmlist in objectswithtmlist:
        tmp = float(objectwithtmlist['tm'])
        print(tmp)
        if maxTm1 == 0.0:
            maxTm1 = tmp
        elif tmp >= maxTm1:
            maxTm2 = maxTm1
            maxTm1 = tmp
        elif tmp >= maxTm2:
            maxTm2 = tmp
    return(str(maxTm1),str(maxTm2))




print(deuxMaxTm(temp))
#driver = webdriver.Chrome()
#driver.get("https://crispr.dbcls.jp/")
#
#seq="ATGATTCATTCAATTGTTGGTGCCATTACTGGCGAAAATGATAAGAAGAAGATCAAGGGAACTGTTGTGTTGATGAAGAAGAATGTGTTGGATTTTAATGACTTCAATGCATCGGTTCTGGACCGGGTTCATGAGCTGTTGGGACAGGGAGTCTCTCTGCAGCTCGTCAGTGCTGTTCATGGTGATCCTGCAAATGGGTTACAGGGGAAACTTGGGAAACCAGCATACTTGGAAGACTGGATTACCACAATTACTTCTTTAACCGCTGGCGAGTCTGCATTCAAGGTCACGTTCGACTGGGATGAGGAGATTGGAGAGCCAGGGGCTTTCATAATTAGAAACAATCACCACAGTGAGTTTTACCTCAGGACTCTCACTCTTGAAGATGTTCCTGGGTGTGGCAGAATTCA CTTTGTTTGTAATTCCTGGGTCTACCCTGCTAAGCACTACAAAACTGACCGTGTTTTCTTCACTAATCAGACATATCTTCCAAGTGAAACACCAGGGCCACTGCGCAAGTACAGAAAAGGGGAACTGGTGAATCTGAGGGGAGATGGAACCGGAGAGCTTAAGGAATGGGATCGAGTGTATGACTATGCTTACTATAATGATTTGGGGAATCCAGACAGGGATCTCAAATACGCCCGCCCTGTGCTGGGAGGATCTGCAGAGTATCCTTATCCCAGGAGGGGAAGAACTGGTAGACCACCATCTGAAAAAGATCCCAACACCGAGAGCAGATTGCCACTTGTGATGAGCTTAAACATATATGTTCCAAGAGATGAACGATTTGGTCACCTCAAGATGTCAGACTTCCTGGCTTATGCCCTGAAATCCATAGTTCAATTCCTTCTCCCTGAGTTTGAGGCTCTATGTGACATCACCCCCAATGAGTTTGACAGCTTCCAAGATGTATTAGACCTCTACGAAGGAGGAATCAAGGTCCCAGAGGGCCCTTTACTTGACAAAATTAAGGACAACATCCCTCTTGAGATGCTCAAGGAACTTGTTCGTACTGATGGGGAACATCTCTTCAAGTTCCCAATGCCCCAAGTCATCAAAGAGGATAAGTCTGCATGGAGGACTGACGAAGAATTTGCTAGAGAAATGCTGGCTGGACTCAACCCAGTTGTCATCCGACTACTCCAAGAGTTTCCTCCAAAAAGCAAGCTGGATCCTGA"
#
#elemchampseq = driver.find_element_by_id("useq")
#elemchampseq.clear()
#elemchampseq.send_keys(seq)
#elemspecificitycheck = driver.find_element_by_id("crisprdirect-combobox-dblist-inputEl")
#elemspecificitycheck.clear()
#elemspecificitycheck.send_keys("Grape (Vitis vinifera) genome, IGGP_12x (Jun, 2011)")
#elemspecificitycheck.send_keys(Keys.RETURN)
#
##driver.find_element_by_xpath("//div[contains(@id,'boundlist-1010-listEl')]/ul/li").click()
#
#driver.find_element_by_xpath("//*[@id='ext-gen1018']/form/div[1]/p[5]/input").click()
##driver.find_element_by_xpath("//input[contains(@type,'submit')]")
#time.sleep(1)
##driver.find_element_by_xpath("//input[contains(@id,'filter_highlight')]").click()
##driver.find_element_by_xpath("//*[@id='ext-gen1018']/a[2][contains(text(),'Download')]").click()
#driver.find_element_by_xpath("//*[@id='ext-gen1018']/form/div[4]/ul/li[2]/a[2]").click()
##driver.find_element_by_xpath("//a[contains(@type,'submit')]")
#time.sleep(9)
config = json.loads(open('C:/Users/ivan/Downloads/CRISPRdirect.json').read())
results=config['results']
specificresults=[]
for result in results:
    #specificité
    if((int(result['hit_20mer']) <= 1) and (int(result['hit_12mer']) <=1)):
        specificresults.append(result)
        
        deuxMaxTm
    

        
for specificresult in specificresults: 
       if(specificresult['strand'] == '-'):
          specificresult['sequence']= reverse(specificresult['sequence'])
        
        
    #temperature

    #reverse

    

    #seulement2
    
    





assert "No results found." not in driver.page_source
#driver.close()

