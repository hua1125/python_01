#使用Testloader()

"""

"""

from demo14 import login
import unittest
import sys
#
# def
#     print('开始运行方法：',sys._getframe().f_code.co_name)
#


class Testlogin(unittest.TestCase):
    #测试用例
    #正确的用户名，密码
    def test_login_success(self):
        except_value = 1
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
    # 创建一个条件a
    suit_a = unittest.TestLoader().discover('.',pattern='test_login_testdiscover.py')
    print(suite_a)

    runner = unittest.TextTestRunner()
    runner.run(suite_a)