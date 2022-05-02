import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))) # 폴더 다를 때 사용

from pages import login, option_BI
import time


def option_BI():
    login.login()
    time.sleep(2)
    option_BI.inputBI()
