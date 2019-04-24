from django.db import models


class BaseModel(models.Model):
    CHOICES_DELETE = (
        (0, '未删除'),
        (1, '已删除')
    )
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_delete = models.SmallIntegerField(default=0, choices=CHOICES_DELETE, verbose_name='逻辑删除')

    class Meta:
        abstract = True