from django.core.mail import EmailMultiAlternatives
from rest_framework import response


# 邮件发送 配置
EMAIL_USE_SSL = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.163.com"
EMAIL_PORT = 25
EMAIL_HOST_USER = "tangeml@163.com"
EMAIL_HOST_PASSWORD = '25242041@wy'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


def send_email(request):
    subject = '来自leontom的测试邮件'
    text_content = '这是一封重要的邮件.'
    html_content = '<p>这是一封<strong>重要的</strong>邮件.</p>'
    from_email = EMAIL_HOST_USER
    to_email = '3161859630@qq.com'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email,])
    msg.attach_alternative(html_content, "text/html")
    msg.attach_file('./test.json')
    msg.send()
    return
