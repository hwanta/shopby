from unittest import TestCase
import sys, os  # 폴더 다를 때 사용
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from lib import login
from pages.setting import malls
import time


class Test(TestCase):

    # 초기 login 및 설정 > 쇼핑몰관리 진입
    @classmethod
    def setUpClass(cls):
        login.login()
        time.sleep(1)

        malls.accessMalls()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        login.create_driver.driver.quit()

    def test_001(self):
        malls.addMall()
        time.sleep(1)

    def test_002(self):
        malls.accessEditMall()
        time.sleep(1)

    def test_003(self):
        malls.mallName()
        time.sleep(1)

    def test_004(self):
        malls.mallNumber()
        time.sleep(1)

    def test_005(self):
        malls.mallEmail()
        time.sleep(1)

    def test_006(self):
        malls.intro_PC()
        time.sleep(1)

    def test_007(self):
        malls.intro_MO()
        time.sleep(1)

    def test_008(self):
        malls.domain()
        time.sleep(1)

    def test_009(self):
        malls.domain_PC()
        time.sleep(1)

    def test_010(self):
        malls.domain_MO()
        time.sleep(1)

    def test_011(self):
        malls.account()
        time.sleep(1)

    def test_012(self):
        malls.creditCard()
        time.sleep(1)

    def test_013(self):
        malls.realtimeAccount()
        time.sleep(1)

    def test_014(self):
        malls.virtualAccount()
        time.sleep(1)

    def test_015(self):
        malls.escrowRealtimeAccount()
        time.sleep(1)

    def test_016(self):
        malls.escrowVirtualAccount()
        time.sleep(1)

    def test_017(self):
        malls.payco()
        time.sleep(1)

    def test_018(self):
        malls.accountInfoEdit()
        time.sleep(1)

    def test_019(self):
        malls.memberAuth()
        time.sleep(1)

    def test_020(self):
        malls.authTime()
        time.sleep(1)

    def test_021(self):
        malls.authType()
        time.sleep(1)

    def test_022(self):
        malls.customerClaim()
        time.sleep(1)

    def test_023(self):
        malls.storagePeriod()
        time.sleep(1)

    def test_024(self):
        malls.storagePeriodSelect()
        time.sleep(1)

    def test_025(self):
        malls.storageQuantity()
        time.sleep(1)

    def test_026(self):
        malls.save()
        time.sleep(1)

    def test_027(self):
        malls.mallManage()
        time.sleep(1)

