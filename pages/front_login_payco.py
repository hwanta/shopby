from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # 로딩될 때까지 대기
from selenium.webdriver.support import expected_conditions as EC  # 로딩될 때까지 대기
import time
from libs import create_driver


# 쇼핑몰 로그인
def login():

    url = 'https://devfe.shopby.co.kr:8283'
    create_driver.driver.get(url)

    try:
        # 로그인 버튼 클릭
        WebDriverWait(create_driver.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'LOGIN')))
        create_driver.driver.find_element(by=By.LINK_TEXT,
                                          value='LOGIN').click()

        # 페이코 간편로그인 클릭
        create_driver.driver.find_element(by=By.CSS_SELECTOR,
                                          value='#openIdMethod > a.btn_payco_login.js_btn_payco_login.btn_login_sns').click()

        # 새로운 창으로 변경
        create_driver.driver.switch_to.window(create_driver.driver.window_handles[1])

        # 페이코 아이디, 비밀번호 입력 후 로그인 버튼 클릭
        time.sleep(2)
        create_driver.driver.find_element(by=By.NAME,
                                          value='id').send_keys('dlquddnr414@naver.com')
        create_driver.driver.find_element(by=By.CSS_SELECTOR,
                                          value='#idInputArea > ul > li > a').click()
        create_driver.driver.find_element(by=By.NAME,
                                          value='pw').send_keys('quddnr414@')
        create_driver.driver.find_element(by=By.ID,
                                          value='loginBtn').click()

        # print(driver.current_url)
        time.sleep(2)
        # 현재 창을 원래 창으로 변경
        create_driver.driver.switch_to.window(create_driver.driver.window_handles[0])
        # print(driver.current_url)

        # 로그인이 완료되었습니다. alert 창 닫기('닫기'span을 클릭함, 버튼 클릭이 되지 않음)
        create_driver.driver.find_element(by=By.CSS_SELECTOR,
                                          value='#popups-area > div.layer_wrap.dimed > div > div > div.btn_box > button > span').click()

        # alert 존재하면 내용 출력, 없으면 pass 출력
        WebDriverWait(create_driver.driver, 3).until(EC.alert_is_present())
        alert = create_driver.driver.switch_to.alert
        print("login : Fail")
        print(alert.text)
        alert.accept()
    except:
        print("login : Pass")