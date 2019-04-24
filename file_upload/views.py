import os

from django.shortcuts import render

from rest_framework import viewsets
# Create your views here.
from rest_framework.response import Response
from timedrf import settings
from .serializers import UploadFileSerializer
from .models import FileModel
from rest_framework.decorators import list_route, detail_route
from rest_framework.status import HTTP_400_BAD_REQUEST
from django.http.response import FileResponse


class FileUplodAPIView(viewsets.ModelViewSet):
    serializer_class = UploadFileSerializer
    queryset = FileModel.objects.all()
    upload_file_path = settings.UPLOAD_FILE_PATH

    def create(self, request, *args, **kwargs):
        """上传文件"""
        file_obj = request.FILES.get('file', None)
        filename = file_obj.name
        try:
            with open(self.upload_file_path + filename, 'wb') as f:
                for chunk in file_obj.chunks():
                    f.write(chunk)
        except Exception as e:
            return Response({'message': '%s' % e}, HTTP_400_BAD_REQUEST)
        else:
            FileModel.objects.create(
                file_name=filename,
                file=file_obj,
                file_path=self.upload_file_path + filename
            )
        return Response({'message': 'OK'}, 200)


class DownFileView(viewsets.ViewSet):
    """文件下载"""
    @detail_route(methods=['GET'])
    def get(self, request, pk):
        obj = FileModel.objects.get(id=pk)
        file_path_ = obj.file_path
        file_name = file_path_.split('/')[-1]
        with open(settings.UPLOAD_FILE_PATH + file_name, 'r', encoding='utf-8') as f:
            file_ = f.read()
            response = FileResponse(file_)
            response["content_type"] = 'application/json'
            response['Content-Disposition'] = "attachment; filename= {}".format(file_name)
            return response