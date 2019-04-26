# __author__ = Created by Chenkl on 2018/4/18
# coding=gbk

import smtplib
from email.mime.text import MIMEText
import time
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
# from base.configure import configure

class sendMail():
    # Conf = configure();
    # filePath = Conf.resultFilePath()
    def sndmail(self,Tomail,content,enclosure_list):
        data = time.strftime('%Y%m%d',time.localtime(time.time()))
        msg_from='yqst@testroad.org'                                 #发送方邮箱
        passwd='GMc4tJHXiuDqzTTQ'                                   #填入发送方邮箱的授权码
        msg_to= Tomail.split(',')                                  #收件人邮箱

        subject="舆情搜索结果"                                     #主题

        msg = MIMEMultipart(content)
        msg['Subject'] = subject
        msg['From'] = msg_from
        msg['To'] = ",".join(msg_to)
        msg.attach(MIMEText(content, 'plain', 'gbk')) #邮件正文
        #读取邮件附件
        if enclosure_list is not None:
            for enclosure in enclosure_list:
                att1 =  MIMEApplication(open(enclosure, 'rb').read())
                att1.add_header('Content-Disposition', 'attachment', filename=enclosure) #这里的名字是邮件中显示的名字，可以任意
                msg.attach(att1)
        try:
            #s = smtplib.SMTP_SSL("smtp.qq.com",465)    #邮件服务器及端口号
            s = smtplib.SMTP_SSL("smtp.exmail.qq.com",465)
            s.login(msg_from, passwd)
            s.sendmail(msg_from, msg_to, msg.as_string())
            print("发送成功")
        except s.SMTPException as e:
            print("发送失败")
        finally:
            s.quit()
'''
Conf  =  configure()
tomail = Conf.ToMail()
SendMail = sendMail()
SendMail.sndmail(Tomail=tomail,content="附件为今天的舆情搜索结果，请查收",enclosure_list=["dd.txt"])
'''