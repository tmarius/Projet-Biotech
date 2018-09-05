# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 14:34:26 2018

@author: Thomas
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#driver = webdriver.Chrome()
#driver.get("http://www.python.org")
#assert "Python" in driver.title
#elem = driver.find_element_by_name("q")
#elem.clear()
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
#driver.close()

driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org/")
elem = driver.find_element_by_id("searchInput")
elem.send_keys("abricot")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
recup = driver.find_element_by_xpath("//*[@id='mw-content-text']/div/div[3]/div/div").text
print (recup)
#driver.close()