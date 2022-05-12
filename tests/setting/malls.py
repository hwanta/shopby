import sys, os # 폴더 다를 때 사용
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from lib import login
from pages.setting import malls
import time


def addMallTC():
    login.login()
    time.sleep(2)
    malls.addMall()

def editMallTC():
    time.sleep(2)
    malls.editMall()

def manageMallTC():
    time.sleep(2)
    malls.mallManage()

    time.sleep(5)  # 5초 대기
    lib.create_driver.driver.quit()