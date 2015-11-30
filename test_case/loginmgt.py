#coding=utf-8

import unittest
from selenium import webdriver
from page_login import loginpage

class loginmgt(unittest.TestCase):
    # def setUp(self):
    #     pub.init(self)

    def loginmgt(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        login = loginpage(driver)
        login.open()
        self.assertEqual(True,login.is_loaded)
        login.user_field("028@0101005")
        login.pwd_field('abc12345')
        login.login

if __name__ == '__main__':
    unittest.main()