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

class myLog(unittest.TestCase):
    def setUp(self):
        pub.init(self)
    
    def test_mylog_01(self):
        '''查看评阅日志权限人'''
        driver = self.driver
        driver.get(self.base_url)     
        user.login(self)
        time.sleep(2)
        self.assertEqual("今目标企业工作平台",driver.title)
        pub.module_icon(self)
        driver.find_element_by_class_name("j_ico_log").click()
        pub.switchtoframe(self)
        driver.find_element_by_xpath("//a[contains(@href, 'mylog.do')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//a[contains(text(),'看看谁有权评阅您的日志')]").click()
        time.sleep(2)
        pingyue = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div")
        pingyue.text
        print u"有权评阅您的日志的有：%s"%pingyue.text
        driver.get_screenshot_as_file("D:\\work\\mgt_webtest\\screenshot\\permModalpeople%s"%time.strftime("%Y%m%d_%H%M%S",time.localtime()))
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='permModal']/div[3]/button").click()#find_element_by_xpath('//*[@id="permModal"]').
        user.quit(self)

    def test_mylog_02(self):
        '''查看日志详情'''
        driver = self.driver
        driver.get(self.base_url)
        user.login(self)
        time.sleep(2)
        self.assertEqual("今目标企业工作平台",driver.title)
        pub.module_icon(self)
        driver.find_element_by_class_name("j_ico_log").click()
        pub.switchtoframe(self)
        driver.find_element_by_xpath("//a[contains(@href, 'mylog.do')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='containerDiv']/div/div[2]/div[3]/div/table/tbody/tr/td/div").click()
        time.sleep(2)
        logdetail = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/h4")
        logdetail.text
        print u"您现在看到的日志是%s的日志"%logdetail.text
        driver.find_element_by_xpath("//div[3]/div/div/a").click()
        time.sleep(2)
        driver.find_element_by_xpath("//a[contains(text(),'上一个')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//a[contains(text(),'返回日志列表')]").click()
        time.sleep(2)
        user.quit(self)
        

if __name__ == "__main__":
    unittest.main()
