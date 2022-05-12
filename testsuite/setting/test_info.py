from unittest import TestCase
import sys, os  # 폴더 다를 때 사용
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from lib import login
from pages.setting import info
import time


class Test(TestCase):

    # 초기 login 및 설정 > 기본정보 진입
    @classmethod
    def setUpClass(cls):
        login.login()
        time.sleep(1)

        info.accessBI()
        time.sleep(1)

    def test_001(self):
        info.companyName()

    def test_002(self):
        info.representativeName()

    def test_003(self):
        info.companyRegistrationNumber()

    def test_004(self):
        info.representativeNumber()

    def test_005(self):
        info.telemarketingNumber()

    def test_006(self):
        info.representativeEmail()

    def test_007(self):
        info.faxNumber()

    def test_008(self):
        info.businessType()

    def test_009(self):
        info.businessConditions()

    def test_010(self):
        info.businessAddress()

    def test_011(self):
        info.managerName()

    def test_012(self):
        info.managerNumber()

    def test_013(self):
        info.managerInfo()

    def test_014(self):
        info.managerEmail()

    def test_015(self):
        info.save()


