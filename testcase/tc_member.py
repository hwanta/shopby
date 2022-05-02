import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))) # 폴더 다를 때 사용

from pages import login, member
import time


def tc_member():
    login.login()
    member.MemberList()
    member.MemberListSearch()

