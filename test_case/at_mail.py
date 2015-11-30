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

class mail(unittest.TestCase):
    def setUp(self):
        pub.init(self)
    
    def test_sendnewemail(self):
        '''发送新邮件'''
        driver = self.driver
        driver.get(self.base_url)# + "/mgt/frame.jsp?url=RA8B4")
        user.login(self)
        time.sleep(3)
        pub.module_icon(self)
        driver.find_element_by_class_name("j_ico_email").click()
        time.sleep(2)
        pub.switchtoframe(self)        
        driver.find_element_by_id("li_1").click()
        time.sleep(5)
        driver.find_element_by_id("tos").send_keys("itaobay@126.com")
        time.sleep(1)
        driver.find_element_by_id("cc").send_keys("itaobay@126.com")
        time.sleep(1)
        now = time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime())
        mailtitle = driver.find_element_by_id("title")
        mailtitle.send_keys(u"邮件标题_%s"%now)
        driver.find_element_by_id("commonUpload_a").click()
        driver.find_element_by_xpath("//input[@name='0']").send_keys("D:\\work\\mgt_webtest\\data\\mailcontent.txt")
        time.sleep(3)
        driver.find_element_by_id("commonUpload_a").click()
        driver.find_element_by_xpath("//input[@name='1']").send_keys("D:\\work\\mgt_webtest\\data\\worklog.txt")
        time.sleep(6)
        driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div[2]/table/tbody/tr/td/div/div[5]/input").click()
        print u"发送邮件成功，邮件主题是：'邮件标题_%s'"%now
        #driver.implicitly_wait(30)
        time.sleep(6)

        #打开收件箱检查是否收到邮件
        driver.get("http://www.126.com")
        time.sleep(3)
        driver.find_element_by_id("idInput").clear()
        driver.find_element_by_id("idInput").send_keys("itaobay")
        time.sleep(2)
        driver.find_element_by_id("pwdInput").clear()
        driver.find_element_by_id("pwdInput").send_keys("guanghui")
        driver.find_element_by_id("loginBtn").click()
        time.sleep(5)
        driver.find_element_by_id("_mail_component_34_34").click()
        time.sleep(5)
        driver.find_element_by_id("_mail_component_40_40").click()
        time.sleep(3)
        newmailtitle = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div[4]/div[2]/div/div[2]/span").text#click()
        #newmailtitle = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div/div/div/div/h1").text
        if newmailtitle == u"邮件标题_%s"%now:
            print u"邮件收到，测试通过！邮件标题是：%s"%newmailtitle
        else:
            driver.get_screenshot_as_file("D:\\work\\mgt_webtest\\screenshot_png\\邮件未收到%s.png"%time.strftime("%Y%m%d%H%M%S",time.localtime()))
            print u"邮件未收到，测试失败，请人工查看原因！"
        driver.delete_all_cookies()
            
    
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
