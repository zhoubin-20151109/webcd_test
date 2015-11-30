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

class myComment(unittest.TestCase):
    def setUp(self):
        pub.init(self)
    
    def test_mycomment_01(self):
        '''评论标签切换'''
        driver = self.driver
        driver.get(self.base_url)     
        user.login(self)
        time.sleep(2)
        self.assertEqual("今目标企业工作平台",driver.title)
        pub.module_icon(self)
        driver.find_element_by_class_name("j_ico_log").click()
        pub.switchtoframe(self)
        driver.find_element_by_xpath("//li[4]/a/strong").click()
        time.sleep(2)
        self.assertEqual("我的评论",driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div/div/div/span").text)
        driver.find_element_by_xpath("//div[2]/div/div/ul/li[2]/a").click()
        time.sleep(2)
        driver.find_element_by_xpath("//a[contains(@href, 'mycomment.do?type=received')]").click()
        print u"测试通过！"
        time.sleep(2)
        user.quit(self)
        
    def test_mycomment_02(self):
        '''编辑发出的评论'''
        driver = self.driver
        driver.get(self.base_url)     
        user.login(self)
        time.sleep(2)
        self.assertEqual("今目标企业工作平台",driver.title)
        pub.module_icon(self)
        driver.find_element_by_class_name("j_ico_log").click()
        pub.switchtoframe(self)
        driver.find_element_by_xpath("//li[4]/a/strong").click()
        time.sleep(2)
        self.assertEqual("我的评论",driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div/div/div/span").text)
        driver.find_element_by_xpath("//div[2]/div/div/ul/li[2]/a").click()
        time.sleep(2)
        driver.find_element_by_xpath("//a[contains(text(),'编辑')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='commentText']").clear()
        nowtime = time.ctime()
        driver.find_element_by_xpath("//*[@id='commentText']").send_keys(u"编辑发出的评论%s"%nowtime)
        #time.sleep(2)
        driver.find_element_by_xpath("//*[@id='editCommentOk']").click()
        time.sleep(2)
        self.assertEqual(u"编辑发出的评论%s"%nowtime,driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/table/tbody/tr[1]/td/div[1]/span[1]").text)
        print u"修改成功！"
        user.quit(self)
        
    def test_mycomment_03(self):
        '''删除发出的评论'''
        driver = self.driver
        driver.get(self.base_url)     
        user.login(self)
        time.sleep(2)
        self.assertEqual("今目标企业工作平台",driver.title)
        pub.module_icon(self)
        driver.find_element_by_class_name("j_ico_log").click()
        pub.switchtoframe(self)
        driver.find_element_by_xpath("//li[4]/a/strong").click()
        time.sleep(2)
        self.assertEqual("我的评论",driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div/div/div/span").text)
        driver.find_element_by_xpath("//div[2]/div/div/ul/li[2]/a").click()
        time.sleep(2)
        del_before = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/table/tbody/tr[1]/td/div[1]/span[1]").text
        driver.find_element_by_xpath("//a[contains(text(),'删除')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//a[contains(text(),'取消')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//a[contains(text(),'删除')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//a[contains(text(),'确定')]").click()
        time.sleep(2)
        del_after = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/table/tbody/tr[1]/td/div[1]/span[1]").text
        if del_after != del_before:
            print u"删除成功！目前最新的评论内容是：%s"%del_after
        else:
            print u"删除失败！"
        user.quit(self)

if __name__ == "__main__":
    unittest.main()
