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

# 회원리스트_검색
def MemberListSearch():
    searchWord = login.create_driver.driver.find_element(by=By.XPATH, value='//*[@id="searchForm"]/table/tbody/tr[2]/td/div/input') #검색어 입력 찾기
    searchWord.clear()
    searchWord.send_keys('bomee331') # 회원리스트 아이디 검색어 입력
    search = login.create_driver.driver.find_element(by=By.XPATH, value='//*[@id="searchForm"]/table/tbody/tr[1]/td[2]/div/button[1]') #검색 버튼 찾기
    search.click() # search 클릭
    print("searchWord : pass")

