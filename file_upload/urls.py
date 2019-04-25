from django.conf.urls import url, include
from rest_framework import routers

from rest_framework import routers
from . import views


# 实例化一个对象
router = routers.DefaultRouter(trailing_slash=False)
# 往对象添加url
router.register(r'', views.FileUplodAPIView, base_name='upload_file')
router.register(r'down', views.DownFileView, base_name='down_file')


urlpatterns = [
   url(r'', include(router.urls)),
]