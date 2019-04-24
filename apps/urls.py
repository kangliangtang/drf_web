from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from apps import views

# router = routers.SimpleRouter()
# router.register(r'users', UserViewSet)
# router.register(r'accounts', AccountViewSet)
# urlpatterns = router.urls

# 实例化一个router对象
router = routers.DefaultRouter(trailing_slash=False)  # trailing_slash=False 将url的最后"/"去除才可以访问
# 往对象里注册（添加）url
router.register(r'project', views.ProjectViewSet,  base_name='project_name')
# router.register(r'log', views.OperationLogAPIView,  base_name='log')   # 当View继承的不是ModelViewSet, 此处会报错


urlpatterns = [
   url(r'^log', views.OperationLogAPIView.as_view()),
   url(r'^', include(router.urls)),
]
