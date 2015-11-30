#coding=utf-8

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest, time, pub


user_id = 'email'
pwd_id = 'password'
loginbtn_xpath = '//form[@id="commonForm"]/div/div/div[8]/a'

def logins(self,username,passwd):   
    driver = self.driver
    driver.get(self.base_url)
    driver.maximize_window()
    driver.find_element_by_id(user_id).clear()
    driver.find_element_by_id(user_id).send_keys(username)
    driver.find_element_by_id(pwd_id).clear()
    driver.find_element_by_id(pwd_id).send_keys(passwd)
    driver.find_element_by_xpath(loginbtn_xpath).click()

#部门经理登录(函数)
def login(self):   
    driver = self.driver
    driver.get(self.base_url)
    # driver.maximize_window()
    driver.find_element_by_id(user_id).clear()
    driver.find_element_by_id(user_id).send_keys("0000@0101005")
    driver.find_element_by_id(pwd_id).clear()
    driver.find_element_by_id(pwd_id).send_keys("12qwaszx")
    time.sleep(1)
    driver.find_element_by_xpath(loginbtn_xpath).click()
    time.sleep(2)

#普通员工登录
def login_yg(self):   
    driver = self.driver
    driver.get(self.base_url)
    driver.maximize_window()
    driver.find_element_by_id(user_id).clear()
    driver.find_element_by_id(user_id).send_keys("0282@0101005")
    driver.find_element_by_id(pwd_id).clear()
    driver.find_element_by_id(pwd_id).send_keys("abc12345")
    time.sleep(2)
    driver.find_element_by_xpath(loginbtn_xpath).click()
    time.sleep(2)

#手机终端页面用户登录
def login_m(self):   
    driver = self.driver
    driver.maximize_window()
    driver.find_element_by_id(user_id).clear()
    driver.find_element_by_id(user_id).send_keys("028@0101005")
    driver.find_element_by_id(pwd_id).clear()
    driver.find_element_by_id(pwd_id).send_keys("abc12345")
    time.sleep(2)
    driver.find_element_by_id(loginbtn_id).click()
    time.sleep(2)

#web端退出模块(函数)
def quit(self):
    driver = self.driver
    time.sleep(3)
    driver.switch_to_default_content()
    driver.find_element_by_link_text("安全退出").click()
    time.sleep(2)

#移动端退出模块(函数)
def quit_m(self):
    driver = self.driver
    driver.get(self.base_url)
    time.sleep(3)
    driver.find_element_by_link_text("安全退出").click()