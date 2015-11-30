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

class myPlan(unittest.TestCase):
    def setUp(self):
        pub.init(self)
    
    def test_planlist_01(self):
        '''新建日计划'''
        driver = self.driver
        driver.get(self.base_url)     
        user.login(self)
        time.sleep(2)
        self.assertEqual("今目标企业工作平台",driver.title)
        pub.module_icon(self)
        driver.find_element_by_class_name("j_ico_log").click()
        time.sleep(3)
        pub.switchtoframe(self)
        driver.find_element_by_xpath("//li[2]/a/strong").click()
        time.sleep(2)
        driver.find_element_by_xpath("//a[contains(text(),'新建日计划')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='dayPlanContent']").send_keys(u"今日工作计划@%s"%time.ctime())
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='btn_worklog_ok_dayPlan']").click()
        user.quit(self)
        
    def test_planlist_02(self):
        '''日计划状态'''
        driver = self.driver
        driver.get(self.base_url)     
        user.login(self)
        time.sleep(2)
        self.assertEqual("今目标企业工作平台",driver.title)
        pub.module_icon(self)
        driver.find_element_by_class_name("j_ico_log").click()
        time.sleep(3)
        pub.switchtoframe(self)
        driver.find_element_by_xpath("//li[2]/a/strong").click()
        time.sleep(2)
        driver.find_element_by_css_selector("i.mpic-deny").click()
        time.sleep(2)
        print u"日计划状态已改为已完成！"
        driver.find_element_by_xpath("//a[2]/span").click()
        time.sleep(1)
        driver.find_element_by_css_selector("i.mpic-ok").click()
        time.sleep(1)
        print u"日计划状态恢复为未完成！"
        user.quit(self)
        
    def test_planlist_03(self):
        '''查询日计划'''
        driver = self.driver
        driver.get(self.base_url)     
        user.login(self)
        time.sleep(2)
        self.assertEqual("今目标企业工作平台",driver.title)
        pub.module_icon(self)
        driver.find_element_by_class_name("j_ico_log").click()
        pub.switchtoframe(self)
        driver.find_element_by_xpath("//li[2]/a/strong").click()
        time.sleep(2)
        driver.find_element_by_css_selector("i.icon-calendar").click()
        driver.find_element_by_xpath("/html/body/div[2]").find_element_by_xpath("//tbody/tr[5]/td[5]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//span[@id='dpYears2']/span/i").click()
        driver.find_element_by_xpath("/html/body/div[3]").find_element_by_xpath("//div[3]/div[3]/table/tbody/tr[5]/td[5]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//button[@id='checkBtn']").click()
        time.sleep(2)
        print u"查询结果成功！"
        driver.find_element_by_xpath("//*[@id='resetBtn']").click()
        print u"查询时间已清空！"
        user.quit(self)
        
    

if __name__ == "__main__":
    unittest.main()
