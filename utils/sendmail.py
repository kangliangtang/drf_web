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
        msg_from='yqst@testroad.org'                                 #���ͷ�����
        passwd='GMc4tJHXiuDqzTTQ'                                   #���뷢�ͷ��������Ȩ��
        msg_to= Tomail.split(',')                                  #�ռ�������

        subject="�����������"                                     #����

        msg = MIMEMultipart(content)
        msg['Subject'] = subject
        msg['From'] = msg_from
        msg['To'] = ",".join(msg_to)
        msg.attach(MIMEText(content, 'plain', 'gbk')) #�ʼ�����
        #��ȡ�ʼ�����
        if enclosure_list is not None:
            for enclosure in enclosure_list:
                att1 =  MIMEApplication(open(enclosure, 'rb').read())
                att1.add_header('Content-Disposition', 'attachment', filename=enclosure) #������������ʼ�����ʾ�����֣���������
                msg.attach(att1)
        try:
            #s = smtplib.SMTP_SSL("smtp.qq.com",465)    #�ʼ����������˿ں�
            s = smtplib.SMTP_SSL("smtp.exmail.qq.com",465)
            s.login(msg_from, passwd)
            s.sendmail(msg_from, msg_to, msg.as_string())
            print("���ͳɹ�")
        except s.SMTPException as e:
            print("����ʧ��")
        finally:
            s.quit()
'''
Conf  =  configure()
tomail = Conf.ToMail()
SendMail = sendMail()
SendMail.sndmail(Tomail=tomail,content="����Ϊ�����������������������",enclosure_list=["dd.txt"])
'''