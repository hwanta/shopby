import sys, os # 폴더 다를 때 사용
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from pages import front_login, create_driver
import time

# 로그인
front_login.login()
time.sleep(5) # 5초 대기
front_login.create_driver.driver.quit()