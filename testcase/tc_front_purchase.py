import sys, os # 폴더 다를 때 사용
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from pages import front_login, front_purchase
import time


def front_purchase():
    # 로그인
    front_login.login()

    front_purchase.productPurchase()
