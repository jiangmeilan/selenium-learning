# coding = utf-8
from selenium import webdriver
import os, time

driver = webdriver.Chrome()
driver.get('https://passport.baidu.com/v2/?login')

driver.add_cookie({'name':'useName','value':'18801771334'})
driver.add_cookie({'name':'password','value':'lan199169'})

driver.get('https://passport.baidu.com/v2/?login')
time.sleep(5)

driver.quit()


