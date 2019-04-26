import pytz
from django.http import HttpResponse, HttpResponseRedirect

from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from apps.serializers import ProjectModelSerializer, OperationLogModelSerializer
from apps import models

from rest_framework.response import Response
# from django_filters import filters
from rest_framework import filters

# 操作日志
from utils.operation_log import OperationLogDecorator
from django.utils.decorators import method_decorator
logde = OperationLogDecorator()

from rest_framework.pagination import PageNumberPagination
from django.conf import settings
from django.core.mail import send_mass_mail
from django.core.mail import EmailMultiAlternatives, EmailMessage, BadHeaderError
from utils.email_tasks import celery_send_email_task


class LogPagination(PageNumberPagination):
    """分页设置"""
    page_size = 11                           # 每页条数
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100                     # 最大分页



class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectModelSerializer
    queryset = models.ProjectModel.objects.all()

    # @method_decorator(logde.project_update)
    # def update(self, request, *args, **kwargs):
    #     return super().update(request, *args, **kwargs)

    @method_decorator(logde.project_update)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


class OperationLogAPIView(ListAPIView):
    serializer_class = OperationLogModelSerializer
    pagination_class = LogPagination
    queryset = models.OperationLogModel.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    ordering = ('-create_time',)

    def get_queryset(self):
        """根据项目名称（project_id） 获取操作日志记录"""
        project_id = self.request.query_params.get('project_id', None)
        query_set = super().get_queryset().filter(project_id=project_id)
        if self.request.query_params.get('time_start'):
            start_time_str = self.request.query_params.get('time_start')
            print('time_start:', start_time_str)
            end_time_str = self.request.query_params.get('time_end')
            start_time = timezone.datetime.strptime(start_time_str, '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=pytz.utc)
            print('start_time:', start_time)
            end_time = timezone.datetime.strptime(end_time_str, '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=pytz.utc)
            # end_time += timezone.timedelta(days=1)
            print('time_end:', end_time)
            query_set = query_set.filter(create_time__range=(start_time, end_time))
        return query_set


def send_email_view(request):
    subject = '来自leontom的测试邮件'
    time_task_name = 'time定时'
    task_result_code = 'run success!'
    task_time = '60s'
    text_content = '定时任务<{}>已执行完成，结果为<{}>,执行时间为<{}>。详细测试结果见附件'.format(time_task_name,task_result_code, task_time)
    html_content = '<p>定时任务<strong>&lt;{}&gt;</strong>已执行完成，结果为<strong>&lt;{}&gt;</strong>,执行时间为<strong><{}></strong>。详细测试结果见附件</p>'
    html_content = html_content.format(time_task_name, task_result_code, task_time)
    from_email = settings.EMAIL_HOST_USER
    to_emails = ['3161859630@qq.com', ]
    if subject and text_content and from_email:
        try:
            msg = EmailMultiAlternatives(subject, text_content, from_email, to_emails)
            msg.attach_alternative(html_content, "text/html")                              # 邮箱内容html格式
            file_path = settings.UPLOAD_FILE_PATH + 'test.json'
            file_path = None
            # msg.attach(filename='test', content='file data')
            if file_path:
                msg.attach_file(file_path)                                                     # 添加附件
            msg.send()
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('Send email success!')
    else:
        return HttpResponse('参数不完整')


# def celery_sendemail():
#     celery_send_email_task()
