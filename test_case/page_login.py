#coding=utf-8

class loginpage(object):
    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://web2.jingoal.cn'
        self.title = u'今目标企业工作平台'

    def is_loaded(self):
        return self.driver.title == self.title

    def user_field(username):
        user_field = self.driver.find_element_by_id(id='loginNameNomal')
        user_field.send_keys(username)

    def pwd_field(pwd):
        pwd_field = self.driver.find_element_by_id('pwd')
        pwd_field.send_keys(pwd)

    def login():
        login = self.driver.find_element_by_xpath("//input[@type='submit']")
        login.click()

    def open(self):
        self.driver.get(self.url)

    def close(self):
        self.driver.close()

##########################################################

class bmicalcpage(object):
    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://dl.dropbox.com/u/55228056/bmicalculator.html'
        self.title = 'BMI Calculator'
    
    @property
    def is_loaded(self):
        return self.driver.title == self.title
    
    @property
    def bmi(self):
        bmi_field = self._driver.find_element_by_id('bmi')
        return bmi_field.get_attribute('value')
    
    @property
    def bmi_category(self):
        bmi_category_field = self._driver.find_element_by_id('bmi_category')
        return bmi_category_field.get_attribute('value')
    
    def open(self):
        self.driver.get(self.url)
    
    def calculate(self, height, weight):
        height_field = self.driver.find_element_by_id('heightCMS')
        weight_field = self.driver.find_element_by_id('weightKg')
        calc_button = self.driver.find_element_by_id('Calculate')
        
        height_field.send_keys(height)
        weight_field.send_keys(weight)
        calc_button.click()
    
    def close(self):
        self.driver.close()