from rest_framework import serializers

from apps import models

class ProjectModelSerializer(serializers.ModelSerializer):
    """操作日志 序列化"""
    class Meta:
        model = models.ProjectModel
        exclude = ('id', 'is_delete', 'create_time', 'update_time')
        # fields = '__all__'


class OperationLogModelSerializer(serializers.ModelSerializer):
    """操作日志 序列化"""
    class Meta:
        model = models.OperationLogModel
        # exclude = ('is_delete', 'create_time', 'update_time')
        fields = ('id', 'action', 'data', 'create_time', 'user')