from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # 로딩될 때까지 대기
from selenium.webdriver.support import expected_conditions as EC  # 로딩될 때까지 대기
from pages.setting import option
from selenium.webdriver.common.keys import Keys
from libs import login, element
from selenium.webdriver.support.select import Select
import time, random


# 설정 > 관리정책 > 운영자 관리
def accessAdmin():
    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located \
                                                            ((By.CSS_SELECTOR,
                                                              'body > div > div.header-wrap > div.gnb-wrap > div.left-wrap > ul > li.on > a')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="설정").click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located \
                                                            ((By.LINK_TEXT, '관리정책')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="관리정책").click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located \
                                                            ((By.LINK_TEXT, '운영자 관리')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="운영자 관리").click()


# 운영자 관리 > 검색어(TC_266,267)
def searchWord():
    # 드롭박스 클릭
    try:
        select = Select(login.create_driver.driver.find_element(by=By.XPATH,
                                                                value='//*[@id="searchForm"]/table/tbody/tr[1]/td[1]/select'))
        select.select_by_value("ADMIN_NAME")
        time.sleep(1)
        print("TC " + '266' + " PASS")
    except Exception as e:
        print(e)
        print("TC " + '266' + " Fail")

    # 검색어 입력
    element.InputByXPath('//*[@id="searchForm"]/table/tbody/tr[1]/td[1]/div/div/input', '안아련', '267')


# 운영자 관리 > 상태(TC_269)
def state():
    # ㅁ전체선택 클릭
    element.ClickById('admin-status-checkbox_all', '269-1')
    # ㅁ등록대기 클릭
    element.ClickById('admin-status-checkbox_register', '269-2')
    # ㅁ정상 클릭
    element.ClickById('admin-status-checkbox_normal', '269-3')
    # ㅁ로그인 잠김 클릭
    element.ClickById('admin-status-checkbox_blockLogin', '269-4')
    # ㅁ장기 미로그인 운영자 클릭(해당 부분은 추후수정 필요)
    # element.ClickByID('admin-not-logined-long-time-checkbox_longNoneLogin', '269-5')


# 운영자 관리 > 상세검색(TC_272,274)
def advancedSearch():
    # 소속부서 드롭박스 클릭
    element.ClickByCSS_Selector('#searchForm > table > tbody > tr:nth-child(3) > td > select:nth-child(1)', '272')

    # 직책 드롭박스 클릭
    element.ClickByCSS_Selector('#searchForm > table > tbody > tr:nth-child(3) > td > select:nth-child(1)', '274')


# 운영자 관리 > 검색/초기화(TC_275~277)
def searchButton():
    element.ClickByXPath('//*[@id="searchForm"]/table/tbody/tr[1]/td[2]/div/button[1]', 275)

    findword = login.create_driver.driver.find_element(By.XPATH, value='/html/body/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[1]/table/tbody/tr[2]/td[2]/div').text

    time.sleep(1)

    if findword == '안아련':
        print("TC " + '276' + " PASS")
    else:
        print("TC " + '276' + " Fail")

    # 초기화 버튼 클릭
    element.ClickByXPath('//*[@id="searchForm"]/table/tbody/tr[1]/td[2]/div/button[2]', '277')


# 운영자 관리 > 운영자 등록 버튼(TC_279)
def clickRegistration():
    element.ClickByXPath('/html/body/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div/button', '279')


# 운영자 등록 > 운영자명(TC_281)
def operatorName():
    element.InputByName('adminName','새로운 운영자' + str(element.randomNumT), '281')


# 운영자 등록 > 이메일(TC_282)
def operatorEmail():
    element.InputByName('emailId','dlquddnr' + str(element.randomNumT), '282-1')
    element.InputByName('emailDomain','naver.com' + str(element.randomNumT), '282-2')


# 운영자 등록 > 권한그룹(TC_284)
def permissionGroup():
    try:
        select = Select(login.create_driver.driver.find_element(by=By.XPATH,
                                                                value='/html/body/div/div[4]/div[1]/div/div/'
                                                                      'div[2]/div/table/tbody/tr[3]/td/select'))
        select.select_by_value(random.choice(['1990', '1991', '1992']))
        time.sleep(1)
        print("TC " + '284' + " PASS")
    except Exception as e:
        print(e)
        print("TC " + '284' + " Fail")


# 운영자 등록 > 취소(TC_285)
def cancelRegistration():
    # login.create_driver.driver.find_element(By.XPATH, value='/html/body/div/div[3]/div[2]/'
    #                                                         'div[1]/div/div/div/div[1]/div/button').click()
    element.ClickByXPath('/html/body/div/div[4]/div[1]/div/div/div[2]/div/div/button[1]', '285')


# 운영자 등록 > 저장(TC_286)
# def saveRegistration():
#     try:
#         login.create_driver.driver.find_element(By.XPATH, value='/html/body/div/div[4]/div[1]/'
#                                                                 'div/div/div[2]/div/div/button[2]').click()
#         time.sleep(1)
#         WebDriverWait(login.create_driver.driver, 3).until(EC.alert_is_present())
#         alert = login.create_driver.driver.switch_to.alert
#         alert.accept()
#         print("TC " + '286' + " PASS")
#         return True
#     except Exception as e:
#         print(e)
#         print("TC " + '286' + " Fail")
#         return False


