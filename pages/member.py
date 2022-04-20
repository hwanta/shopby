from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # 로딩될 때까지 대기
from selenium.webdriver.support import expected_conditions as EC  # 로딩될 때까지 대기
from pages import login,create_driver


# 회원 메뉴
def MemberList():
    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located \
                                              ((By.LINK_TEXT, '회원')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value='회원').click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located \
                                              ((By.LINK_TEXT, '회원관리')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="회원관리").click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located \
                                              ((By.LINK_TEXT, '회원 리스트')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="회원 리스트").click()

