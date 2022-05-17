from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # 로딩될 때까지 대기
from selenium.webdriver.support import expected_conditions as EC  # 로딩될 때까지 대기
from pages.setting import option
import time, random
from selenium.webdriver.common.keys import Keys
from libs import login, element
from selenium.webdriver.support.select import Select


# 설정 > 관리정책 > 권한 관리
def accessPermissionGroup() :
    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.CSS_SELECTOR,'body > div > div.header-wrap > div.gnb-wrap > div.left-wrap > ul > li.on > a')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="설정").click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.LINK_TEXT,'관리정책')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="관리정책").click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.LINK_TEXT,'권한그룹 관리')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="권한그룹 관리").click()


# 설정 > 권한그룹 관리 > 권한그룹명(TC_305)
def authorityName():
    element.InputByXPath('//*[@id="searchForm"]/table/tbody/tr[1]/td[1]/div/div/input','테스트','305')


# 설정 > 권한그룹 관리 > 상세검색(TC_307,309)
def authoritySearch():
    # 개인정보 목록조회 드롭박스 클릭
    try:
        select = Select(login.create_driver.driver.find_element(by=By.XPATH,
                                                                value='//*[@id="searchForm"]/table/tbody/tr[2]/td/select[1]'))
        select.select_by_value("false")
        time.sleep(1)
        print("TC " + '307' + " PASS")
    except Exception as e:
        print(e)
        print("TC " + '307' + " Fail")

    # 상품관리 권한 드롭박스 클릭
    try:
        select = Select(login.create_driver.driver.find_element(by=By.XPATH,
                                                                value='//*[@id="searchForm"]/table/tbody/tr[2]/td/select[2]'))
        select.select_by_value("false")
        time.sleep(1)
        print("TC " + '309' + " PASS")
    except Exception as e:
        print(e)
        print("TC " + '309' + " Fail")


# 설정 > 권한그룹 관리 > 검색버튼(TC_310,311)
def searchButton():
    # 검색
    element.ClickByXPath('//*[@id="searchForm"]/table/tbody/tr[1]/td[2]/div/button[1]', '310-1')
    search = login.create_driver.driver.find_element(By.XPATH,value='/html/body/div/div[3]/div[2]/div[1]/div/div/div/div[2]/'
                                                                    'div/div/div[1]/div[2]/div[2]/div/div[1]/table/tbody/tr/td[1]').text

    if search.__contains__('권한'):
        print("TC " + '310-2' + " PASS")
    else:
        print("TC " + '310-2' + " Fail")

    # 초기화
    element.ClickByXPath('//*[@id="searchForm"]/table/tbody/tr[1]/td[2]/div/button[2]', '311-1')
    # 권한그룹명 inputbox text로 담음
    reset = login.create_driver.driver.find_element(By.XPATH,value='//*[@id="searchForm"]/table/tbody/tr[1]/td[1]/div/div/input').text

    if reset == '':
        print("TC " + '311-2' + " PASS")
    else:
        print("TC " + '311-2' + " Fail")


# 설정 > 권한그룹 관리 > 권한그룹 등록 버튼(TC_312)
def clickRegistration():
    element.ClickByXPath('/html/body/div[1]/div[3]/div[2]/div[1]/div/div/div/div[1]/div/button','312-1')
    registration = login.create_driver.driver.find_element(By.XPATH,value='/html/body/div[1]/div[3]/div[1]/div[1]/div').text

    if registration == '권한그룹 등록':
        print("TC " + '312-2' + " PASS")
    else:
        print("TC " + '312-2' + " Fail")


# 권한그룹 등록 > 쇼핑몰 선택(TC_314,315)
def selectMall():
    element.ClickByID('AllSelectCheckbox_all-select-mall', '314')
    element.ClickByID('MallCheckbox_4362', '315-1')
    element.ClickByID('MallCheckbox_4395', '315-2')


# 권한그룹 등록 > 권한 그룹명(TC_316)
def addName():
    element.InputByXPath('/html/body/div/div[3]/div[2]/div[1]/div[1]/div[2]/table/tbody/tr[2]/td/div/div/input',
                         '테스트 권한' + str(element.randomNumT),'316')


# 권한그룹 등록 > 권한그룹 설명(TC_317)
def addDescription():
    element.InputByXPath('/html/body/div/div[3]/div[2]/div[1]/div[1]/div[2]/table/tbody/tr[3]/td/div/div/input',
                         '테스트 권한그룹 설명' + str(element.randomNumT),'317')


# 권한그룹 등록 > 개인정보 목록조회(TC_318)
def addListInquiry():
    element.ClickByNameIndex('radio-privacy-authority', 0, '318-1')
    element.ClickByNameIndex('radio-privacy-authority', 1, '318-2')


# 권한그룹 등록 > 1차 메뉴 기준으로 보기 드롭박스(TC_320)
def selectBox1():
    try:
        select = Select(login.create_driver.driver.find_element(by=By.XPATH,
                                                                value='/html/body/div/div[3]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/select'))
        select.select_by_index(random.randrange(0, 3))
        time.sleep(1)
        print("TC " + '320' + " PASS")
    except Exception as e:
        print(e)
        print("TC " + '320' + " Fail")


# 권한그룹 등록 > 권한 선택 드롭박스(TC_322)
def selectBox2():
    try:
        select = Select(login.create_driver.driver.find_element(by=By.XPATH,
                                                                value='/html/body/div/div[3]/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/select'))
        select.select_by_index(random.randrange(1, 4))
        time.sleep(1)
        print("TC " + '322' + " PASS")
    except Exception as e:
        print(e)
        print("TC " + '322' + " Fail")


# 권한그룹 등록 > 전체 체크박스(TC_323)
def checkBox():
    element.ClickByXPath('/html/body/div/div[3]/div[2]/div[1]/div[2]/div[2]/div[3]/table/thead/tr/th[1]/span/input', '323')


# 권한그룹 등록 > 일괄적용 버튼(TC_324)
def button():
    element.ClickByXPath('/html/body/div[1]/div[3]/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/button', '324')



