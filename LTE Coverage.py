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
 
def startBot(Address, url):
    path = r"C:\Users\Dewald\OneDrive - FrontierCo\Desktop\Python Projects\Website_Login\chromedriver.exe"
     
    # giving the path of chromedriver to selenium webdriver
    driver = webdriver.Chrome(path)
     
    # opening the website  in chrome.
    driver.get(url)
     
    # find the id or name or class of
    # username by inspecting on username input
    driver.find_element_by_name("search").send_keys(Address)
    #print("1") 
    time.sleep(2)
    #try:
    html_list = driver.find_element_by_class_name("list-group")
        #print("2")
    items = html_list.find_elements_by_class_name("list-group-item")
    #print("3")
    #print(type(items)) Items becomes list 
    #except 
    x = items[0].text +" "
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
        
    #except Exception() as e:
        #print("LTE is not available at "+str(x))
            
    #clickbtn = driver.find_element_by_class_name("input-group-append") #clicks in text box
    #driver.find_element_by_xpath("//div[@class='input-group-append']").send_keys(Keys.ENTER)
    #driver.find_element_by_xpath("//ul[@class='input-group']").click()
    #time.sleep(5)
    
    #for x in items:
    #    text = x.text
    #    print(text)
    
    #driver.get('popupContainer')
    #print(str(driver.text))
    
    
Address = input("Type Address \n")
Address += (" ")
print("address")
url = "https://vccoverage.afrigis.co.za/#/"
startBot(Address,url)