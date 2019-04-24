import datetime
import json
from django.http import QueryDict
from rest_framework.request import Request
from apps.models import OperationLogModel, ProjectModel

# def my_decorator(func):
#     """自定义装饰器"""
#     def wrapper(request, *args, **kwargs):
#         print('-------自定义装饰器被调用了--------')
#         # print('请求路径:', request.path)
#         # print('请求方法：', request.method)
#         project_id = request.META.get('HTTP_PROJECTID')
#
#         project_name = TestProjectModel.objects.filter(id=project_id).first()
#         user = request.user
#         data = get_parameter_dic(request)
#         action_time = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
#         # 操作行为
#         # 将不同的操作写成自定义的文字描述，添加到表中action字段下
#         action = '用户<{}> 新增 <{}>项目'.format(user, project_name)
#         # print("项目id", project_id)
#         # print('{}：', user)
#         # print('请求数据(dict)：', data)
#         # print('操作时间：', action_time)
#         # print('操作行为：', action)
#
#         # 获取接口名称 filter(uid__gt = 1).values('uid')
#         # interface_name = InterfaceModel.objects.filter(is_delete=False, module__project_id=project_id, module__project__project_statu=True).values('name')
#         # print("interface_name", interface_name)
#         api_response = func(request, *args, **kwargs)
#         # 当返回 200 认为接口操作成功，记录下操作日志
#         if Response.status_code == 200:
#             operation_log_create(action=action, data=data, action_time=action_time, user=user, project=project_id)
#         return api_response
#     return wrapper



class OperationLogDecorator(object):
    """操作日志装饰器"""
    def __init__(self):
        pass

    @staticmethod
    def get_parameter_dic(request):
        """将请求参数转化为dict形式"""
        if isinstance(request, Request) == False:
            return {}
        query_params = request.query_params
        if isinstance(query_params, QueryDict):
            query_params = query_params.dict()
        result_data = request.data
        if isinstance(result_data, QueryDict):
            result_data = result_data.dict()

        if query_params != {}:
            # return json.dumps(query_params)
            return query_params
        else:
            # return json.dumps(result_data)
            return result_data

    @staticmethod
    def _get_project_name(project_id):
        """获取项目名称"""
        project_obj = ProjectModel.objects.filter(id=project_id).values("project_name")
        project_name = ''.join(i.get("project_name", None) for i in list(project_obj))
        return project_name

    @staticmethod
    def __operation_log_create(action=None, data=None, action_time=None, user=None, project_id=None):
        """操作日志表 添加数据"""
        # olm = OperationLogModel(
        OperationLogModel.objects.create(
            action=action,
            data=data,
            action_time=action_time,
            user=user,
            project_id=project_id
        )
        # olm.save()

    def project_update(self, func):
        """修改 项目信息"""
        def wrapper(request, *args, **kwargs):
            print('======装饰器被调用=======')
            project_id = request.META.get('HTTP_PROJECTID')
            project_id = int(project_id)
            project_name = self._get_project_name(project_id)
            user = 'user_testname'
            data = self.get_parameter_dic(request)
            action_time = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
            print("----调用接口 view-------------")
            api_response = func(request, *args, **kwargs)
            # 当返回 200 认为接口操作成功，记录下操作日志

            print('======项目名称=========', project_name)
            if api_response.status_code == 200:

                # project_obj = UserInfo.objects.filter(id=int(project_id)).values("username")
                print('---------huilau---------------', project_name)
                # project_obj = UserInfo.objects.all().filter(id=int(project_id)).values("username")
                action = '<{}>修改了<{}>项目信息'.format(user, project_name)
                # 添加到数据库
                print('---------添加到数据库----------')
                self.__operation_log_create(action=action, data=data, action_time=action_time, user=user, project_id=project_id)
            return api_response
        return wrapper


