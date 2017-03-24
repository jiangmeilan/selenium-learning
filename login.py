# -*- coding:utf-8 -*-
import time
import os
from selenium import webdriver
driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('login.html')
driver.get(file_path)
driver.maximize_window()
input_name = driver.find_element_by_name('u')
input_name.send_keys('lushuai')
input_key = driver.find_element_by_name('p')
input_key.send_keys('lanlan')
button = driver.find_element_by_class_name('but')
button.click()
time.sleep(5)
browser.quit()
