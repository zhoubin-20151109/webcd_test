#coding=utf-8
#个人设置重构的自动化测试用例
#Author：dengrong

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from random import randint
import unittest, time, re, user, pub
# import sys
# reload(sys)
# sys.setdefaultencoding( 'utf-8' )

def goTo(self):
    driver = self.driver
    user.logins(self,'0282@0101005','abc12345')
    time.sleep(2)
    print driver.title
    driver.switch_to_frame("mgt_workbench_iframe")
    driver.find_element_by_css_selector("a.blue1").click()
    # lc.findCss(driver,"a.blue1").click()
    time.sleep(2)

class selfSetUp(unittest.TestCase):
    def setUp(self):
        pub.init(self)

    def tearDown(self):
        self.driver.close()
        self.driver.delete_all_cookies()

    def test_self_setup_01(self):
        '''语言设置：设置为繁体'''
        driver = self.driver
        goTo(self)
        lang = driver.find_element_by_id("showLang").text
        driver.find_element_by_id("modifyLangBtn").click()
        time.sleep(1)
        if lang == u"中文简体":
            langset = driver.find_element_by_id("langSel")
            langset.find_element_by_xpath("//option[@value='zh_TW']").click()
            time.sleep(1)
            driver.find_element_by_id("modifyLangSubmitBtn").click()
            time.sleep(2)
            driver.switch_to_frame("mgt_workbench_iframe")
            try:
                self.assertEqual(u"今目標企業工作平臺",driver.title)
                print u"设置为中文繁体语言成功！"
            except AssertionError:
                driver.get_screenshot_as_file(u"D:\\work\\mgt_webtest\\screenshot\\设置繁体失败_%s.png"%pub.now())
                print u"设置为中文繁体语言失败！已截图保存至D:\\work\\mgt_webtest\\screenshot\\设置繁体失败_%s.png"%pub.now()
        else:
            pass
            
    def test_self_setup_02(self):
        '''语言设置：设置为简体'''
        driver = self.driver
        goTo(self)
        lang = driver.find_element_by_id("showLang").text
        driver.find_element_by_id("modifyLangBtn").click()
        time.sleep(1)
        if lang == u"中文繁體":
            langset = driver.find_element_by_id("langSel")
            langset.find_element_by_xpath("//option[@value='zh_CN']").click()
            time.sleep(1)
            driver.find_element_by_id("modifyLangSubmitBtn").click()
            time.sleep(2)
            driver.switch_to_frame("mgt_workbench_iframe")
            try:
                self.assertEqual(u"今目标企业工作平台",driver.title)
                print u"设置为中文简体语言成功！"
            except AssertionError:
                driver.get_screenshot_as_file(u"D:\\work\\mgt_webtest\\screenshot\\设置简体失败_%s.png"%pub.now())
                print u"设置为中文简体语言失败！已截图保存至D:\\work\\mgt_webtest\\screenshot\\设置简体失败_%s.png"%pub.now()
        else:
            pass

    def test_self_setup_03(self):
        '''查看权限'''
        driver = self.driver
        goTo(self)
        driver.find_element_by_link_text(u"查看权限").click()
        print u"查看权限成功！"
        time.sleep(2)
        driver.find_element_by_xpath("//button[@id='modalClose']").click()
        # user.quit(self)

    def test_self_setup_04(self):
        '''修改手机号:异常'''
        driver = self.driver
        goTo(self)
        mobileBook = open("D:\\work\\mgt_webtest\\data\\mobilebook.txt")
        mobileNo = mobileBook.readlines()
        mobileBook.close()
        driver.find_element_by_xpath("//div[@id='modifymobile']/a").click()
        for phoneNo in mobileNo:
            driver.find_element_by_id("bindmobile").clear()
            driver.find_element_by_id("bindmobile").send_keys(u"%s"%phoneNo)
            time.sleep(1)
            try:
                driver.find_element_by_xpath("//a[@type='button']").click()
                time.sleep(2)
            except:
                print u'修改成功！'
            showNo = driver.find_element_by_id("notificationstop-center").text
            print u"%s此次输入的号码是：%s"%(showNo,phoneNo)
        #driver.find_element_by_xpath("//a[contains(text(),'取消')]").click()

    def test_self_setup_05(self):
        '''修改手机号:正常'''
        driver = self.driver
        goTo(self)
        phoneNo = randint(10000000000,99999999999)
        driver.find_element_by_xpath("//div[@id='modifymobile']/a").click()
        driver.find_element_by_id("bindmobile").clear()
        driver.find_element_by_id("bindmobile").send_keys("%s"%phoneNo)
        driver.find_element_by_xpath("//a[@type='button']").click()
        time.sleep(2)
        showNo = driver.find_element_by_id("notificationstop-center").text        
        print u"%s绑定手机号已修改为：18628055581"%showNo
        # user.quit(self)

    def test_self_setup_06(self):
        '''绑定邮箱：正常(若已绑定则打印出已绑定的邮箱)'''
        driver = self.driver
        goTo(self)
        try:
            driver.find_element_by_id("bindEmailBtn").click()
            driver.find_element_by_id("bindemail").clear()
            driver.find_element_by_id("bindemail").send_keys("i.goal@qq.com")
            time.sleep(1)
            driver.find_element_by_xpath("(//a[@type='button'])[2]").click()
            time.sleep(2)
            print u"此次绑定的邮箱是：i.goal@qq.com"
        except:
            showEmail = driver.find_element_by_id("showemail").text
            print u"邮箱已绑定,绑定的邮箱是：%s"%showEmail
        # finally:
            # user.quit(self)

    def test_self_setup_07(self):
        '''修改邮箱：异常'''
        driver = self.driver
        goTo(self)
        emailList = ['@1.com','126.com','deng@rong','deng@qq.']
        driver.find_element_by_id("modifyEmailBtn").click()
        for email in emailList:
            time.sleep(2)
            driver.find_element_by_id("bindemail").clear()
            time.sleep(2)
            driver.find_element_by_id("bindemail").send_keys("%s"%email)
            time.sleep(1)
            driver.find_element_by_xpath("(//a[@type='button'])[2]").click()
            time.sleep(2)
            popInfo = driver.find_element_by_id("notificationstop-center").text
            print u"%s此次绑定的邮箱是：%s"%(popInfo,email)
        driver.find_element_by_xpath("(//a[contains(text(),'取消')])[2]").click()
        # user.quit(self)

    def test_self_setup_08(self):
        '''修改邮箱:正常'''
        driver = self.driver
        goTo(self)
        email = 'drtest01@126.com'
        driver.find_element_by_id("modifyEmailBtn").click()
        time.sleep(2)
        driver.find_element_by_id("bindemail").clear()
        time.sleep(2)
        driver.find_element_by_id("bindemail").send_keys("%s"%email)
        time.sleep(1)
        driver.find_element_by_xpath("(//a[@type='button'])[2]").click()
        time.sleep(2)
        print u"邮箱已修改！此次绑定的邮箱是：%s"%email
        driver.find_element_by_id("rebindEmailBtn").click()
        popInfo = driver.find_element_by_id("notificationstop-center").text
        print u"提示信息：%s"%popInfo
        # user.quit(self)

    def test_self_setup_09(self):
        '''修改密码:正常'''
        driver = self.driver
        goTo(self)
        driver.find_element_by_xpath("//a[@onclick='selfsetup.gotoChangepw();']").click()
        driver.find_element_by_id("oldPwd").send_keys("abc12345")
        driver.find_element_by_id("newPwd").send_keys("abc123456")
        driver.find_element_by_id("verifyPwd").send_keys("abc123456")
        time.sleep(2)
        driver.find_element_by_xpath("//button[@onclick='changePwd();']").click()
        time.sleep(2)
        driver.switch_to_default_content()
        driver.find_element_by_link_text(u"安全退出").click()
        time.sleep(2)
        user.logins(self,'0282@0101005','abc123456')
        time.sleep(2)
        self.assertEqual(u'今目标企业工作平台',driver.title)
        print u"密码修改成功!"
        driver.switch_to_frame("mgt_workbench_iframe")
        driver.find_element_by_css_selector("a.blue1").click()
        time.sleep(2)
        driver.find_element_by_xpath("//a[@onclick='selfsetup.gotoChangepw();']").click()
        time.sleep(2)
        driver.find_element_by_id("oldPwd").send_keys("abc123456")
        driver.find_element_by_id("newPwd").send_keys("abc12345")
        driver.find_element_by_id("verifyPwd").send_keys("abc12345")
        time.sleep(2)
        driver.find_element_by_xpath("//button[@onclick='changePwd();']").click()
        print u"密码恢复为原密码!"
        # user.quit(self)
        
    def test_self_setup_10(self):
        '''修改头像：个人设置--图片格式'''
        driver = self.driver
        goTo(self)
        imageFile = {"jpg":"D:\\work\\mgt_webtest\\data\\me.jpg",
                     "png":"D:\\work\\mgt_webtest\\data\\me.png",
                     "bmp":"D:\\work\\mgt_webtest\\data\\me.bmp",
                     "jpeg":"D:\\work\\mgt_webtest\\data\\me.jpeg"}
        for format,image in imageFile.items():
            driver.find_element_by_link_text("修改").click()
            time.sleep(2)            
            driver.find_element_by_id("vcardFile").send_keys("%s"%image)
            time.sleep(2)
            driver.find_element_by_id("cropSubmit").click()
            print u"头像修改成功,图片格式为%s"%format
        # user.quit(self)

    def test_self_setup_11(self):
        '''修改头像：图片格式不支持'''
        driver = self.driver
        goTo(self)
        driver.find_element_by_link_text("修改头像").click()
        time.sleep(2)
        driver.find_element_by_id("vcardFile").send_keys("D:\\work\\mgt_webtest\\data\\me.gif")
        popInfo = driver.find_element_by_id("notificationstop-center").text
        print u"%s"%popInfo
        time.sleep(2)
        driver.find_element_by_id("cropSubmit").click()
        time.sleep(2)
        # user.quit(self)
    
        
    def test_self_setup_11(self):
        '''修改头像：尺寸过大'''
        driver = self.driver
        goTo(self)
        driver.find_element_by_link_text("修改头像").click()
        time.sleep(2)
        driver.find_element_by_id("vcardFile").send_keys("D:\\work\\mgt_webtest\\data\\toobig.bmp")
        popInfo = driver.find_element_by_id("notificationstop-center").text
        print u"%s"%popInfo
        time.sleep(2)
        driver.find_element_by_id("cropSubmit").click()
        time.sleep(2)
        # user.quit(self)

    def test_self_setup_12(self):
        '''删除头像'''
        driver = self.driver
        goTo(self)
        driver.find_element_by_link_text("修改头像").click()
        time.sleep(2)
        driver.find_element_by_id("vcardFile").send_keys("D:\\work\\mgt_webtest\\data\\me.jpg")
        time.sleep(2)
        driver.find_element_by_id("delvcard").click()
        time.sleep(2)
        driver.find_element_by_id("cropSubmit").click()
        print u"删除头像，设置为默认头像！"
        time.sleep(2)
        # user.quit(self)

if __name__ == "__main__":
    unittest.main()