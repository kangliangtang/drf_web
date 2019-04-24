from django.db import models

# Create your models here.
from utils.base_model import BaseModel


class ProjectModel(BaseModel):
    project_name = models.CharField(max_length=32)
    class Meta:
        db_table = "tb_project"


class OperationLogModel(BaseModel):
    """操作日志 测试"""
    action = models.CharField(max_length=128, verbose_name='操作行为')
    data = models.CharField(max_length=512, verbose_name='操作数据')
    action_time = models.DateTimeField(auto_now_add=True, verbose_name='操作时间')
    user = models.CharField(max_length=64, verbose_name='操作人')
    # project = models.ForeignKey('UserInfo', on_delete=models.CASCADE, verbose_name='关联姓名')
    project_id = models.IntegerField(verbose_name='项目id')

    class Meta:
        db_table = 'tb_operation_log'
        verbose_name = '操作日志测试'
        verbose_name_plural = '操作日志测试'