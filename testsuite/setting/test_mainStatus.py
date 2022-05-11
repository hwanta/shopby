from unittest import TestCase
import sys, os # 폴더 다를 때 사용
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from tests.setting import mainStatus


class Test(TestCase):
    def test_main_status_tc(self):
        mainStatus.mainStatusTC()
