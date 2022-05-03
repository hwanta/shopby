from unittest import TestCase
import sys, os # 폴더 다를 때 사용
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from pages import front_login, create_driver
import time

class Test(TestCase):
    def test_front_login(self):
        front_login.login()
