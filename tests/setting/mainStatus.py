import sys, os # 폴더 다를 때 사용
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from pages import login
from pages.setting import mainStatus
import time


def mainStatusTC():
    login.login()
    time.sleep(2)
    mainStatus.sales()

    time.sleep(5)  # 5초 대기
    login.create_driver.driver.quit()