# coding = utf-8
from selenium import webdriver
import os, time

driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath(u'上传文件.html')
driver.get(file_path)
driver.find_element_by_name('file').send_keys('D:\\')
time.sleep(3)
driver.quit()
