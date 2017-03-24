# -*- coding:utf-8 -*-
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="u1"]/a[8]').click()
driver.find_element_by_xpath('//*[@id="save"]').click()
alert = driver.switch_to_alert()
time.sleep(10)
alert.accept()
driver.quit()
