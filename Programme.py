# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 14:34:26 2018

@author: Thomas
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException  
import time
import re

driver = webdriver.Chrome()
driver.get("https://www.ncbi.nlm.nih.gov/")
driver.find_element_by_xpath("//a[contains(@href,'/gene/')]").click()
elem = driver.find_element_by_id("term")
elem.send_keys("VvHT5 vitis vinifera")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source

#attendre que l'utilisateur sélectionne un gène
i=0
while i<50:
    try:
        time.sleep(5)
        chaine_id = driver.find_element_by_xpath("//span[@class='geneid']").text
        break
    except NoSuchElementException:
        i=i+1
        
motif = re.compile(r'(?<=Gene ID: )[0-9]+')
gene_id = motif.search(chaine_id)
gene_id = gene_id.group(0)

print (gene_id)
#driver.close()
