# -*- coding:utf-8 -*-
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.maximize_window()
driver.find_element_by_link_text(u'登录').click()
driver.find_element_by_name('userName').send_keys('18801771334')
driver.find_element_by_name('password').send_keys('199169')
driver.find_element_by_id('TANGRAM__PSP_10__submit').click()
time.sleep(5)