# 운영자 관리 > 운영자 수정 진입(TC_290)
def editOperator():
    # 운영자 관리 페이지 재진입
    accessAdmin()
    time.sleep(2)

    # protest1 (id) 클릭
    element.ClickByLinkText('protest2', '290-1')
    confirm = login.create_driver.driver.find_element(By.CSS_SELECTOR, value='body > div > div.container-wrap > '
                                                                             'div.content-top-wrap > div:nth-child(1)'
                                                                             ' > div > h2').text
    if confirm == '운영자 수정':
        print("TC " + '290-2' + " PASS")
    else:
        print("TC " + '290-2' + " Fail")

    # c_url = login.create_driver.driver.current_url
    # if c_url == 'https://alpha-admin.shopby.co.kr/pro/configuration/management/admin/edit?adminNo=148397':
    #     print("TC " + '290-2' + " PASS")
    # else:
    #     print("TC " + '290-2' + " Fail")


# 운영자 수정 > 이메일(TC_290)
def editEmail():
    element.InputByName('emailId','dlquddnr' + str(element.randomNumT), '290-1')
    element.InputByName('emailDomain','naver.com' + str(element.randomNumT), '290-2')


# 운영자 수정 > 전화번호(TC_296)
def editPhoneNum():
    element.InputByName('phoneNo','01000000000', '292')


# 운영자 수정 > 소속부서(TC_297)
def editAffiliationDepartment():

    # clear 작동하지 않을 때 사용
    clear_ele = login.create_driver.driver.find_element(By.XPATH, value='/html/body/div/div[3]/div[2]/div[1]/div[1]/div/table/tbody/tr[6]/td/div/div/input')
    clear_ele.send_keys(Keys.CONTROL + 'a')
    clear_ele.send_keys(Keys.DELETE)

    element.InputByXPath('/html/body/div/div[3]/div[2]/div[1]/div[1]/div/table/tbody/tr[6]/td/div/div/input',
                         '소속부서 테스트' + str(element.randomNumT), '297')
    try:
        popup = login.create_driver.driver.find_element(By.XPATH, value='/html/body/div/div[3]/div[2]/div[1]/div[1]/div'
                                                                        '/table/tbody/tr[6]/td/div/div/div/button')
        popup.click()
    except:
        print("이미 있는 소속부서임")


# 운영자 수정 > 직급(TC_298)
def editRank():
    element.InputByName('jobPositionName','직급 테스트' + str(element.randomNumT), '298')


# 운영자 수정 > 직책(TC_299)
def editPosition():

    # clear 작동하지 않을 때 사용
    clear_ele = login.create_driver.driver.find_element(By.XPATH, value='/html/body/div/div[3]/div[2]/div[1]/div[1]/'
                                                                        'div/table/tbody/tr[7]/td[2]/div/div/input')
    clear_ele.send_keys(Keys.CONTROL + 'a')
    clear_ele.send_keys(Keys.DELETE)

    element.InputByXPath('/html/body/div/div[3]/div[2]/div[1]/div[1]/div/'
                         'table/tbody/tr[7]/td[2]/div/div/input','직책 테스트' + str(element.randomNumT), '299')
    try:
        popup = login.create_driver.driver.find_element(By.XPATH, value='/html/body/div/div[3]/div[2]/div[1]/div[1]/div'
                                                                        '/table/tbody/tr[7]/td[2]/div/div/div/button')
        popup.click()
    except:
        print("이미 있는 직책임")


# 운영자 수정 > 권한그룹(TC_301)
def editPermissionGroup():
    try:
        select = Select(login.create_driver.driver.find_element(by=By.XPATH,
                                                                value='/html/body/div/div[3]/div[2]/div[1]/'
                                                                      'div[1]/div/table/tbody/tr[8]/td/select'))
        select.select_by_value(random.choice(['1990', '1991', '1992']))
        time.sleep(1)
        print("TC " + '301' + " PASS")
    except Exception as e:
        print(e)
        print("TC " + '301' + " Fail")


# 운영자 수정 > 운영자 삭제(TC_302)
# def deleteOperator():
#     try:
#         button = login.create_driver.driver.find_element(By.XPATH,
#                                                              value='/html/body/div/div[4]/div/div[1]/button')
#         login.create_driver.driver.execute_script("arguments[0].click();", button)
#         time.sleep(1)
#         WebDriverWait(login.create_driver.driver, 3).until(EC.alert_is_present())
#         alert = login.create_driver.driver.switch_to.alert
#         alert.accept()
#         print("TC " + '302' + " PASS")
#         return True
#     except Exception as e:
#         print(e)
#         print("TC " + '302' + " Fail")
#         return False


# 운영자 수정 > 저장(TC_303)
def save():
    try:
        button = login.create_driver.driver.find_element(By.XPATH,
                                                             value='/html/body/div/div[4]/div/div[2]/button[2]')
        login.create_driver.driver.execute_script("arguments[0].click();", button)
        time.sleep(1)
        WebDriverWait(login.create_driver.driver, 3).until(EC.alert_is_present())
        alert = login.create_driver.driver.switch_to.alert
        alert.accept()
        print("TC " + '303' + " PASS")
        return True
    except Exception as e:
        print(e)
        print("TC " + '303' + " Fail")
        return False


# 운영자 수정 > 목록(TC_304)
def operatorList():
    login.create_driver.driver.find_element(By.LINK_TEXT, value='autopro1').click()
    time.sleep(2)

    try:
        button = login.create_driver.driver.find_element(By.XPATH,
                                                             value='/html/body/div/div[4]/div/div[2]/button[1]')
        login.create_driver.driver.execute_script("arguments[0].click();", button)
        time.sleep(1)
        print("TC " + '304' + " PASS")
    except Exception as e:
        print(e)
        print("TC " + '304' + " Fail")




