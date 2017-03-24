# -*- coding:utf-8 -*-
from selenium import webdriver
import os, time

browser = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath(u'drop.html')
browser.get(file_path)
time.sleep(2)
browser.find_element_by_id('ShippingMethod').click()
browser.find_element_by_xpath("//option[@value='10.69']").click()
time.sleep(3)
browser.quit()
