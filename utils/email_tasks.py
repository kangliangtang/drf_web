from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail, EmailMultiAlternatives
import logging

logger = logging.getLogger(__name__)


@shared_task
def celery_send_email_task(subject, connection, from_email, to_emails, **kwargs):
    try:
        # 使用celery并发处理邮件发送的任务
        # send_mail(subject, message, from_email, recipient_list, **kwargs)
        msg = EmailMultiAlternatives(subject, connection, from_email, to_emails)
        if kwargs['html_content']:
            msg.attach_alternative(kwargs['html_content'], "text/html")  # 邮箱内容html格式
        if kwargs['file']:
            msg.attach_file(kwargs['file'])                              # 添加附件
        msg.send()
    except Exception as e:
        logger.error("邮件发送失败: {}".format(e))
