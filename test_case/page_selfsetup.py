#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

class selfSetupPage():
	def setLanguage(self,langug):
		driver = self.driver
		driver.find_element_by_id("langSel").find_element_by_xpath("//option[@value=langug]").click()
        driver.find_element_by_id("modifyLangSubmitBtn").click()