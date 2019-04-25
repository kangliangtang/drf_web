
# name = 'ssssssss'
# try:
#     name = 'kkk'
# except Exception:
#     pass
# finally:
#     print(name)


# from django.utils import timezone
# import pytz
# import datetime
# import time
#
# # start_time_str  = '2019-04-19 10:08:00'
# start_time_str  = datetime.datetime.now()
# start_time_str  = time.time()
# start_time_str  = '2017-04-23T05:27:20.000Z'
# start_time_str  = '2019-04-19T09:10:20.000Z'
# print('=====', start_time_str)
# start_time = timezone.datetime.strptime(start_time_str, '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=pytz.utc)
# print('----', start_time)



# def test(id):
#     print(id)
#     try:
#         n = id +''
#     except Exception:
#         pass
#
#
# s = test(2)
# print(s)


# from functools import wraps
#
# def decorator02(func):
#     @wraps(func)                          # 保持原函数名称不变
#     def wrapper():
#         print('饭前先洗手    before执行....')
#         ret = func()
#         print('饭后百步走    after执行.....')
#         return ret
#     return wrapper
#
# @decorator02
# def eat():             # 原函数
#     print('吃饭咯..    原函数running....')
#     return '好饱'
#
# # 调用原函数
# result = eat()
# print('原函数的返回值为：', result)
# print(eat.__name__)




# s = 'fdjaf'
# c = 'test.json'
# d = s + c
# print(d)
# f = s + '%s'%c
# print(f)


urls = ["http://meiwen.me/src/index.html",
          "http://1000chi.com/game/index.html",
          "http://see.xidian.edu.cn/cpp/html/1429.html",
          "https://docs.python.org/2/howto/regex.html",
          """https://www.google.com.hk/search?client=aff-cs-360chromium&hs=TSj&q=url%E8%A7%A3%E6%9E%90%E5%9F%9F%E5%90%8Dre&oq=url%E8%A7%A3%E6%9E%90%E5%9F%9F%E5%90%8Dre&gs_l=serp.3...74418.86867.0.87673.28.25.2.0.0.0.541.2454.2-6j0j1j1.8.0....0...1c.1j4.53.serp..26.2.547.IuHTj4uoyHg""",
          "file://D:/code/echarts-2.0.3/doc/example/tooltip.html",
          "http://api.mongodb.org/python/current/faq.html#is-pymongo-thread-safe",
          "https://pypi.python.org/pypi/publicsuffix/",
          "http://127.0.0.1:8000"
          ]

# import urllib
# for url in urls:
#     proto, rest = urllib.splittype(url)
#     print(proto)
#     print(rest)

    # res, rest = urllib.splithost(rest)



from urllib.parse import urlparse


# for url in urls:
#     # url = 'file://D:NFSDNA/post/719.html?P=3&A=8'
#     res = (urlparse(url)).path
#     print(res)
#     print(type(res))
#     print('-------------')
# # print(res.path)


# from urllib.parse import urlparse
#
# url = 'http://www.leontom.cc/post/719.html'
# res = urlparse(url)
# print("返回对象:", res)
# print("域名:", res.netloc)
#
# #  ParseResult(scheme='http', netloc='www.leontom.cc', path='/post/719.html', params='', query='', fragment='')
#
# # www.leontom.cc




from django.core.mail import EmailMultiAlternatives
from django.core import mail

subject, from_email, to = 'hello', 'from@example.com', 'to@example.com'
text_content = 'This is an important message.'
html_content = '<p>This is an <strong>important</strong> message.</p>'
msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
msg.attach_alternative(html_content, "text/html")
msg.send()

from django.core.mail import send_mail
# send_mail(subject, message, from_email, recipient_list, **kwrags)

mail.attch()

#------------------------
import os
from email.mime.image import MIMEImage
from django.conf import settings
from django.core import mail


def add_img(src, img_id):
     """
    在富文本邮件模板里添加图片
    :param src:
    :param img_id:
    :return:
    """
     fp = open(src, 'rb')
     msg_image = MIMEImage(fp.read())
     fp.close()
     msg_image.add_header('Content-ID', '<'+img_id+'>')
     return msg_image


def send_util():
    path = os.getcwd()
    path_use = path.replace('\\', '/')
    html = '''
31     <!DOCTYPE html>
32     <html lang="en">
33     <head>
34         <meta charset="UTF-8">
35         <title>Title</title>
36     </head>
37     <body>
38     牛逼呀小伙子，你成功了
39     <img src="cid:test_cid"/>
40     </body>
41     </html>
42     '''
    recipient_list = ['xxxx@xxxx.com']
    from_mail = settings.EMAIL_HOST_USER
    msg = mail.EmailMessage('富文本邮件测试', html, from_mail, recipient_list)
    msg.content_subtype = 'html'
    msg.encoding = 'utf-8'
    image = add_img(path_use+'/mail_util/test.png', 'test_cid')
    msg.attach(image)
    if msg.send():
        return True
    else:
        return False



