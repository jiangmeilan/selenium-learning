from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
#from selenium.webdrivier.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = 'http://www.baidu.com' 
        self.verificationError = []

    def test_baidu_search(self):
        driver = self.driver
        try:
            driver.get(self.base_url)
            driver.find_element_by_id('kw').send_keys('selenium')
            driver.find_element_by_id('su').click()
        except Exception as e:
            self.verificationError.append(str(e))

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationError)

if __name__ == '__main__':
    unittest.main()

