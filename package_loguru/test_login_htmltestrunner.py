

#使用htmltestrunner模块生成测试报告

"""
类：HTMLTestRunner(f,titile,description)

"""
from demo14 import login
import unittest
from package_loguru.HTMLTestRunner import HTMLTestRunner

class Testlogin(unittest.TestCase):
    #测试用例
    #正确的用户名，密码
    def test_login_success(self):
        except_value = 0
        actual_value = login('root','123456').get('code')
        self.assertEqual(except_value,actual_value)
    #错误的用户名
    def test_login_wrong(self):
        except_value = 1
        actual_value = login('roo','123456').get('code')
        self.assertEqual(except_value,actual_value)
    #空的用户名
    def test_login_none(self):
        except_value = 1
        actual_value = login('','123456').get('code')
        self.assertEqual(except_value,actual_value)

if __name__ == '__main__':
    suite_a = unittest.TestSuite()
    suite_a.addTest(Testlogin('test_login_success'))
    suite_a.addTest(Testlogin('test_login_wrong'))
    suite_a.addTest(Testlogin('test_login_none'))
    print(suite_a)
    #创建一个测试报告文件,格式为.html
    test_report = './test_report.html'

    with open(test_report,'wb') as f:
        runner = HTMLTestRunner(f,title='测试报告',description='测试报告')
        runner.run(suite_a)#runner 里面的run方法

