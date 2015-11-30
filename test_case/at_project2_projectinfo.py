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

def project_info(self):
    '''打开状态为实现中的第一个项目'''
    driver = self.driver
    driver.get(self.base_url)# + "/mgt/frame.jsp?url=MGT_PROJECT_MY")        
    user.login(self)
    time.sleep(2)
    pub.module_icon(self)
    driver.find_element_by_class_name("j_ico_project").click()
    pub.switchtoframe(self)
    #筛选状态为进行中的项目，给第一个项目新建协商
    driver.find_element_by_id("statusFilter").click()
    time.sleep(0.5)
    filt = driver.find_element_by_id("mainStatusChange")
    time.sleep(1)
    filt.find_element_by_xpath("//option[@value='0']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//td[3]/a").click()
    time.sleep(2)

class projectInfo(unittest.TestCase):
    def setUp(self):
        pub.init(self)

    def test_project_info_1(self):
        '''新建协商'''
        driver = self.driver
        project_info(self)
        driver.find_element_by_xpath("//a[contains(text(),'协商')]").click()
        time.sleep(1)
        driver.find_element_by_id("realname").click()
        time.sleep(2)
        now = time.strftime("%Y%m%d_%H%M%S",time.localtime())
        driver.find_element_by_id("title").send_keys(u"新建协商主题_%s"%now)
        time.sleep(2)
        f2 = driver.find_element_by_xpath("//span/table/tbody/tr[2]/td/iframe")
        driver.switch_to_frame(f2)
        driver.find_element_by_xpath("//*[@id='tinymce']").send_keys(u"协商内容@%s"%time.ctime())
        driver.switch_to_default_content()
        pub.switchtoframe(self)
        driver.find_element_by_link_text(u"上传附件").click()
        time.sleep(1)
        driver.find_element_by_xpath("//input[@name='0']").send_keys("D:\\work\\mgt_webtest\\data\\know_commentContent.txt")
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='connsubmit']").click()
        time.sleep(2)
        driver.find_element_by_id("mgtConfirmDivId").find_element_by_id("confirmOk").click()
        time.sleep(2)
        title = driver.find_element_by_xpath("//table/tbody/tr[2]/td[2]/div[1]/a")
        self.assertEqual(u"新建协商主题_%s"%now,title.text)
        print u"新建协商成功！标题为：新建协商主题_%s"%now
        user.quit(self)
        
    def test_project_info_2(self):
        '''添加文档'''
        driver = self.driver
        project_info(self)
        driver.find_element_by_link_text(u"文档").click()
        time.sleep(2)
        driver.find_element_by_id("realname").click()
        time.sleep(2)
        now = time.strftime("%Y%m%d_%H%M%S",time.localtime())
        driver.find_element_by_id("title").send_keys(u"添加文档_%s"%now)
        driver.find_element_by_link_text(u"上传附件").click()
        time.sleep(2)
        driver.find_element_by_link_text(u"删除").click()
        time.sleep(2)
        driver.find_element_by_link_text(U"上传附件").click()
        driver.find_element_by_xpath("//input[@type='file']").send_keys("D:\\work\\mgt_webtest\\data\\know_commentContent.txt")
        time.sleep(2)
        driver.find_element_by_id("connsubmit").click()
        time.sleep(2)
        driver.find_element_by_id("mgtConfirmDivId").find_element_by_id("confirmOk").click()
        time.sleep(2)
        title = driver.find_element_by_xpath("//div[2]/div[2]/div[2]/table/tbody/tr[2]/td[2]")
        title.text
        self.assertEqual(u"添加文档_%s"%now,title.text)
        print u"添加文档成功！标题为：添加文档_%s"%now
        user.quit(self)
        
    def test_project_info_3(self):
        '''编辑人员'''
        driver = self.driver
        project_info(self)
        driver.find_element_by_link_text(u"人员").click()
        time.sleep(2)
        driver.find_element_by_link_text(u"删除参与人").click()
        time.sleep(2)
        driver.find_element_by_id("reason_form").find_element_by_id("reason").send_keys(u"删除理由_%s"%pub.now())
        time.sleep(3)
        driver.find_element_by_id("MgtPopup-Popup").find_element_by_xpath("//input[@value='提交']").click()
        time.sleep(2)
        driver.find_element_by_id("mgtConfirmDivId").find_element_by_id("confirmOk").click()
        time.sleep(2)
        driver.find_element_by_id("buttonOk").click()
        time.sleep(2)
        driver.find_element_by_id("realname").click()
        time.sleep(2)
        driver.find_element_by_link_text(u"设置参与人").click()
        time.sleep(2)
        driver.find_element_by_id("userListSelectSelfInput").click()
        time.sleep(2)
        driver.find_element_by_id("userListSubmitButton").click()
        time.sleep(2)
        driver.find_element_by_id("addUserReason").send_keys(u"编辑人员原因:%s"%pub.now())
        time.sleep(2)
        driver.find_element_by_id("submitAdd").click()
        time.sleep(2)
        driver.find_element_by_id("confirmOk").click()
        print u"修改成功！"
        time.sleep(2)
        user.quit(self)

    def test_project_info_4(self):
        '''新建子项目'''
        driver = self.driver
        project_info(self)
        driver.find_element_by_link_text(u"子项目").click()
        time.sleep(2)
        driver.find_element_by_id("realname").click()
        time.sleep(2)
        driver.find_element_by_id("targetName").send_keys(u"子项目名称_%s"%pub.now())
        time.sleep(2)
        f1 = driver.find_element_by_xpath("//table/tbody/tr[3]/td/div/span/table/tbody/tr[2]/td/iframe")
        driver.switch_to_frame(f1)
        driver.find_element_by_id("tinymce").send_keys(u"项目描述@%s"%pub.now())
        driver.switch_to_default_content()
        pub.switchtoframe(self)
        driver.find_element_by_id("beginDateCheckBox").click()
        time.sleep(1)
        driver.find_element_by_id("endDateCheckBox").click()
        time.sleep(2)
        driver.find_element_by_id("submitAdd").click()
        time.sleep(2)
        driver.find_element_by_id("confirmOk").click()
        time.sleep(2)
        print u"子项目创建成功！"
        user.quit(self)

    def test_project_info_5(self):
        '''转移子项目'''
        driver = self.driver
        project_info(self)
        
    

if __name__ == "__main__":
    unittest.main()
