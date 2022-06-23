from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # 로딩될 때까지 대기
from selenium.webdriver.support import expected_conditions as EC  # 로딩될 때까지 대기
from pages.setting import option
import time, random
from selenium.webdriver.common.keys import Keys
from libs import login, element, create_driver
from selenium.webdriver.support.select import Select

def accessProductList() :
    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.CSS_SELECTOR,'body > div > div.header-wrap > div.gnb-wrap > div.left-wrap > ul > li.on > a')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="상품").click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.LINK_TEXT,'상품 관리')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="상품 관리").click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.LINK_TEXT,'상품 등록')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="상품 등록").click()

def momo() :
    element.ClickByText('일반 상품', '1')