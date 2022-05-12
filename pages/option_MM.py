from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait   # 로딩될 때까지 대기
from selenium.webdriver.support import expected_conditions as EC # 로딩될 때까지 대기
from pages.setting import option


# 설정 > 기본정책 > 쇼핑몰관리
# 신규 쇼핑몰 등록
def clickMall() :

    option.mallManagement()
    try:
    # 신규 쇼핑몰 등록 버튼 클릭
        addMall = lib.create_driver.driver.find_element(by=By.XPATH,
                                                        value='//*[@id="mall-list-grid"]/div/div/div/div[1]/div/button')
        addMall.click()
        WebDriverWait(lib.create_driver.driver, 3).until(EC.alert_is_present())
        alert = lib.create_driver.driver.switch_to.alert
        print(alert.text)
        alert.accept()
    except:
        print('pass')

def clickMallName() :

    option.mallManagement()
    # 내부 class 스크롤
    mallList = lib.create_driver.driver.find_element(by=By.CLASS_NAME,
                                                     value='tui-grid-body-area')
    lib.create_driver.driver.execute_script("arguments[0].scrollBy(0,470)", mallList)

    # 쇼핑몰명 클릭
    try:
        mallName = lib.create_driver.driver.find_element(by=By.LINK_TEXT,
                                                         value='shopbypro_QA_11111')
        mallName.click()
        WebDriverWait(lib.create_driver.driver, 3).until(EC.alert_is_present())
        alert = lib.create_driver.driver.switch_to.alert
        print(alert.text)
        alert.accept()
    except:
        print('pass')

def clickPC() :

    option.mallManagement()
    # 내부 class 스크롤
    mallList = lib.create_driver.driver.find_element(by=By.CLASS_NAME,
                                                     value='tui-grid-body-area')
    lib.create_driver.driver.execute_script("arguments[0].scrollBy(0,470)", mallList)

    # PC웹 클릭
    try:
        _PCWeb = lib.create_driver.driver.find_element(by=By.XPATH,
                                                       value='//*[@id="mall-list-grid"]/div/div/div/div[2]/div/div/div[1]/'
                                                'div[2]/div[2]/div/div[1]/table/tbody/tr[10]/td[2]/div/a')
        _PCWeb.click()
        WebDriverWait(lib.create_driver.driver, 3).until(EC.alert_is_present())
        alert = lib.create_driver.driver.switch_to.alert
        print(alert.text)
        alert.accept()
    except:
        print('pass')

def clickMobile() :

    option.mallManagement()

    # 내부 class 스크롤
    mallList = lib.create_driver.driver.find_element(by=By.CLASS_NAME,
                                                     value='tui-grid-body-area')
    lib.create_driver.driver.execute_script("arguments[0].scrollBy(0,470)", mallList)

    # 모바일웹 클릭
    try:
        _MobileWeb = lib.create_driver.driver.find_element(by=By.XPATH,
                                                           value='//*[@id="mall-list-grid"]/div/div/div/div[2]/div/div/div[1]/'
                                                'div[2]/div[2]/div/div[1]/table/tbody/tr[10]/td[3]/div/a')
        _MobileWeb.click()
        WebDriverWait(lib.create_driver.driver, 3).until(EC.alert_is_present())
        alert = lib.create_driver.driver.switch_to.alert
        print(alert.text)
        alert.accept()
    except:
        print('pass')




