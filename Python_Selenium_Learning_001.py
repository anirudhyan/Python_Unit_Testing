# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 17:39:49 2022

@author: anirudhya n
"""

import time
from selenium import webdriver  #selenium is package and webdriver is a sub package
driver_chrome=webdriver.Chrome(executable_path=r"C:\Users\anirudhya n\Downloads\Web_Drivers_Selenium\chromedriver_win32\chromedriver") #Chrome is a class
driver_chrome.get("https://rahulshettyacademy.com/angularpractice/")
driver_chrome.maximize_window()
print(driver_chrome.title)
print(driver_chrome.current_url)
driver_chrome.find_element_by_name("name").send_keys("Shri Sairam")
driver_chrome.find_element_by_name("email").send_keys("Learn_python@gmail.com")
#$("[name='name']")   used to check the name from console
driver_chrome.find_element_by_id("exampleInputPassword1").send_keys("123456789")
#$("input[name='name']") used to check from webrowser console
#driver_chrome.find_element_by_css_selector()
#time.sleep(10)
#driver_chrome.get("https://gmail.com")
#print(driver_chrome.title)
#time.sleep(10)
#driver_chrome.back()
#driver_chrome.minimize_window()
'''time.sleep(10)
driver_chrome.refresh()
driver_chrome.close()  # closes a particular tab
#driver_chrome.quit()  # quits all tabs
'''
#driver_mozilla=webdriver.Firefox(executable_path="")
#driver_ie=webdriver.Ie(executable_path="")

'''
Using various locators in selenium
id
name
class name
link text
css
xml
'''
