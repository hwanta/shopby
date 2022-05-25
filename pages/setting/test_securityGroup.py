from unittest import TestCase
import sys, os  # 폴더 다를 때 사용
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from libs import login
from pages.setting import securityGroup
import time


class Test(TestCase):
    @classmethod
    def setUpClass(cls):
        login.login()
        time.sleep(1)

        securityGroup.accessSecurityGroup()
        time.sleep(1)

    def tearDown(self):
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        login.create_driver.driver.quit()

    def test_001(self):
        securityGroup.securityAuthentication()

    def test_002(self):
        securityGroup.securityAuthentication2()
