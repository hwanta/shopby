from unittest import TestCase
import sys, os  # 폴더 다를 때 사용
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from libs import login
from pages.setting import external
import time


class Test(TestCase):
    @classmethod
    def setUpClass(cls):
        login.login()
        time.sleep(1)

        external.accessExternal()
        time.sleep(1)

    def tearDown(self):
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        login.create_driver.driver.quit()

    def test_001(self):
        external.choiceMall()

    def test_002(self):
        external.google()

    def test_003(self):
        external.naver()

    def test_004(self):
        external.kakao()

    def test_005(self):
        external.instagram()

    def test_006(self):
        external.easyLogin()

    def test_007(self):
        external.externalScript()

    def test_008(self):
        external.save()
