import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))) # 폴더 다를 때 사용

from pages import login, order_IOL
import time


order_IOL.findOrder()

time.sleep(5) # 5초 대기
login.driver.quit()