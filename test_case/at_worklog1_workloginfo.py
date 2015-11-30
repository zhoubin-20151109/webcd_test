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

class workLogInfo(unittest.TestCase):
    def setUp(self):
        pub.init(self)
    
    def test_todaylog_01(self):
        '''新建日计划'''
        driver = self.driver
        driver.get(self.base_url)     
        user.login(self)
        time.sleep(2)
        self.assertEqual("今目标企业工作平台",driver.title)
        pub.module_icon(self)
        driver.find_element_by_class_name("j_ico_log").click()
        pub.switchtoframe(self)
        driver.find_element_by_xpath("//a[@id='newOrEditPendingMatter']").click()
        time.sleep(1)
        #使用二次定位的方法找到日计划对话框
        dayplan = driver.find_element_by_id("myModalDayPlan").find_element_by_id("dayPlanContent")
        dayplan.send_keys(u"今日日计划_%s"%time.strftime("%Y_%m_%d-%H_%M_%S",time.localtime()))
        time.sleep(1)
        driver.find_element_by_id("btn_worklog_ok_dayPlan").click()
        time.sleep(1)
        print u"日计划创建成功！内容为:今日日计划_%s"%time.strftime("%Y_%m_%d-%H_%M_%S",time.localtime())
        user.quit(self)
        
    def test_todaylog_02(self):
        '''日计划状态修改'''
        driver = self.driver
        driver.get(self.base_url)# + "/module/worklog/userfo.do?locale=zh_CN")        
        user.login(self)
        time.sleep(2)
        self.assertEqual("今目标企业工作平台",driver.title)
        pub.module_icon(self)
        driver.find_element_by_class_name("j_ico_log").click()
        pub.switchtoframe(self)
        planstatus = driver.find_element_by_xpath("//td/a/i")
        if planstatus.get_attribute('class') == 'mpic-deny':
            driver.find_element_by_css_selector('i.mpic-deny').click()
            print u"状态修改为已完成！"
        else:
            driver.find_element_by_css_selector('i.mpic-ok').click()
            print u"状态修改为未完成！"
        time.sleep(2)
        user.quit(self)

    def test_todaylog_03(self):
        '''删除日计划'''
        driver = self.driver
        driver.get(self.base_url)# + "/module/worklog/userfo.do?locale=zh_CN")        
        user.login(self)
        time.sleep(2)
        self.assertEqual("今目标企业工作平台",driver.title)
        pub.module_icon(self)
        driver.find_element_by_class_name("j_ico_log").click()
        pub.switchtoframe(self)
        driver.find_element_by_xpath("//td[3]/a/i").click()
        time.sleep(1)
        dayplan_del = driver.find_element_by_id("myModalDayPlan").find_element_by_id("btn_worklog_delete_dayPlan")
        dayplan_del.click()
        time.sleep(2)
        driver.find_element_by_xpath("//a[contains(text(),'取消')]").click()#取消删除
        time.sleep(1)
        dayplan_del.click()
        time.sleep(1)
        driver.find_element_by_xpath("//a[contains(text(),'确定')]").click()#确认删除
        time.sleep(2)
        print u"日计划删除成功！"
        user.quit(self)

    
    def test_todaylog_04(self):
        '''新建工作记录'''
        driver = self.driver
        driver.get(self.base_url)# + "/module/worklog/userfo.do?locale=zh_CN")        
        user.login(self)
        time.sleep(2)
        self.assertEqual("今目标企业工作平台",driver.title)
        pub.module_icon(self)
        driver.find_element_by_class_name("j_ico_log").click()
        pub.switchtoframe(self)        
        driver.find_element_by_xpath("//a[contains(text(),'新建工作记录')]").click()
        time.sleep(2)
        #使用二次定位的方法找到对话框中的文本框
        worklog = driver.find_element_by_id("myModal").find_element_by_id("modalContent")
        worklog.send_keys(u"工作记录:%s"%time.strftime("%Y_%m_%d-%H_%M_%S",time.localtime()))
        time.sleep(1)
        driver.find_element_by_id("btn_worklog_ok").click()
        time.sleep(2)
        print u"工作记录:%s"%time.strftime("%Y_%m_%d-%H_%M_%S",time.localtime())
        user.quit(self)        
    
    def test_todaylog_05(self):
        '''修改工作记录'''
        driver = self.driver
        driver.get(self.base_url)# + "/module/worklog/userfo.do?locale=zh_CN")        
        user.login(self)
        time.sleep(2)
        self.assertEqual("今目标企业工作平台",driver.title)
        pub.module_icon(self)
        driver.find_element_by_class_name("j_ico_log").click()
        pub.switchtoframe(self)
        try:
            driver.find_element_by_xpath("//td[3]/a/i").click()        
            time.sleep(1)
            #使用二次定位的方法找到对话框中的文本框
            div = driver.find_element_by_id("myModal").find_element_by_id("modalContent")
            nowtime = time.strftime("%Y_%m_%d-%H_%M_%S",time.localtime())
            div.clear()
            div.send_keys(u"第一个工作记录：%s"%nowtime)
            print u"修改成功！内容如下：今天的第一个工作记录：%s"%nowtime
            time.sleep(2)
            driver.find_element_by_id("btn_worklog_ok").click()
            time.sleep(2)
        except NoSuchElementException, e:
            print u"数据尚未创建！"
            return False
        finally:
            user.quit(self)
            
    def test_todaylog_06(self):
        '''新建今日工作小结'''
        driver = self.driver
        driver.get(self.base_url)# + "/module/worklog/userfo.do?locale=zh_CN")        
        user.login(self)
        time.sleep(2)
        self.assertEqual("今目标企业工作平台",driver.title)
        pub.module_icon(self)
        driver.find_element_by_class_name("j_ico_log").click()
        pub.switchtoframe(self)
        #点击新建工作小结链接，并输入数据创建；若已创建，则打印已创建
        try:
            driver.find_element_by_xpath("//a[contains(text(),'新建工作小结')]").click()        
            time.sleep(2)
            #使用二次定位的方法找到对话框中的文本框
            worksumm = driver.find_element_by_id("myModal").find_element_by_id("modalContent")
            nowtime = time.strftime("%Y_%m_%d-%H_%M_%S",time.localtime())
            worksumm.send_keys(u"今日工作小结：%s"%nowtime)
            print u"工作小结新建成功！内容如下：今日工作小结：%s"%nowtime
            driver.find_element_by_id("btn_worklog_ok").click()
            time.sleep(2)
        except NoSuchElementException, e:
            print u"今日工作小结已创建！"      
        finally:
            user.quit(self)    

    def test_todaylog_07(self):
        '''上传附件'''
        driver = self.driver
        driver.get(self.base_url)# + "/module/worklog/userfo.do?locale=zh_CN")        
        user.login(self)
        time.sleep(2)
        self.assertEqual("今目标企业工作平台",driver.title)
        pub.module_icon(self)
        driver.find_element_by_class_name("j_ico_log").click()
        pub.switchtoframe(self)        
        driver.find_element_by_xpath("//a[contains(text(),'上传附件')]").click()
        time.sleep(1)
        upatt = driver.find_element_by_id("attachForm").find_element_by_id("mgtfile")
        upatt.send_keys("D:\\work\\mgt_webtest\\data\\mailcontent.txt")
        print u"上传附件成功！"
        time.sleep(2)
        driver.find_element_by_id("myModal").find_element_by_id("btn_worklog_ok").click()
        time.sleep(2)
        user.quit(self)

    def test_todaylog_08(self):
        '''预览附件'''
        driver = self.driver
        driver.get(self.base_url)# + "/module/worklog/userfo.do?locale=zh_CN")        
        user.login(self)
        time.sleep(2)
        self.assertEqual("今目标企业工作平台",driver.title)
        pub.module_icon(self)
        driver.find_element_by_class_name("j_ico_log").click()
        pub.switchtoframe(self)
        nowhandle = driver.current_window_handle
        driver.find_element_by_xpath("//a[contains(text(),'预览')]").click()
        time.sleep(2)
        allhandles = driver.window_handles
        for handle in allhandles:
            if handle != nowhandle:
                driver.switch_to_window(handle)
                time.sleep(2)
                driver.get_screenshot_as_file("D:\\work\\mgt_webtest\\screenshot\\dayplan_attachpreview%s.png"%time.strftime("%Y%m%d_%H%M%S",time.localtime()))
                print u"预览成功，截图在screenshot目录下！"
                driver.close()
        driver.switch_to_window(nowhandle)
        time.sleep(3)
        user.quit(self)

    def test_todaylog_09(self):
        '''查看访问记录'''
        driver = self.driver
        driver.get(self.base_url)# + "/module/worklog/userfo.do?locale=zh_CN")        
        user.login(self)
        time.sleep(2)
        self.assertEqual("今目标企业工作平台",driver.title)
        pub.module_icon(self)
        driver.find_element_by_class_name("j_ico_log").click()
        pub.switchtoframe(self)
        driver.find_element_by_xpath("//a[contains(text(),'访问记录')]").click()
        time.sleep(1)
        print u"访问记录查看成功!"
        user.quit(self)
        
    
    def test_todaylog_10(self):
        '''删除附件'''
        driver = self.driver
        driver.get(self.base_url)# + "/module/worklog/userfo.do?locale=zh_CN")        
        user.login(self)
        time.sleep(2)
        self.assertEqual("今目标企业工作平台",driver.title)
        pub.module_icon(self)
        driver.find_element_by_class_name("j_ico_log").click()
        pub.switchtoframe(self)
        driver.find_element_by_xpath("//a[contains(text(),'删除')]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//a[contains(text(),'取消')]").click()#取消删除
        time.sleep(1)
        driver.find_element_by_xpath("//a[contains(text(),'删除')]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//a[contains(text(),'确定')]").click()#确定删除
        print u"删除成功!"
        time.sleep(2)
        user.quit(self)

    def test_todaylog_11(self):
        '''发表评论'''
        driver = self.driver
        driver.get(self.base_url)#+ "/module/worklog/userfo.do?locale=zh_CN")        
        user.login(self)
        time.sleep(2)
        self.assertEqual("今目标企业工作平台",driver.title)
        pub.module_icon(self)
        driver.find_element_by_class_name("j_ico_log").click()
        pub.switchtoframe(self)
        driver.find_element_by_xpath("//*[@id='logComment']").send_keys(u"发表评论@%s"%time.ctime())
        print u"发表评论内容为：发表评论@%s"%time.ctime()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='btnComment']").click()
        time.sleep(3)
        user.quit(self)
        
    def test_todaylog_12(self):
        '''修改评论'''
        driver = self.driver
        driver.get(self.base_url)#+ "/module/worklog/userfo.do?locale=zh_CN")        
        user.login(self)
        time.sleep(2)
        self.assertEqual("今目标企业工作平台",driver.title)
        pub.module_icon(self)
        driver.find_element_by_class_name("j_ico_log").click()
        pub.switchtoframe(self)
        driver.find_element_by_xpath("//a[contains(text(),'编辑')]").click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='commentText']").clear()
        driver.find_element_by_xpath("//*[@id='commentText']").send_keys(u"编辑评论@%s"%time.ctime())
        print u"评论内容修改为：编辑评论@%s"%time.ctime()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='editCommentOk']").click()
        time.sleep(2)
        user.quit(self)

    def test_todaylog_13(self):
        '''删除评论'''
        driver = self.driver
        driver.get(self.base_url)#+ "/module/worklog/userfo.do?locale=zh_CN")        
        user.login(self)
        time.sleep(2)
        self.assertEqual("今目标企业工作平台",driver.title)
        pub.module_icon(self)
        driver.find_element_by_class_name("j_ico_log").click()
        pub.switchtoframe(self)
        time.sleep(2)
        driver.find_element_by_xpath("//a[contains(text(),'删除')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//a[contains(text(),'取消')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//a[contains(text(),'删除')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//a[contains(text(),'确定')]").click()
        time.sleep(2)
        print u"删除评论成功！"
        user.quit(self)
        
    def test_todaylog_14(self):
        '''创建昨日补充日志'''
        driver = self.driver
        driver.get(self.base_url)     
        user.login(self)
        time.sleep(2)
        self.assertEqual("今目标企业工作平台",driver.title)
        pub.module_icon(self)
        driver.find_element_by_class_name("j_ico_log").click()
        pub.switchtoframe(self)
        driver.find_element_by_css_selector("i.mpic-back").click()
        time.sleep(2)
        driver.find_element_by_xpath("//a[@id='supplementTip']").click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="modalContent"]').clear()
        driver.find_element_by_xpath('//*[@id="modalContent"]').send_keys(u"补充日志@%s"%time.ctime())
        time.sleep(2)
        driver.find_element_by_xpath("//button[@id='btn_worklog_ok']").click()
        print u"补充昨日日志成功!"
        time.sleep(2)
        driver.find_element_by_xpath("//a[contains(text(),'今天')]").click()
        time.sleep(2)
        user.quit(self)
        
    def test_todaylog_15(self):
        '''查看本周计划'''
        driver = self.driver
        driver.get(self.base_url)     
        user.login(self)
        time.sleep(2)
        self.assertEqual("今目标企业工作平台",driver.title)
        pub.module_icon(self)
        driver.find_element_by_class_name("j_ico_log").click()
        pub.switchtoframe(self)
        driver.find_element_by_xpath("//a[contains(text(),'本周计划')]").click()
        driver.get_screenshot_as_file("D:\\work\\mgt_webtest\\screenshot\\worklogtoweekplan%s"%time.strftime("%Y%m%d_%H%M%S",time.localtime()))
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='modal4weekplan']/div/button").click()#//button[@type='button'])[2]
        user.quit(self)

if __name__ == "__main__":
    unittest.main()