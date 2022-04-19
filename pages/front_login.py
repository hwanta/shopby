from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # 로딩될 때까지 대기
from selenium.webdriver.support import expected_conditions as EC  # 로딩될 때까지 대기
from pages import create_driver

# 쇼핑몰 로그인
def login():

    url = 'https://devfe.shopby.co.kr:8283'
    create_driver.driver.get(url)
    try:
        # 로그인 버튼 클릭
        WebDriverWait(create_driver.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'LOGIN')))
        create_driver.driver.find_element(by=By.LINK_TEXT,
                            value='LOGIN').click()

        # 아이디 비밀번호 입력. 로그인 버튼 클릭
        create_driver.driver.find_element(by=By.NAME,
                            value='member-id').send_keys('dlquddnr414')
        create_driver.driver.find_element(by=By.NAME,
                            value='member-password').send_keys('quddnr414@')
        create_driver.driver.find_element(by=By.ID,
                            value='member-login-btn').click()

        # alert 존재하면 내용 출력, 없으면 pass 출력
        WebDriverWait(create_driver.driver, 3).until(EC.alert_is_present())
        alert = create_driver.driver.switch_to.alert
        print("login : Fail")
        print(alert.text)
        alert.accept()
    except:
        print("login : Pass")