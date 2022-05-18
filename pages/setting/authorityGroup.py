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
        select.select_by_index(random.randrange(2, 4))
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


# 권한그룹 등록 > 권한 초기화 버튼(TC_325)
def buttonReset():
    element.ClickByXPath('/html/body/div[1]/div[3]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/button', '325')
    try:
        while(True):
            WebDriverWait(login.create_driver.driver, 3).until(EC.alert_is_present())
            alert = login.create_driver.driver.switch_to.alert
            alert.accept()
    except:
        return


# 권한그룹 등록 > 상품담당자(MD)권한 선택(TC_326)
def buttonMD():
    try:
        select = Select(login.create_driver.driver.find_element(by=By.XPATH,
                                                                value='/html/body/div/div[3]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/select'))
        select.select_by_index(0)
        time.sleep(1)
    except Exception as e:
        print(e)
    login.create_driver.driver.find_element(By.CSS_SELECTOR, value='body').send_keys(Keys.PAGE_DOWN)
    element.ClickByXPath('//*[@id="md_md-check"]', '326')


# 권한그룹 등록 > 권한설정 라디오버튼(TC_328)
# def radioButton():
#     element.ClickByNameIndex('#none-menu-설정_1_1652833224117', '328-1')
#     try:
#         while(True):
#             WebDriverWait(login.create_driver.driver, 3).until(EC.alert_is_present())
#             alert = login.create_driver.driver.switch_to.alert
#             alert.accept()
#     except Exception as e:
#         print(e)
#     element.ClickByNameIndex('radio-menu-authority-상품_2_1652827167683', 1, '328-2')
#     try:
#         while(True):
#             WebDriverWait(login.create_driver.driver, 3).until(EC.alert_is_present())
#             alert = login.create_driver.driver.switch_to.alert
#             alert.accept()
#     except Exception as e:
#         print(e)
#     element.ClickByNameIndex('radio-menu-authority-주문/배송_3_1652827167683', random.randrange(0, 3), '328-3')
#     try:
#         while(True):
#             WebDriverWait(login.create_driver.driver, 3).until(EC.alert_is_present())
#             alert = login.create_driver.driver.switch_to.alert
#             alert.accept()
#     except Exception as e:
#         print(e)
#     element.ClickByNameIndex('radio-menu-authority-회원_4_1652827167683', random.randrange(0, 3), '328-4')
#     try:
#         while(True):
#             WebDriverWait(login.create_driver.driver, 3).until(EC.alert_is_present())
#             alert = login.create_driver.driver.switch_to.alert
#             alert.accept()
#     except Exception as e:
#         print(e)
#     element.ClickByNameIndex('radio-menu-authority-게시판_5_1652827167684', random.randrange(0, 3), '328-5')
#     try:
#         while(True):
#             WebDriverWait(login.create_driver.driver, 3).until(EC.alert_is_present())
#             alert = login.create_driver.driver.switch_to.alert
#             alert.accept()
#     except Exception as e:
#         print(e)
#     element.ClickByNameIndex('radio-menu-authority-프로모션_6_1652827167684', random.randrange(0, 3), '328-6')
#     try:
#         while(True):
#             WebDriverWait(login.create_driver.driver, 3).until(EC.alert_is_present())
#             alert = login.create_driver.driver.switch_to.alert
#             alert.accept()
#     except Exception as e:
#         print(e)
#     element.ClickByNameIndex('radio-menu-authority-디자인_7_1652827167684', random.randrange(0, 3), '328-7')
#     try:
#         while (True):
#             WebDriverWait(login.create_driver.driver, 3).until(EC.alert_is_present())
#             alert = login.create_driver.driver.switch_to.alert
#             alert.accept()
#     except Exception as e:
#         print(e)
#     element.ClickByNameIndex('radio-menu-authority-부가서비스_8_1652827167684', random.randrange(0, 3), '328-8')
#     try:
#         while(True):
#             WebDriverWait(login.create_driver.driver, 3).until(EC.alert_is_present())
#             alert = login.create_driver.driver.switch_to.alert
#             alert.accept()
#     except Exception as e:
#         print(e)
#     element.ClickByNameIndex('radio-menu-authority-마케팅_9_1652827167684', random.randrange(0, 3), '328-9')
#     try:
#         while(True):
#             WebDriverWait(login.create_driver.driver, 3).until(EC.alert_is_present())
#             alert = login.create_driver.driver.switch_to.alert
#             alert.accept()
#     except Exception as e:
#         print(e)
#     element.ClickByNameIndex('radio-menu-authority-통계_10_1652827167684', random.randrange(0, 3), '328-10')
#     try:
#         while(True):
#             WebDriverWait(login.create_driver.driver, 3).until(EC.alert_is_present())
#             alert = login.create_driver.driver.switch_to.alert
#             alert.accept()
#     except Exception as e:
#         print(e)


