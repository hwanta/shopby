import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))) # 폴더 다를 때 사용

from pages import option_MM_mallEdit
from lib import login
import time

login.login()
option_MM_mallEdit.mallEdit()

time.sleep(5) # 5초 대기
lib.create_driver.driver.quit()
