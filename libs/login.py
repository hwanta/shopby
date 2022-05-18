from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait   # 로딩될 때까지 대기
from selenium.webdriver.support import expected_conditions as EC # 로딩될 때까지 대기
from libs import create_driver


# 쇼핑몰 로그인
def login():
    url = 'https://alpha-admin.shopby.co.kr'
    create_driver.driver.get(url)

    # 로그인 되어있는지 먼저 확인
    try:
        create_driver.driver.find_element(by=By.XPATH,
                                          value='//*[@id="container"]/div[2]/div/form/div/table/tr[1]/td/input')
    except:
        return

    # xpath 해당 부분이 존재하는지 확인
    WebDriverWait(create_driver.driver, 10).until(EC.presence_of_element_located ((By.XPATH,'//*[@id="container"]/'
                                                                                            'div[2]/div/form/div/'
                                                                                            'table/tr[1]/td/input')))
    # 통합회원 로그인 클릭
    create_driver.driver.find_element(by=By.CSS_SELECTOR,
                                      value='#container > div.content_login > div > form > button.btn_login.auth').click()

    # 새 탭으로 이동
    create_driver.driver.close()
    create_driver.driver.switch_to.window(create_driver.driver.window_handles[0])

    # 아이디/비밀번호 입력
    create_driver.driver.find_element(by=By.ID,
                                      value='username').send_keys('proqa01')
    create_driver.driver.find_element(by=By.ID,
                                      value='password').send_keys('1q2w3e4r!!')

    # 로그인 버튼 클릭
    create_driver.driver.find_element(by=By.LINK_TEXT,
                                      value='로그인').click()

    # alert 존재하면 내용 출력, 없으면 pass 출력
    try:
        WebDriverWait(create_driver.driver, 3).until(EC.alert_is_present())
        alert = create_driver.driver.switch_to.alert
        print(alert.text)
        alert.accept()
    except:
        print("login : Pass")

    # 비밀번호 변경 팝업 출력 시 [다음에 변경하기] 버튼 클릭
    try:
        popup = create_driver.driver.find_element(by=By.CLASS_NAME, value='layer_popup').is_displayed()
        create_driver.driver.find_element(by=By.CSS_SELECTOR,
                                          value='#container > div.content_login > div.layer_popup_wrap.ncp_layerpopup > div > '
                                                'div.lp_content > div > div.lp_footer > button.lp_close_btn.medium.lp_close').click()
    except:
        print("비밀번호 변경 팝업 미출력됨")
