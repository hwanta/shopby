from unittest import TestCase
import sys, os  # 폴더 다를 때 사용
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from libs import login
from pages.setting import authorityGroup
import time


class Test(TestCase):
    @classmethod
    def setUpClass(cls):
        login.login()
        time.sleep(1)

        authorityGroup.accessPermissionGroup()
        time.sleep(1)

    def tearDown(self):
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        login.create_driver.driver.quit()

    def test_001(self):
        authorityGroup.authorityName()

    def test_002(self):
        authorityGroup.authoritySearch()

    def test_003(self):
        authorityGroup.searchButton()

    def test_004(self):
        authorityGroup.clickRegistration()

    def test_005(self):
        authorityGroup.selectMall()

    def test_006(self):
        authorityGroup.addName()

    def test_007(self):
        authorityGroup.addDescription()

    def test_008(self):
        authorityGroup.addListInquiry()

    def test_009(self):
        authorityGroup.selectBox1()

    def test_010(self):
        authorityGroup.selectBox2()

    def test_011(self):
        authorityGroup.checkBox()

    def test_012(self):
        authorityGroup.button()

    def test_013(self):
        authorityGroup.buttonReset()

    def test_014(self):
        authorityGroup.buttonMD()

    # 현재 id, name 계속 변해서 제외
    # def test_015(self):
    #     authorityGroup.radioButton()

    def test_016(self):
        authorityGroup.save()

    def test_017(self):
        authorityGroup.authorityList()

    def test_018(self):
        authorityGroup.selectAuthority()

    def test_019(self):
        authorityGroup.editAuthority()




