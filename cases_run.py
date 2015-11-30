#!/usr/bin/env python
# -*- coding: utf-8 -*-

'执行这个脚本可以根据需要执行自动化测试用例，生成测试报告，并发送到mail_to指定的邮箱地址'
__author__ = 'Rong Deng'

import unittest,HTMLTestRunner
import os,time,datetime,sys,smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
sys.path.append('\\test_case')
reload(sys)
sys.setdefaultencoding( 'utf-8' )

path = "D:\\workspace\\mgt_test"
#定义发送邮件
def sendmail(file_new):
    #发信邮箱
    mail_from='drtest01@126.com'
    #收信邮箱
    mail_to='imfuture@139.com'
    #定义正文
    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body,_subtype='html',_charset='utf-8')
    #定义标题
    msg['Subject']=u"今目标测试报告"
    #定义发送时间（不定义的可能有的邮件客户端会不显示发送时间）
    msg['date']=time.strftime('%Y %m %d %H:%M:%S',time.localtime())
    smtp=smtplib.SMTP()
    #连接SMTP 服务器，此处用的126的SMTP 服务器
    smtp.connect('smtp.126.com')
    #用户名密码
    smtp.login('drtest01@126.com','jingoal')
    smtp.sendmail(mail_from,mail_to,msg.as_string())
    smtp.quit()
    print u'测试报告已经发送到指定的邮箱!'

#查找测试报告，调用发邮件功能
def sendreport():
    result_dir = path + '\\report'
    lists=os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn) if not
                              os.path.isdir(result_dir+"\\"+fn) else 0)
    print (u"最新测试生成的报告： "+lists[-1])
    #找到最新生成的文件
    file_new = os.path.join(result_dir,lists[-1])
    print file_new
    #调用发邮件模块
    sendmail(file_new)

def creatsuite():
    list_case = path + "\\test_case"
    testunit=unittest.TestSuite()

    #discover 方法定义
    discover=unittest.defaultTestLoader.discover(list_case,
                     pattern ='at_task*',
                     top_level_dir=None)
                    
    #discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTest(test_case)
            print testunit
    return testunit

alltestnames = creatsuite()

now = time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime())
filename = path + '\\report\\'+now+'_result.html'
fp = file(filename, 'wb')

runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title=u'今目标企业平台测试结果',
            description=u'用例执行详细信息：')


# if __name__ == "__main__":
# 执行测试用例
for i in xrange(1):
    runner.run(alltestnames)