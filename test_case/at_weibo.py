#! D:\work\mgt_webtest\
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

class weiBo(unittest.TestCase):
    def setUp(self):
        pub.init(self)
    
    def test_weibo_add(self):
        '''发微博'''
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(3)
        user.login(self)
        time.sleep(2)
        pub.module_icon(self)
        driver.find_element_by_class_name("j_ico_twitter").click()
        time.sleep(2)
        pub.switchtoframe(self)
        driver.find_element_by_xpath("//textarea").send_keys(u"测试，测试!%s"%time.ctime())
        time.sleep(3)
        driver.find_element_by_xpath("//button[@type='button']").click()
        print u"微博发布!"
        user.quit(self)
        
if __name__ == "__main__":
    unittest.main()