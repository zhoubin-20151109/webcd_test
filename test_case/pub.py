#!/usr/bin/env python
# -*- coding: utf-8 -*-

'定义各脚本需要重复调用的功能函数，使代码可以重用，减少冗余'
__author__ = 'Rong Deng'

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest, time

def init(self):
    # self.driver = webdriver.Firefox()
    # self.driver = webdriver.Chrome()
    self.driver = webdriver.Ie()
    # self.driver = HtmlUnitDriver()
    # self.driver = webdriver.Safari()
    # self.driver = webdriver.Opera()
    # self.driver = webdriver.Remote("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.HTMLUNITWITHJS)
    self.driver.implicitly_wait(30)
    self.base_url = 'http://project.test1.com'
    self.verificationErrors = []
    self.accept_next_alert = True

def module_icon(self):
    driver = self.driver
    driver.find_element_by_xpath('//*[@id="headAdd"]').click()
    time.sleep(2)
    
def switchtoframe(self):
    driver = self.driver
    time.sleep(3)
    frame = driver.find_element_by_xpath("//iframe[3]")
    driver.switch_to_frame(frame)
    time.sleep(1)

def now():
    now = time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime())
    return now