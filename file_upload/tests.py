from django.test import TestCase

# Create your tests here.

# from rest_framework.test import APITestCase

# def create_dish(self):
#     # 此处图片路径为绝大路径，static目录和tests.py文件同级
#     image_path = os.path.join(os.path.dirname(
#         os.path.abspath(__file__)), 'static/test/dish_image.jpg')
#     image_fp = open(image_path, 'rb')
#
#     self.dish_data['photo'] = image_fp
#     # 注意post()的format值为"multipart"而不是json
#     response = self.client.post(url, self.dish_data,
#                                 format='multipart')
#     image_fp.close()
#     return response


# def test_create_dish(self):
#     resp = self.create_dish()
#     self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
#     self.assertEqual(self.dish_data['name'], resp.data['name'])
#     self.assertTrue(resp.data['photo'])
#     self.assertTrue('http://testserver/' in resp.data['photo'])


# 'DEFAULT_PARSER_CLASSES': (
#     'rest_framework.parsers.JSONParser',
#     'rest_framework.parsers.FormParser',
#     'rest_framework.parsers.MultiPartParser'
# )

# import os
#
# print(os.getcwd())

