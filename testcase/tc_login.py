import sys, os  # 폴더 다를 때 사용

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from pages import login
import time


def login():
    # 로그인
    login.login()

