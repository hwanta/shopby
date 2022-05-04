import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))) # 폴더 다를 때 사용

from pages import login, option_MM, option_MM_mallEdit
import time

login.login()
option_MM_mallEdit.mallEdit()

time.sleep(5) # 5초 대기
login.create_driver.driver.quit()
