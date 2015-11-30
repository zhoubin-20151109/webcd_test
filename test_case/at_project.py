#! D:\work\mgt_webtest
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

class projectStatus(unittest.TestCase):
    def setUp(self):
        pub.init(self)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
    
    def test_project_create_project(self):
        '''新建项目'''
        driver = self.driver
        user.login(self)
        time.sleep(2)
        self.assertEqual("今目标互联网工作平台",driver.title)
        print driver.title
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="headAdd"]/i').click()
        time.sleep(2)
        driver.find_element_by_class_name('project').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="addProject"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="projectEdit"]/div/div[2]/div/div[1]/div[1]/input').send_keys(u'项目编号_%s'%pub.now())
        # driver.find_element_by_css_selector('div.projectCode.project_code.ui-input').send_keys(u'项目编号_%s'%pub.now())
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('//*[@id="projectEdit"]/div/div[2]/div/div[2]/div[1]/input').send_keys(u'项目名称_%s'%pub.now())
                                    # //*[@id="projectEdit"]/div/div[2]/div/div[2]/div[1]/input
        driver.implicitly_wait(10)
        # driver.find_element_by_xpath('//*[@id="projectContent"]').send_keys(u'项目内容_%s'%pub.now())
        # driver.implicitly_wait(10)
        #web控件尚未提交，无法创建项目
        driver.find_element_by_xpath('//*[@id="projectEdit"]/div/div[2]/div/div[6]/button[1]').click()
        
#     def test_project_
        
if __name__ == "__main__":
    unittest.main()