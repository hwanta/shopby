from unittest import TestCase
import sys, os  # 폴더 다를 때 사용
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from libs import login
from pages.product import addSingle
import time

class Test(TestCase):

    @classmethod
    def setUpClass(cls):
        login.login()
        time.sleep(1)

        addSingle.accessProductList() # 각 테스트 해야할 항목의 함수를 입력(페이지별 수정 필요)
        time.sleep(1)

    def tearDown(self):
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        login.create_driver.driver.quit() # 여기까지는 로그인 함수로 모든 테스트 시작에 필요한 공통 함수

    def test_001(self): # 1번부터 각 함수를 매칭하여 테스트 실행 (그냥 함수로 나열하면 abc 순서대로 테스트가 실행되어 tc 순서와 다르게 테스트가 실행 됨)
        addSingle.momo()