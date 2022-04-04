import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))) # 폴더 다를 때 사용

from pages import login, option_MM, option_MM_mallEdit
import time


login.login()
option_MM.clickMall()
option_MM.clickMallName()
option_MM.clickPC()
time.sleep(1) # PC웹 출력되고 1초 대기

# 현재 탭을 1번 탭으로 변경 후 해당 탭 닫기
login.driver.switch_to.window(login.driver.window_handles[1])
login.driver.close()

# 다시 현재 탭 0번 탭으로 변경
login.driver.switch_to.window(login.driver.window_handles[0])

option_MM.clickMobile()

time.sleep(5) # 5초 대기
login.driver.quit()