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

class viewLog(unittest.TestCase):
    def setUp(self):
        pub.init(self)
    
    def test_viewlog_01(self):
        '''发布评阅日志'''
        driver = self.driver
        driver.get(self.base_url)     
        user.login(self)
        time.sleep(2)
        self.assertEqual("今目标企业工作平台",driver.title)
        pub.module_icon(self)
        driver.find_element_by_class_name("j_ico_log").click()
        pub.switchtoframe(self)
        driver.find_element_by_xpath("//li[5]/a/strong").click()
        time.sleep(2)
        self.assertEqual("评阅日志",driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div/span").text)
        driver.find_element_by_xpath("//div[@id='viewlogList']/table/tbody/tr/td/div").click()
        time.sleep(2)
        #发布一条为空的评论，查看错误信息提示是否正确
        driver.find_element_by_xpath("//*[@id='btnComment']").click()
        print u"%s"%driver.find_element_by_class_name("valid-error").text
        self.assertEqual(u"请输入评论内容或上传附件！",driver.find_element_by_class_name("valid-error").text)
        time.sleep(2)
        nowtime = time.ctime()
        driver.find_element_by_xpath("//*[@id='logComment']").send_keys(u"经理评阅日志@%s"%nowtime)
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='btnComment']").click()
        print u"经理评阅日志成功！内容为：经理评阅日志@%s"%nowtime
        time.sleep(2)
        driver.switch_to_default_content()
        driver.find_element_by_xpath("//a[contains(text(),'安全退出')]").click()
        time.sleep(2)

        #被评阅的员工查看经理发出的评阅信息
        driver.get(self.base_url)     
        user.login_a(self)
        time.sleep(2)
        self.assertEqual("今目标企业工作平台",driver.title)
        pub.module_icon(self)
        driver.find_element_by_class_name("j_ico_log").click()
        pub.switchtoframe(self)
        driver.find_element_by_xpath("//li[4]/a/strong").click()
        time.sleep(2)
        self.assertEqual("我的评论",driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div/div/div/span").text)
        managerView = driver.find_element_by_xpath("html/body/div/div/div[2]/div[2]/div/table/tbody/tr[1]/td/div[1]/span[1]")
        managerView.text
        self.assertEqual(u'经理评阅日志@%s'%nowtime,managerView.text)
        print u"员工可看到领导发布的评阅信息！"
        user.quit(self)
        driver.close()

    def test_viewlog_02(self):
        '''编辑评阅日志'''
        driver = self.driver
        driver.get(self.base_url)     
        user.login(self)
        time.sleep(2)
        self.assertEqual("今目标企业工作平台",driver.title)
        pub.module_icon(self)
        driver.find_element_by_class_name("j_ico_log").click()
        pub.switchtoframe(self)
        driver.find_element_by_xpath("//li[5]/a/strong").click()
        time.sleep(2)
        self.assertEqual("评阅日志",driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div/span").text)
        driver.find_element_by_xpath("//div[@id='viewlogList']/table/tbody/tr/td/div").click()
        time.sleep(2)
        driver.find_element_by_xpath("//a[contains(text(),'编辑')]").click()
        time.sleep(2)
        nowtime = time.ctime()
        driver.find_element_by_xpath("//*[@id='commentText']").clear()
        driver.find_element_by_xpath("//*[@id='commentText']").send_keys(u"编辑经理评阅日志@%s"%nowtime)
        print u"编辑评阅日志成功！编辑后的评论内容：编辑经理评阅日志@%s"%nowtime
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='editCommentOk']").click()
        time.sleep(2)
        self.assertEqual(u"编辑经理评阅日志@%s"%nowtime,driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[4]/div/div/div[6]/div/table/tbody/tr[2]/td").text)
        user.quit(self)
        driver.close()

    def test_viewlog_03(self):
        '''删除评阅日志'''
        driver = self.driver
        driver.get(self.base_url)     
        user.login(self)
        time.sleep(2)
        self.assertEqual("今目标企业工作平台",driver.title)
        pub.module_icon(self)
        driver.find_element_by_class_name("j_ico_log").click()
        pub.switchtoframe(self)
        driver.find_element_by_xpath("//li[5]/a/strong").click()
        time.sleep(2)
        self.assertEqual("评阅日志",driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div/span").text)
        driver.find_element_by_xpath("//div[@id='viewlogList']/table/tbody/tr/td/div").click()
        time.sleep(2)
        theFirstInfo = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[4]/div/div/div[6]/div/table/tbody/tr[2]/td").text
        driver.find_element_by_xpath("//a[contains(text(),'删除')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//a[contains(text(),'取消')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//a[contains(text(),'删除')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//a[contains(text(),'确定')]").click()
        time.sleep(2)
        #self.verifyEqual(theFirstInfo,driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[4]/div/div/div[6]/div/table/tbody/tr[2]/td").text)
        if theFirstInfo != driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[4]/div/div/div[6]/div/table/tbody/tr[2]/td").text:
            print u"删除成功！"
            print u"删除的评论内容是：%s"%theFirstInfo
        else:
            print u"删除失败"
        user.quit(self)
    
if __name__ == "__main__":
    unittest.main()

