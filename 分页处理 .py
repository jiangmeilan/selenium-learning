# coding = utf-8
from selenium import webdriver
import os, time

driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath(u'∑÷“≥¥¶¿Ì.html')
driver.get(file_path)
total_page = len(driver.find_element_by_tag_name('select').find_elements_by_tag_name('option'))
print 'total page is %s' %(total_pages)
time.sleep(2)
pages = driver.find_element_by_tag_name('select').find_elements_by_tag_name('option')
for page in pages:
	page.click()
	time.sleep(3)

time.sleep(3)
driver.quit()
