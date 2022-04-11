from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager  # import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # 로딩될 때까지 대기
from selenium.webdriver.support import expected_conditions as EC  # 로딩될 때까지 대기
from selenium.webdriver.common.keys import Keys
import time

# driver 옵션 추가(시스템에 부착된 장치가 작동하지 않습니다. 삭제 옵션)
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

options.add_argument("--start-maximized")  # 전체화면 옵션

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
url = 'https://devfe.shopby.co.kr:8283/'
driver.get(url)


# 쇼핑몰 로그인
def login():
    try:
        # 로그인 버튼 클릭
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'LOGIN')))
        driver.find_element(by=By.LINK_TEXT,
                            value='LOGIN').click()

        # 페이코 간편로그인 클릭
        driver.find_element(by=By.CSS_SELECTOR,
                            value='#openIdMethod > a.btn_payco_login.js_btn_payco_login.btn_login_sns').click()

        # 새로운 창으로 변경
        driver.switch_to.window(driver.window_handles[1])

        # 페이코 아이디, 비밀번호 입력 후 로그인 버튼 클릭
        time.sleep(2)
        driver.find_element(by=By.NAME,
                            value='id').send_keys('dlquddnr414@naver.com')
        driver.find_element(by=By.CSS_SELECTOR,
                            value='#idInputArea > ul > li > a').click()
        driver.find_element(by=By.NAME,
                            value='pw').send_keys('quddnr414@')
        driver.find_element(by=By.ID,
                            value='loginBtn').click()

        # print(driver.current_url)
        time.sleep(2)
        # 현재 창을 원래 창으로 변경
        driver.switch_to.window(driver.window_handles[0])
        # print(driver.current_url)

        # 로그인이 완료되었습니다. alert 창 닫기('닫기'span을 클릭함, 버튼 클릭이 되지 않음)
        driver.find_element(by=By.CSS_SELECTOR,
                            value='#popups-area > div.layer_wrap.dimed > div > div > div.btn_box > button > span').click()

        # alert 존재하면 내용 출력, 없으면 pass 출력
        WebDriverWait(driver, 3).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        print("login : Fail")
        print(alert.text)
        alert.accept()
    except:
        print("login : Pass")