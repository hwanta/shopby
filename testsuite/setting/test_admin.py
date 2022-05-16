from unittest import TestCase
import sys, os  # 폴더 다를 때 사용
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from lib import login
from pages.setting import admin
import time


class Test(TestCase):
    @classmethod
    def setUpClass(cls):
        login.login()
        time.sleep(1)

        admin.accessAdmin()
        time.sleep(1)

    def tearDown(self):
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        login.create_driver.driver.quit()

    def test_001(self):
        admin.searchWord()

    def test_002(self):
        admin.state()

    def test_003(self):
        admin.advancedSearch()

    def test_004(self):
        admin.searchButton()

    def test_005(self):
        admin.clickRegistration()

    def test_006(self):
        admin.operatorName()

    def test_007(self):
        admin.operatorEmail()

    def test_008(self):
        admin.permissionGroup()

    # 운영자 등록 저장은 주석처리
    # def test_009(self):
    #     admin.saveRegistration()

    def test_010(self):
        admin.cancelRegistration()

    def test_011(self):
        admin.editOperator()

    def test_012(self):
        admin.editEmail()

    def test_013(self):
        admin.editPhoneNum()

    def test_014(self):
        admin.editAffiliationDepartment()

    def test_015(self):
        admin.editRank()

    def test_016(self):
        admin.editPosition()

    def test_017(self):
        admin.editPermissionGroup()

    def test_018(self):
        admin.save()

    def test_019(self):
        admin.operatorList()
