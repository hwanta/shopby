from unittest import TestCase
import sys, os  # 폴더 다를 때 사용
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from libs import login
from pages.setting import securitySetting
import time


class Test(TestCase):
    @classmethod
    def setUpClass(cls):
        login.login()
        time.sleep(1)

        securitySetting.accessSecuritySetting()
        time.sleep(1)

    def tearDown(self):
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        login.create_driver.driver.quit()

    def test_001(self):
        securitySetting.securityAuthentication()

    def test_002(self):
        securitySetting.securityAuthentication2()

    def test_003(self):
        securitySetting.accessIPSetting()

    def test_004(self):
        securitySetting.changeIPSetting()

    def test_005(self):
        securitySetting.disableIPSetting()
