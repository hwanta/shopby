from unittest import TestCase
import sys, os # 폴더 다를 때 사용
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from tests.setting import malls

class Test(TestCase):
    def test_add_mall_tc(self):
        malls.addMallTC()

    def test_edit_mall_tc(self):
        malls.editMallTC()

    def test_manage_mall_tc(self):
        malls.manageMallTC()
