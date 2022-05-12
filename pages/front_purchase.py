import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait   # 로딩될 때까지 대기
from selenium.webdriver.support import expected_conditions as EC # 로딩될 때까지 대기
from selenium.webdriver import ActionChains


# 상품 구매
def productPurchase():

    # 신규 카테고리 진입
    WebDriverWait(lib.create_driver.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT,
                                                '신규 카테고리')))
    lib.create_driver.driver.find_element(by=By.LINK_TEXT, value="신규 카테고리").click()

    # 코듀로이 셔츠 무배 클릭
    WebDriverWait(lib.create_driver.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT,
                                                                                '코듀로이 셔츠 무배')))
    lib.create_driver.driver.find_element(by=By.LINK_TEXT, value="코듀로이 셔츠 무배").click()

    time.sleep(1)
    # 주문하기 버튼 클릭
    WebDriverWait(lib.create_driver.driver, 10).until(EC.presence_of_element_located((By.ID,
                                                                                'orderBtn')))
    lib.create_driver.driver.find_element(by=By.ID, value="orderBtn").click()

    time.sleep(1)
    # 무통장입금 라디오버튼 클릭
    WebDriverWait(lib.create_driver.driver, 10).until(EC.presence_of_element_located((By.ID,
                                                                                'paymethod-ACCOUNT')))
    # ActionChains 사용하여 해당 요소에 접근 후 클릭
    element = lib.create_driver.driver.find_element(by=By.CSS_SELECTOR, value="#payMethodList > div:nth-child(2) > label")
    action = ActionChains(lib.create_driver.driver)
    action.move_to_element(element).click().perform()

    # 입금자명 입력
    lib.create_driver.driver.find_element(by=By.NAME, value="remitter").send_keys('123')

    # 개인정보 수집 동의/ 구매진행 동의
    lib.create_driver.driver.find_element(by=By.CSS_SELECTOR, value="#termsChecks > div:nth-child(1) > label").click()
    lib.create_driver.driver.find_element(by=By.CSS_SELECTOR, value="#termsChecks > div:nth-child(3) > label").click()

    # 결제하기 버튼 클릭
    lib.create_driver.driver.find_element(by=By.ID, value="orderBuy").click()


