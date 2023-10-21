from django.test import TestCase

# Create your tests here.
from django.urls import reverse


class MyappTests(TestCase):

    def test_hello_view(self):
        response = self.client.get(reverse('hello'))  # 使用URL名称获取视图的URL
        self.assertEqual(response.status_code, 200)  # 检查响应状态码
        self.assertEqual(response.content.decode('utf-8'), "Hello Word")  # 检查响应内容