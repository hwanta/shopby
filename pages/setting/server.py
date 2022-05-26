from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # 로딩될 때까지 대기
from selenium.webdriver.support import expected_conditions as EC  # 로딩될 때까지 대기
from pages.setting import option
import time, random
from selenium.webdriver.common.keys import Keys
from libs import login, element
from selenium.webdriver.support.select import Select


# 설정 > 보안정책 > 보안서버 관리
def accessServer() :
    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.CSS_SELECTOR,'body > div > div.header-wrap > div.gnb-wrap > div.left-wrap > ul > li.on > a')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="설정").click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.LINK_TEXT,'보안정책')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="보안정책").click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.LINK_TEXT,'보안서버 관리')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="보안서버 관리").click()


# 설정 > 보안서버 관리(TC_341)
def securityServer():
    text = login.create_driver.driver.find_element(By.XPATH, value='/html/body/div[1]/div[3]/div[1]/div[1]/div/h2').text
    if text == '보안서버 관리':
        print("TC " + '341' + " PASS")
    else:
        print("TC " + '341' + " Fail")