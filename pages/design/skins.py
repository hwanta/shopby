from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # 로딩될 때까지 대기
from selenium.webdriver.support import expected_conditions as EC  # 로딩될 때까지 대기
from pages.setting import option
import time, random
from selenium.webdriver.common.keys import Keys
from libs import login, element
from selenium.webdriver.support.select import Select

# 디자인 > 디자인 관리 > 권한 스킨 리스트
def accessSkins() :
    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.CSS_SELECTOR,'body > div > div.header-wrap > div.gnb-wrap > div.left-wrap > ul > li.on > a')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="디자인").click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.LINK_TEXT,'디자인 관리')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="디자인 관리").click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.LINK_TEXT,'디자인 스킨 리스트')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="디자인 스킨 리스트").click()

# 디자인 > 디자인 관리 > 권한 스킨 리스트 > PC 미리보기 (TC_1~2)
def pcPreview() :
    # 현재 설정된 디자인 스킨 > PC 선택
    element.ClickByLINKTEXT('PC', '1-1')
    # 사용중인 디자인 스킨 [미리보기] 클릭 (TC_1)
    element.ClickByXPath(
        '/html/body/div/div[3]/div[2]/div[1]/div[1]/div[2]/div[2]/table/tbody/tr/td[1]/div/div[2]/div[1]/button', '1')
    # 작업중인 디자인 스킨 [미리보기] 클릭 (TC_2)
    element.ClickByXPath(
        '/html/body/div/div[3]/div[2]/div[1]/div[1]/div[2]/div[2]/table/tbody/tr/td[2]/div/div[2]/div[1]/button', '2')

def moPreview():
    # 현재 설정된 디자인 스킨 > MO 선택
    element.ClickByLINKTEXT('Mobile', '1-2')
    # 사용중인 디자인 스킨 [미리보기] 클릭 (TC_3)
    element.ClickByXPath(
        '/html/body/div/div[3]/div[2]/div[1]/div[1]/div[2]/div[2]/table/tbody/tr/td[1]/div/div[2]/div[1]/button', '3')
    # 작업중인 디자인 스킨 [미리보기] 클릭 (TC_4)
    element.ClickByXPath(
        '/html/body/div/div[3]/div[2]/div[1]/div[1]/div[2]/div[2]/table/tbody/tr/td[2]/div/div[2]/div[1]/button', '4')



