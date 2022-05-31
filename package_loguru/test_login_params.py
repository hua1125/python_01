



from parameterized import  parameterized
import unittest
from demo14 import login
lst_data = [(0,'root','123456'),(0,'hua','456789')]


class TestLogin(unittest.TestCase):


    @parameterized.expand(lst_data)
    def test_login(self,except_value,username,password):

        actual_value = login(username,password).get('code')
        self.assertEqual(except_value,actual_value)

if __name__ == '__main__':
    unittest.main()