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

class projectStatus(unittest.TestCase):
    def setUp(self):
        pub.init(self)
    
    def test_project_add(self):
        '''新建项目'''
        driver = self.driver
        #driver.get(self.base_url)# + "/mgt/frame.jsp?url=MGT_PROJECT_MY")        
        user.login(self)
        time.sleep(2)
        self.assertEqual("今目标企业工作平台",driver.title)
        pub.module_icon(self)
        driver.find_element_by_class_name("j_ico_project").click()
        pub.switchtoframe(self)
        driver.find_element_by_id("realname").click()
        time.sleep(1)
        now = time.strftime('%Y%m%d_%H%M%S',time.localtime())
        driver.find_element_by_id("targetName").send_keys(u"项目名称_%s"%now)
        time.sleep(1)
        f1 = driver.find_element_by_xpath("//span/table/tbody/tr[2]/td/iframe")#/html/body/div[5]/div/div[2]/div/div/div[2]/table/tbody/tr[3]/td/div/span/table/tbody/tr[2]/td/iframe")
        driver.switch_to_frame(f1)
        driver.find_element_by_xpath("//*[@id='tinymce']").send_keys(u"项目描述@%s"%time.ctime()) 
        driver.switch_to_default_content()
        pub.switchtoframe(self)
        time.sleep(1)
        driver.find_element_by_id("beginDateCheckBox").click()
        time.sleep(1)
        driver.find_element_by_id("endDateCheckBox").click()
        time.sleep(1)
        driver.find_element_by_xpath("//a[@id='selectUserListBtnHref']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//input[@id='userListSelectSelfInput']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//input[@id='userListSubmitButton']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='submitAdd']").click()
        time.sleep(1)
        driver.find_element_by_id("confirmOk").click()
        print u"新建项目成功！项目名称_%s"%now
        time.sleep(2)
        user.quit(self)

    def test_project_status_1(self):
        '''完成项目'''
        driver = self.driver
        driver.get(self.base_url)# + "/mgt/frame.jsp?url=MGT_PROJECT_MY")        
        user.login(self)
        time.sleep(2)
        pub.module_icon(self)
        driver.find_element_by_class_name("j_ico_project").click()
        pub.switchtoframe(self)
        #筛选状态为进行中的项目，将第一个项目状态置为已完成
        driver.find_element_by_id("statusFilter").click()
        time.sleep(0.5)
        filt = driver.find_element_by_id("mainStatusChange")
        time.sleep(1)
        filt.find_element_by_xpath("//option[@value='0']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//td[3]/a").click()
        time.sleep(2)
        #点击完成按钮
        driver.find_element_by_xpath("//div[4]/div/div[2]/span").click()
        time.sleep(2)
        okreason = driver.find_element_by_id("MgtPopup-Popup")
        okreason.find_element_by_id("reason").clear()
        okreason.find_element_by_id("reason").send_keys(u"项目已完成！")
        time.sleep(2)
        okreason.find_element_by_xpath("//input[@value='提交']").click()
        time.sleep(1)
        driver.find_element_by_id("mgtConfirmDivId").find_element_by_id("confirmOk").click()
        time.sleep(1)
        oktext = driver.find_element_by_id("mgtAlertDivId").find_element_by_class_name("alertContentClass")
        oktext.text
        if oktext.text == u"修改成功":
            print u"项目已完成！" 
            driver.find_element_by_id("mgtAlertDivId").find_element_by_id("buttonOk").click()
            user.quit(self)
        else:
            print u"项目修改失败！！！"
            user.quit(self)

    def test_project_status_2(self):
        '''激活项目'''
        driver = self.driver
        driver.get(self.base_url)# + "/mgt/frame.jsp?url=MGT_PROJECT_MY")        
        user.login(self)
        time.sleep(2)
        pub.module_icon(self)
        driver.find_element_by_class_name("j_ico_project").click()
        pub.switchtoframe(self)
        #筛选状态为已完成的项目，撤销第一个项目
        driver.find_element_by_id("statusFilter").click()
        time.sleep(0.5)
        filt = driver.find_element_by_id("mainStatusChange")
        time.sleep(1)
        filt.find_element_by_xpath("//option[@value='2']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//td[3]/a").click()
        time.sleep(2)
        #点击激活按钮
        driver.find_element_by_xpath("//div[2]/div/div[2]/span").click()
        time.sleep(2)
        actReason=driver.find_element_by_xpath("//*[@id='MgtPopup-Popup']")        
        actReason.find_element_by_xpath("//*[@id='reason']").clear()
        driver.find_element_by_xpath("//*[@id='reason']").send_keys(u"激活理由@%s"%time.ctime())
        print u"项目已激活成功！"
        time.sleep(2)
        actReason.find_element_by_xpath("//input[@value='提交']").click()
        time.sleep(1)
        driver.find_element_by_id("mgtConfirmDivId").find_element_by_id("confirmOk").click()
        time.sleep(2)
        driver.find_element_by_id("mgtAlertDivId").find_element_by_id("buttonOk").click()
        time.sleep(1)
        print u"项目已激活！"
        user.quit(self)
        
    def test_project_status_3(self):
        '''撤销项目'''
        driver = self.driver
        driver.get(self.base_url)# + "/mgt/frame.jsp?url=MGT_PROJECT_MY")        
        user.login(self)
        time.sleep(2)
        pub.module_icon(self)
        driver.find_element_by_class_name("j_ico_project").click()
        pub.switchtoframe(self)
        #筛选状态为进行中的项目，撤销列表中的第一个项目
        driver.find_element_by_id("statusFilter").click()
        time.sleep(0.5)
        filt = driver.find_element_by_id("mainStatusChange")
        time.sleep(1)
        filt.find_element_by_xpath("//option[@value='0']").click()
        time.sleep(1)
        pro_name = driver.find_element_by_xpath("//td[3]/a")
        #pro_name.text
        pro_name.click()
        time.sleep(2)
        #点击撤销按钮
        driver.find_element_by_xpath("//div[3]/div/div[2]/span").click()
        time.sleep(2)
        cancelReason = driver.find_element_by_id("MgtPopup-Popup")
        cancelReason.find_element_by_id("reason").clear()
        cancelReason.find_element_by_id("reason").send_keys(u"项目需要撤销！")
        time.sleep(2)
        cancelReason.find_element_by_xpath("//input[@value='提交']").click()
        time.sleep(1)
        driver.find_element_by_id("mgtConfirmDivId").find_element_by_id("confirmOk").click()
        time.sleep(2)
        driver.find_element_by_id("mgtAlertDivId").find_element_by_id("buttonOk").click()
        time.sleep(1)
        print u"项目已撤销！"
        user.quit(self)

    def test_project_status_4(self):
        '''恢复项目'''
        driver = self.driver
        user.login(self)
        time.sleep(2)
        pub.module_icon(self)
        driver.find_element_by_class_name("j_ico_project").click()
        pub.switchtoframe(self)
        #过滤为已撤销的项目，恢复列表中的第一个项目
        driver.find_element_by_id("statusFilter").click()
        time.sleep(0.5)
        filt = driver.find_element_by_id("mainStatusChange")
        time.sleep(1)
        filt.find_element_by_xpath("//option[@value='1']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//td[3]/a").click()
        time.sleep(2)
        #点击恢复按钮
        driver.find_element_by_xpath("//div[2]/div/div[2]/span").click()
        time.sleep(2)
        resReason=driver.find_element_by_xpath("//*[@id='MgtPopup-Popup']")
        resReason.find_element_by_xpath("//*[@id='reason']").clear()
        driver.find_element_by_xpath("//*[@id='reason']").send_keys(u"恢复理由@%s"%time.ctime())
        time.sleep(2)
        resReason.find_element_by_xpath("//input[@value='提交']").click()
        time.sleep(1)
        driver.find_element_by_id("mgtConfirmDivId").find_element_by_id("confirmOk").click()
        time.sleep(2)
        driver.find_element_by_id("mgtAlertDivId").find_element_by_id("buttonOk").click()
        time.sleep(1)
        print u"项目已恢复！"
        user.quit(self)

    def test_project_status_5(self):
        '''修改项目'''
        driver = self.driver
        user.login(self)
        time.sleep(2)
        pub.module_icon(self)
        driver.find_element_by_class_name("j_ico_project").click()
        pub.switchtoframe(self)
        #筛选状态为实现中的项目，修改第一个项目
        driver.find_element_by_id("statusFilter").click()
        time.sleep(0.5)
        filt = driver.find_element_by_id("mainStatusChange")
        time.sleep(1)
        filt.find_element_by_xpath("//option[@value='0']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//td[3]/a").click()
        time.sleep(2)
        driver.find_element_by_xpath("//input[@value='修改']").click()
        time.sleep(2)
        driver.find_element_by_id("targetName").clear()
        driver.find_element_by_id("targetName").send_keys(u"修改项目名称_%s"%time.strftime("%Y%m%d_%H%M%S",time.localtime()))
        time.sleep(2)
        driver.find_element_by_id("editTargetReason").clear()
        driver.find_element_by_id("editTargetReason").send_keys(u"修改理由@%s"%time.ctime())
        time.sleep(2)
        driver.find_element_by_id("submitAdd").click()
        time.sleep(1)
        driver.find_element_by_id("mgtConfirmDivId").find_element_by_id("confirmOk").click()
        print u"修改成功！修改理由@%s"%time.ctime()
        time.sleep(2)
        user.quit(self)
        
if __name__ == "__main__":
    unittest.main()