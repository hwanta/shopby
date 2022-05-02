import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))) # 폴더 다를 때 사용

from pages import login, option_MM, option_MM_mallEdit
import time


def option_MM_malledit():
    login.login()
    option_MM_mallEdit.mallEdit()


