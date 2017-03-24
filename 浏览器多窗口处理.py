# -*- coding:utf-8 -*-
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://passport.baidu.com/v2/?login&tpl=mn&u=https%3A%2F%2Fwww.baidu.com%2F')
nowhandle = driver.current_window_handle
driver.maximize_window()
driver.find_element_by_link_text(u'立即注册').click()
time.sleep(10)
allhandles = driver.window_handles
for handle in allhandles:
    if handle != nowhandle:
        driver.switch_to_window(handle)
        print 'new window!'
        time.sleep(5)
        driver.close()
driver.switch_to_window(nowhandle)
driver.find_element_by_id('kw').send_keys(u'注册成功！')
time.sleep(5)
driver.quit()
