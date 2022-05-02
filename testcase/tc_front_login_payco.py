import sys, os # 폴더 다를 때 사용
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from pages import front_login_payco
import time


def front_login_payco():
    # 로그인
    front_login_payco.login()