# 권한그룹 등록 > 저장(TC_329)
def save():
    try:
        button = login.create_driver.driver.find_element(By.XPATH,
                                                             value='/html/body/div[1]/div[4]/div/div[2]/button[2]')
        login.create_driver.driver.execute_script("arguments[0].click();", button)
        time.sleep(1)
        WebDriverWait(login.create_driver.driver, 3).until(EC.alert_is_present())
        alert = login.create_driver.driver.switch_to.alert
        alert.accept()
        print("TC " + '329' + " PASS")
        return True
    except Exception as e:
        print(e)
        print("TC " + '329' + " Fail")
        return False


# 권한그룹 등록 > 목록(TC_330)
def authorityList():
    login.create_driver.driver.find_element(By.XPATH, value='/html/body/div[1]/div[3]/div[2]/div[1]/div/div/div/div[1]/div/button').click()
    time.sleep(2)
    element.ClickByXPath('/html/body/div[1]/div[4]/div/div[2]/button[1]', '330')


# 권한그룹 수정(TC_331)
def selectAuthority():
    editauthority = login.create_driver.driver.find_element(By.CSS_SELECTOR,
                                                            value='body > div > div.container-wrap > div.content-bottom-wrap > '
                                                                  'div.contents > div > div > div > div.content_item_bx > div > '
                                                                  'div > div.tui-grid-content-area > div.tui-grid-rside-area > '
                                                                  'div.tui-grid-body-area > div > div.tui-grid-table-container > '
                                                                  'table > tbody > tr:nth-child(1) > td:nth-child(1) > div > a').text
    element.ClickByCSS_SELECTOR('body > div > div.container-wrap > div.content-bottom-wrap > '
                                'div.contents > div > div > div > div.content_item_bx > div > '
                                'div > div.tui-grid-content-area > div.tui-grid-rside-area > '
                                'div.tui-grid-body-area > div > div.tui-grid-table-container > '
                                'table > tbody > tr:nth-child(1) > td:nth-child(1) > div > a', '331-1')

    defaultauthority = login.create_driver.driver.find_element(By.CSS_SELECTOR,
                                                               value='body > div > div.container-wrap > div.content-bottom-wrap > '
                                                                     'div.contents > div:nth-child(1) > div.box-cont > table > '
                                                                     'tbody > tr:nth-child(3) > td > div > div > input').get_attribute('type')
    if editauthority == '테스트':
        print("TC " + '331-1' + " PASS")
    else:
        print("TC " + '331-2' + " Fail")


# 권한그룹 수정(TC_322)
def editAuthority():
    # ㅁautoqa 쇼핑몰 선택
    element.ClickByID('MallCheckbox_4362', '322-1')

    # 권한그룹명 + randdomT 변수
    element.InputByXPath('/html/body/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/table/tbody/tr[3]/td/div/div/input', '테스트 권한' + str(element.randomNumT), '322-2')

    # 권한그룹 설명 + randdomT 변수
    element.InputByXPath('/html/body/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/table/tbody/tr[4]/td/div/div/input', '테스트 권한그룹 설명' + str(element.randomNumT), '322-3')

    # 개인정보 목록조회 ㅇ가능
    element.ClickByID('enable-privacy-authority', '322-4')
    login.create_driver.driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.PAGE_DOWN)

    # 모든 권한 읽기로 변경
    login.create_driver.driver.find_element(By.XPATH, value='/html/body/div[1]/div[3]/div[2]/div[1]/div[2]/div[2]/div[3]/table/thead/tr/th[1]/span/input').click()
    try:
        select = Select(login.create_driver.driver.find_element(by=By.XPATH,
                                                                value='/html/body/div[1]/div[3]/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/select'))
        select.select_by_index(2)
        time.sleep(1)
    except Exception as e:
        print(e)
        print("TC " + '322-5' + " Fail")
    element.ClickByXPath('/html/body/div[1]/div[3]/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/button', '322-5')

    # 저장버튼 클릭
    try:
        button = login.create_driver.driver.find_element(By.XPATH,
                                                             value='/html/body/div[1]/div[4]/div/div[2]/button[2]')
        login.create_driver.driver.execute_script("arguments[0].click();", button)
        time.sleep(1)
        WebDriverWait(login.create_driver.driver, 3).until(EC.alert_is_present())
        alert = login.create_driver.driver.switch_to.alert
        alert.accept()
        print("TC " + '322-6' + " PASS")
    except Exception as e:
        print(e)
        print("TC " + '322-6' + " Fail")


# 권한그룹 삭제(TC_333)
def deleteAuthority():
    # scroll = login.create_driver.driver.find_element(By.CSS_SELECTOR, value='body')
    # login.create_driver.driver.execute_script("arguments[0].scrollBy(0,470)", scroll)
    grid = login.create_driver.driver.find_element(By.CLASS_NAME, value='tui-grid-body-area')
    login.create_driver.driver.execute_script("arguments[0].scrollBy(1000,0)", grid)