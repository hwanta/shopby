from unittest import TestCase
from libs import login
import sys, os  # 폴더 다를 때 사용
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

class Test(TestCase):
    def test_login(self):
        login.login()
