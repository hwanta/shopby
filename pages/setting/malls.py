from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait   # 로딩될 때까지 대기
from selenium.webdriver.support import expected_conditions as EC # 로딩될 때까지 대기
from pages import login
from pages.setting import option
import time


# 설정 > 기본정책 > 쇼핑몰관리
# 신규 쇼핑몰 등록
def addMall() :

    option.mallManagement()
    try:
    # 신규 쇼핑몰 등록 버튼 클릭
        addMall = login.create_driver.driver.find_element(by=By.XPATH,
                                            value='//*[@id="mall-list-grid"]/div/div/div/div[1]/div/button')
        addMall.click()
        WebDriverWait(login.create_driver.driver, 3).until(EC.alert_is_present())
        alert = login.create_driver.driver.switch_to.alert
        print(alert.text)
        alert.accept()
    except:
        print('신규 쇼핑몰 등록 버튼 클릭 시 alert 미출력됨')

# 쇼핑몰 수정
def editMall():

    option.mallManagement()
    # 내부 class 스크롤
    mallList = login.create_driver.driver.find_element(by=By.CLASS_NAME,
                                                value='tui-grid-body-area')
    login.create_driver.driver.execute_script("arguments[0].scrollBy(0,470)", mallList)

    # 쇼핑몰명 클릭
    try:
        mallName = login.create_driver.driver.find_element(by=By.LINK_TEXT,
                                                value='shopbypro_QA_11111')
        mallName.click()
        WebDriverWait(login.create_driver.driver, 3).until(EC.alert_is_present())
        alert = login.create_driver.driver.switch_to.alert
        print(alert.text)
        alert.accept()
    except:
        print('쇼핑몰명 클릭 시 alert 미출력됨')

# 쇼핑몰 등록/수정 이외의 부분
def mallMange() :

    option.mallManagement()
    # 내부 class 스크롤
    mallList = login.create_driver.driver.find_element(by=By.CLASS_NAME,
                                                       value='tui-grid-body-area')
    login.create_driver.driver.execute_script("arguments[0].scrollBy(0,470)", mallList)

    # PC웹 클릭
    try:
        _PCWeb = login.create_driver.driver.find_element(by=By.XPATH,
                                             value='//*[@id="mall-list-grid"]/div/div/div/div[2]/div'
                                                   '/div/div[1]/div[2]/div[2]/div/div[1]/table/tbody/tr/td[2]/div')
        _PCWeb.click()
        WebDriverWait(login.create_driver.driver, 3).until(EC.alert_is_present())
        alert = login.create_driver.driver.switch_to.alert
        print(alert.text)
        alert.accept()
    except:
        print('PC웹 클릭 시 alert 미출력됨')

    time.sleep(1)  # PC웹 출력되고 1초 대기

    # 현재 탭을 1번 탭으로 변경 후 해당 탭 닫기
    login.create_driver.driver.switch_to.window(login.create_driver.driver.window_handles[1])
    login.create_driver.driver.close()

    # 다시 현재 탭 0번 탭으로 변경
    login.create_driver.driver.switch_to.window(login.create_driver.driver.window_handles[0])

    # 모바일웹 클릭
    try:
        _MobileWeb = login.create_driver.driver.find_element(by=By.XPATH,
                                          value='//*[@id="mall-list-grid"]/div/div/div/div[2]/div/'
                                                'div/div[1]/div[2]/div[2]/div/div[1]/table/tbody/tr/td[3]/div/a')
        _MobileWeb.click()
        WebDriverWait(login.create_driver.driver, 3).until(EC.alert_is_present())
        alert = login.create_driver.driver.switch_to.alert
        print(alert.text)
        alert.accept()
    except:
        print('모바일웹 클릭 시 alert 미출력됨')

    # 현재 탭을 1번 탭으로 변경 후 해당 탭 닫기
    login.create_driver.driver.switch_to.window(login.create_driver.driver.window_handles[1])
    login.create_driver.driver.close()

    # 다시 현재 탭 0번 탭으로 변경
    login.create_driver.driver.switch_to.window(login.create_driver.driver.window_handles[0])





