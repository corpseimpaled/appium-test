import unittest
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class Login(unittest.TestCase):
    reportDirectory = 'reports'
    reportFormat = 'xml'
    dc = {}
    testName = 'Login'
    driver = None
    
    def setUp(self):
        self.dc['reportDirectory'] = self.reportDirectory
        self.dc['reportFormat'] = self.reportFormat
        self.dc['testName'] = self.testName
        self.dc['udid'] = 'LGH860b77a12bb'
        self.dc['appPackage'] = 'org.owline.kasirpintar'
        self.dc['appActivity'] = '.SplashScreen'
        self.dc['platformName'] = 'android'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',self.dc)

    def testLogin(self):
        self.driver.find_element(By.XPATH, '//button[text()="Masuk"]').click()
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@id="edt_email"]')))
        self.driver.find_element_by_xpath("xpath=//*[@id='edt_email']").send_keys('corpseimpaled@gmail.com')
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@id="edt_password"]')))
        self.driver.find_element_by_xpath("xpath=//*[@id='edt_password']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='edt_password']").send_keys('impaled_97')
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@id="btn_login"]')))
        self.driver.find_element_by_xpath("xpath=//*[@id='btn_login']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='OK']").click()

    def tearDown(self):
        self.driver.quit()
        
    if __name__ == '__main__':
        unittest.main()
