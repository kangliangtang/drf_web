import pytz
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










