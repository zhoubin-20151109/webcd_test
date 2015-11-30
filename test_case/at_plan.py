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

class plan(unittest.TestCase):
    def setUp(self):
        pub.init(self)
    
    def test_newweekplan(self):
        '''新建周计划'''
        driver = self.driver
        driver.get(self.base_url)# + "/mgt/frame.jsp?url=MGT_PLN")
        user.login(self)
        time.sleep(2)
        pub.module_icon(self)
        driver.find_element_by_class_name("j_ico_plan").click()
        time.sleep(2)
        pub.switchtoframe(self)
        driver.find_element_by_xpath("//span[@id='realname']").click()
        time.sleep(1)
        
        try:
            driver.find_element_by_xpath("//div[@id='submitButton']/input[2]").click()
            time.sleep(1)
            now = time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime())
            driver.find_element_by_name("modifyTitle").click()
            time.sleep(1)
            driver.find_element_by_id("planTitle").clear()
            driver.find_element_by_id("planTitle").send_keys(u"新计划标题:%s"%now)
            driver.find_element_by_xpath("//div[@id='hideTitleDiv']/span/input[2]").click()        
            time.sleep(1)
            driver.find_element_by_xpath("//input[@value='立即发布当前计划']").click()#/html/body/div[5]/div/div[2]/div/div/table/tbody/tr/td/div/div[3]/div/div/input
            driver.find_element_by_id("mgtConfirmDivId").find_element_by_id("confirmOk").click()
            time.sleep(3)
            print u"新建周计划成功，周计划标题是:%s"%now
        except:
            print u"本周周计划已存在，测试结束!"   

    
    def test_viewweekplan(self):
        '''查看周计划'''
        driver = self.driver
        driver.get(self.base_url)# + "/mgt/frame.jsp?url=MGT_PLN")
        user.login(self)
        time.sleep(2)
        pub.module_icon(self)
        driver.find_element_by_class_name("j_ico_plan").click()
        time.sleep(2)
        pub.switchtoframe(self)
        driver.find_element_by_xpath("//span[@id='realname']").click()
        time.sleep(1)
        #默认新建本周的计划，若已存在，则直接进入本周计划
        now_a = time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime())
        
        try:            
            driver.find_element_by_xpath("//div[@id='weekInfo']/div/input").click()
        except:
            print u"计划不存在,无法查看,测试结束!"
        time.sleep(2)
        try:
            driver.find_element_by_name("modifyPlan").click()
        except:
            driver.find_element_by_name("modifyTitle").click()
            driver.find_element_by_id("planTitle").clear()
            driver.find_element_by_id("planTitle").send_keys(u"新计划标题:%s"%now_a)
            time.sleep(3)
            driver.find_element_by_xpath("//div[@id='hideTitleDiv']/span/input[2]").click()
            time.sleep(1)
            driver.find_element_by_xpath("//input[@value='立即发布当前计划']").click()
            driver.find_element_by_id("mgtConfirmDivId").find_element_by_id("confirmOk").click()
        print u"计划已发布!计划标题是：新计划标题:%s"%now_a
        time.sleep(1)
    
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