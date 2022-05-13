from unittest import TestCase
import sys, os  # 폴더 다를 때 사용
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from lib import login
from pages.setting import terms
import time


class Test(TestCase):
    @classmethod
    def setUpClass(cls):
        login.login()
        time.sleep(1)

        terms.accessTerm()
        time.sleep(1)

    def tearDown(self):
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        login.create_driver.driver.quit()

    def test_001(self):
        terms.choiceMall()

    def test_002(self):
        terms.clickList()

    def test_003(self):
        terms.companyIntroduction()

    def test_004(self):
        terms.introductionUsed()

    def test_005(self):
        terms.introductionContent()

    def test_006(self):
        terms.introductionSave()

    def test_007(self):
        terms.accessTerm()
        terms.choiceMall()
        terms.termsService()

    def test_008(self):
        terms.termsDate()

    def test_009(self):
        terms.termsContent()

    def test_010(self):
        terms.termsUsed()

    def test_011(self):
        terms.termsSave()

    def test_012(self):
        terms.accessTerm()
        terms.choiceMall()
        terms.privacy()

    def test_013(self):
        terms.privacyDate()

    def test_014(self):
        terms.privacyContent()

    def test_015(self):
        terms.privacySave()

    def test_016(self):
        terms.accessTerm()
        terms.choiceMall()
        terms.personalInfo()

    def test_017(self):
        terms.personalInfoContent1()

    def test_018(self):
        terms.personalInfoContent2()

    def test_019(self):
        terms.personalInfoUsed2()

    def test_020(self):
        terms.personalInfoContent3()

    def test_021(self):
        terms.personalInfoUsed3()

    def test_022(self):
        terms.personalInfoContent4()

    def test_023(self):
        terms.personalInfoUsed4()

    def test_024(self):
        terms.personalInfoContent5()

    def test_025(self):
        terms.personalInfoContent6()

    def test_026(self):
        terms.personalInfoContent7()

    def test_027(self):
        terms.personalInfoUsed7()

    def test_028(self):
        terms.personalInfoContent8()

    def test_029(self):
        terms.personalInfoUsed8()

    def test_030(self):
        terms.personalInfoContent9()

    def test_031(self):
        terms.personalInfoSave()

    def test_032(self):
        terms.accessTerm()
        terms.choiceMall()
        terms.useInfo()

    def test_033(self):
        terms.useInfoContent1()

    def test_034(self):
        terms.useInfoUsed1()

    def test_035(self):
        terms.useInfoContent2()

    def test_036(self):
        terms.useInfoUsed2()

    def test_037(self):
        terms.useInfoSave()




