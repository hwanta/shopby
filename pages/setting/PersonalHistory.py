from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # 로딩될 때까지 대기
from selenium.webdriver.support import expected_conditions as EC  # 로딩될 때까지 대기
from pages.setting import option
import time, random
from selenium.webdriver.common.keys import Keys
from libs import login, element
from selenium.webdriver.support.select import Select


# 설정 > 보안정책 > 개인정보접속기록 조회
def accessPersonalHistory() :
    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.CSS_SELECTOR,'body > div > div.header-wrap > div.gnb-wrap > div.left-wrap > ul > li.on > a')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="설정").click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.LINK_TEXT,'보안정책')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="보안정책").click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.LINK_TEXT,'개인정보접속기록 조회')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="개인정보접속기록 조회").click()


# 설정 > 개인정보접속기록 > 회원정보 접속기록(TC_339)
def accessMember():
    element.ClickByLINKTEXT('회원정보 접속기록', '339-1')
    element.ClickByXPath('//*[@id="searchForm"]/table/tbody/tr[3]/td/div/span[1]/button[5]', '339-2')
    element.ClickByXPath('//*[@id="searchForm"]/table/tbody/tr[2]/td[2]/div/button[1]', '339-3')


# 설정 > 개인정보접속기록 > 운영자정보 접속기록(TC_340)
def accessOperator():
    element.ClickByLINKTEXT('운영자정보 접속기록', '340-1')
    element.ClickByXPath('//*[@id="searchForm"]/table/tbody/tr[3]/td/div/span[1]/button[5]', '340-2')
    element.ClickByXPath('//*[@id="searchForm"]/table/tbody/tr[2]/td[2]/div/button[1]', '340-3')