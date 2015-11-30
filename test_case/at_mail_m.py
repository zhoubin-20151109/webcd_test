#! D:\work\mgt_webtest
#coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re, user, pub
from random import randint
from HTMLTestRunner import HTMLTestRunner
import sys
reload(sys)
sys.setdefaultencoding( 'utf-8' )

class mail_Mob(unittest.TestCase):
    def setUp(self):
        pub.init(self)        

    def test_mail_1(self):
        '''附件预览'''
        driver = self.driver
        driver.get(self.base_url+"/module/mobile/mail/index.m")        
        user.login_m(self)
        time.sleep(2)
        num = randint(2,15)
        time.sleep(3)
        mailurl = driver.find_element_by_xpath("//div[@id='content']/div[%d]/div[2]/div/div"%num)
        mailurl.click()

        #查看详细发件人、收件人信息
        detail = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div[3]/a")
        detail.click()
        sender = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[4]/div/div/table/tbody/tr/td[2]/div").text
        print "发件人：%s"%sender #打印发件人邮箱
        now = time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime())
        try:
            driver.find_element_by_xpath("/html/body/div/div[2]/div/div[6]/div/div/a/span").click()
            driver.get_screenshot_as_file("D:\\work\\mgt_webtest\\screenshot_png\\attprev\\attprev%s.png"%now)
            time.sleep(3)
            driver.find_element_by_xpath("/html/body/div/div/div/div/div/a").click()            
            attachname = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[6]/div/div/a/span").text
            print "附件存在，附件名称是:%s"%attachname
            time.sleep(3)
        except:
            driver.get_screenshot_as_file("D:\\work\\mgt_webtest\\screenshot_png\\attprev\\noatt%s.png"%now)
            print u"附件不存在，详情可见截图：\\screenshot_png\\attprev\\noatt%s.png"%now
            driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/a/i").click()

    def test_mail_2(self):
        '''回复邮件'''
        driver = self.driver
        driver.get(self.base_url+"/module/mobile/mail/index.m")        
        user.login_m(self)
        num = randint(2,15)
        time.sleep(3)
        mailurl = driver.find_element_by_xpath("//div[@id='content']/div[%d]/div[2]/div/div"%num)
        mailurl.click()        
        
        L=open("D:\\work\\mgt_webtest\\data\\mailcontent.txt")
        k=L.readlines()
        L.close()
        i=''
        
        for i in k:
            time.sleep(1)
            driver.find_element_by_xpath("//textarea[@id='mailContent']").clear()
            driver.find_element_by_xpath("//textarea[@id='mailContent']").send_keys('%s'%i)
            time.sleep(2)
            driver.find_element_by_id("send").click()
            if len(i.strip()) == 0:#i.strip()=='':
                driver.get_screenshot_as_file("D:\\work\\mgt_webtest\\screenshot\\mailcontentisnull%s.png"%time.strftime("%Y%m%d%H%M%S",time.localtime()))
                print u'邮件内容为空，不能发送！提示信息可见截图：\\screenshot_png\\mailcontentisnull%s.png'%time.strftime("%Y%m%d%H%M%S",time.localtime())
            else:
                print u'邮件快速回复成功！'#快速回复内容是:%s'%i
            time.sleep(3)
        
    def test_mail_3(self):
        '''删除邮件'''
        driver = self.driver
        driver.get(self.base_url+"/module/mobile/mail/index.m")
        user.login_m(self)
        time.sleep(3)
        
        num = randint(2,15)
        mailurl = driver.find_element_by_xpath("//div[@id='content']/div[%d]/div[2]/div/div"%num)
        mailurl.click()
        time.sleep(1)
        mailtitle = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div").text
        driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div[3]/a").click()
        time.sleep(2)
        print u"邮件删除成功!删除的邮件标题是:%s"%mailtitle
        time.sleep(2)
    
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
