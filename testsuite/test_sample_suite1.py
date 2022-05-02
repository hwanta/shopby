from unittest import TestCase
import sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))  # 폴더 다를 때 사용

from pages import login
from testcase import tc_member, tc_option
import time


class TestSample1(TestCase):
    def test_member(self):
        tc_member.tc_member()
        time.sleep(5)  # 5초 대기

    def test_option(self):
        tc_option.tc_option()
        time.sleep(5)  # 5초 대기
        login.create_driver.driver.quit()
