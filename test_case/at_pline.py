#! D:\work\selenium_case
#coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re, user, pub
import sys
reload(sys)
sys.setdefaultencoding( 'utf-8' )

class primaryLine(unittest.TestCase):
    def setUp(self):
        pub.init(self)        
    
    def test_pline_add(self):
        '''新建主线'''
        driver = self.driver
        #driver.get(self.base_url)# + "/module/igoal/index.do?locale=zh_CN")
        user.login(self)
        pub.module_icon(self)
        driver.find_element_by_class_name("j_ico_pline").click()
        time.sleep(2)
        pub.switchtoframe(self)
        driver.implicitly_wait(30)   
        driver.find_element_by_xpath(u"//a[contains(text(),'新建主线')]").click()
        driver.implicitly_wait(30)
        driver.find_element_by_xpath("//input[@id='toNewigoalTitle']").clear()
        newline = driver.find_element_by_xpath("//input[@id='toNewigoalTitle']")
        now = time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime())
        newline.send_keys(u"新建主线_%s"%now)
        time.sleep(3)
        driver.find_element_by_xpath("//button[@id='editIgoalOk']").click()
        time.sleep(2)
        print u"新建主线成功！主线名称为：新建主线_%s"%now
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
