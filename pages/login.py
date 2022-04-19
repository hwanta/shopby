from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait   # 로딩될 때까지 대기
from selenium.webdriver.support import expected_conditions as EC # 로딩될 때까지 대기
from pages import create_driver


# 쇼핑몰 로그인
def login() :

    url = 'https://alpha-admin.shopby.co.kr'
    create_driver.driver.get(url)

    try :
        WebDriverWait(create_driver.driver, 10).until(EC.presence_of_element_located\
                                    ((By.XPATH,'//*[@id="container"]/div[2]/div/form/div/table/tr[1]/td/input')))
        create_driver.driver.find_element(by=By.XPATH,
                                          value='//*[@id="container"]/div[2]/div/form/'
                                                'div/table/tr[1]/td/input').send_keys('shopbyproadmin')  # xpath 사용
        create_driver.driver.find_element(by=By.CSS_SELECTOR,
                                          value='#container > div.content_login > div > '
                                                'form > div > table > tr:nth-child(2) > td > input').send_keys('WkaQhd@629') # css_selector 사용
        create_driver.driver.find_element(by=By.CSS_SELECTOR, value='#container > div.content_login > div > form > button:nth-child(2)').click()
    
        # alert 존재하면 내용 출력, 없으면 pass 출력
        WebDriverWait(create_driver.driver, 3).until(EC.alert_is_present())
        alert = create_driver.driver.switch_to.alert
        print("login : Fail")
        print(alert.text)
        alert.accept()
    except : 
        print("login : Pass")

    # 비밀번호 변경 팝업 출력 시 [다음에 변경하기] 버튼 클릭
    popup = create_driver.driver.find_element(by=By.CLASS_NAME, value='layer_popup').is_displayed()
    if popup :
        create_driver.driver.find_element(by=By.CSS_SELECTOR,
                            value='#container > div.content_login > div.layer_popup_wrap.ncp_layerpopup > div > '
                                  'div.lp_content > div > div.lp_footer > button.lp_close_btn.medium.lp_close').click()
