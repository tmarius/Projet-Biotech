# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 11:04:17 2018

@author: Nolan
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
driver.find_element_by_xpath("//li[contains(@class,'psf-meta')]").click() 
aa=driver.find_element_by_xpath("//li[contains(@class,'psf-meta')]/a").text 
print(aa)
assert "No results found." not in driver.page_source
driver.close()
