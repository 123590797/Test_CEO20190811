import requests
import unittest
# 使用类的方式来管理http请求的发送，它是爷爷类
class BaseHttp(object):
    host = 'http://localhost'

    # 统一http发送方式
    def sendHttp(self, path, method='post', **kwargs):
        url = '{}{}'.format(self.host, path)
        result = requests.request(method=method, url=url, **kwargs)
        return result


#统一封装校验类
class VerifyClass(unittest.TestCase):

    def verify_json_data(self,target,key,result_data):
        code = target.status_code
        target = target.json()
        self.assertEqual(200,code)
        self.assertEqual(target.get(key),result_data)

    def verify_html_data(self,target,result_data):
        code = target.status_code
        target = target.text()
        self.assertEqual(200, code)
        self.assertEqual(result_data,target)
