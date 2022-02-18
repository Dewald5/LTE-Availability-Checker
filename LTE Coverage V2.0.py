# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 08:46:58 2021

@author: Dewald
"""
# Used to import the webdriver from selenium
from selenium import webdriver 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import requests
import time
import os

# Get the path of chromedriver which you have install
 
def startBot(url):
    valid = False
    while valid == False:
        Address = input("Type Address \n")
        Address += (" ")
        path = r"C:\Users\Dewald\OneDrive - FrontierCo\Desktop\Python Projects\Website_Login\chromedriver.exe"
         
        driver = webdriver.Chrome(path)
        driver.get(url)
        driver.find_element_by_name("search").send_keys(Address)
        time.sleep(2)
        html_list = driver.find_element_by_class_name("list-group")
        items = html_list.find_elements_by_class_name("list-group-item")
        valid = True
        try:
           x = items[0].text +" " 
        except IndexError as e:
            print("Please enter valid address")
            valid = False
    
    driver.refresh() #refreshes page
    time.sleep(1)
    driver.find_element_by_name("search").send_keys(x)
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='app']/div/div[1]/div/div[1]/div/ul/li[1]").click()
    time.sleep(12)
    #LTE = driver.find_element_by_xpath("//*[@id='popupContainer']")       
    #LTE = driver.find_element_by_id("popupContainer")
    try:
        driver.find_element_by_xpath("//*[@id='popupContainer']/div[4]/div[2]/a")
        print("\n LTE is available at "+str(x))
    except NoSuchElementException as exc:
        print("\n LTE is not available at "+str(x))
        
url = "https://vccoverage.afrigis.co.za/#/"
startBot(url)