#! D:\work\mgt_webtest
#coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re, user, pub
from random import randint
import sys
reload(sys)
sys.setdefaultencoding( 'utf-8' )

class know_Mob(unittest.TestCase):
    def setUp(self):
        pub.init(self)
    
    def test_knowmob_1(self):
        '''查看详细信息'''
        driver = self.driver
        user.login(self)
        driver.get(self.base_url + "/module/knowledge/index.m")        
        time.sleep(2)
        num = randint(3,16)
        #随机打开首页的一条知识
        driver.find_element_by_xpath("//div[%s]/div/div/a/strong"%num).click()
        time.sleep(1)
        driver.find_element_by_xpath("//a[@id='viewDetail']").click()
        time.sleep(1)
        #检查页面打开是否正确
        self.assertEqual("查看详细",driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/h4/strong").text)
        print u"测试通过，查看详细成功！"
        user.quit_m(self)

    def test_knowmob_2(self):
        '''发表评论'''
        driver = self.driver
        user.login(self)
        driver.get(self.base_url + "/module/knowledge/index.m")        
        time.sleep(2)
        num = randint(3,16)
        driver.find_element_by_xpath("//div[%s]/div/div/a/strong"%num).click()
        time.sleep(1)
        driver.find_element_by_xpath("//button[@id='commBtn']").click()
        time.sleep(1)
        self.assertEqual("评论知识",driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/h4/strong").text)
        comments = open("D:\\work\\mgt_webtest\\data\\know_commentContent.txt")
        comment = comments.readlines()
        comments.close()
        for comm in comment:
            time.sleep(1)
            driver.find_element_by_xpath("//*[@id='commentContent']").clear()
            driver.find_element_by_xpath("//*[@id='commentContent']").send_keys('%s'%comm)
            time.sleep(2)
            driver.find_element_by_xpath("//*[@id='commSubBtn']").click()
            if len(comm.strip()) == 0:#comm.strip()=='':
                driver.get_screenshot_as_file("D:\\work\\mgt_webtest\\screenshot\\knowcommentnull%s.png"%time.strftime("%Y%m%d%H%M%S",time.localtime()))
                print u"评论内容为空！提示信息可见截图：\\screenshot_png\\knowcommentnull%s.png"%time.strftime("%Y%m%d%H%M%S",time.localtime())
            elif len(comm.strip()) > 20000:
                print u"评论内容字符长度大于20000，不允许提交！"
                driver.find_element_by_xpath("//*[@id='commCancel']").click()
            else:
                print u"操作成功！评论内容是:%s"%comm
                time.sleep(1)
                driver.find_element_by_xpath("//button[@id='commBtn']").click()
            time.sleep(3)
        user.quit_m(self)

    def test_knowmob_3(self):
        '''显示较早评论'''
        driver = self.driver
        user.login(self)
        driver.get(self.base_url + "/module/knowledge/index.m")
        time.sleep(2)
        num = randint(3,16)
        driver.find_element_by_xpath("//div[%s]/div/div/a/strong"%num).click()
        time.sleep(1)
        comments = open("D:\\work\\mgt_webtest\\data\\know_commentContent_1.txt")
        comment = comments.readlines()
        comments.close()
        for comm in comment:
            driver.find_element_by_xpath("//button[@id='commBtn']").click()
            time.sleep(2)
            self.assertEqual("评论知识",driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/h4/strong").text)
            driver.find_element_by_xpath("//*[@id='commentContent']").clear()
            #unicode(rst,errors='ignore')
            driver.find_element_by_xpath("//*[@id='commentContent']").send_keys('%s'%comm)
            time.sleep(3)
            driver.find_element_by_xpath("//*[@id='commSubBtn']").click()
            print u"操作成功！评论内容是:%s"%comm
            time.sleep(3)
        self.assertEqual(u"显示较早的评论...",driver.find_element_by_link_text(u"显示较早的评论...").text)
        driver.find_element_by_link_text(u"显示较早的评论...").click()
        time.sleep(3)
        user.quit_m(self)
    
            
            
if __name__=="__main__":
    unittest.main()
        

        