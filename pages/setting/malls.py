from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait   # 로딩될 때까지 대기
from selenium.webdriver.support import expected_conditions as EC # 로딩될 때까지 대기
from pages.setting import option
import time, random
from selenium.webdriver.common.keys import Keys
from libs import login,element
from selenium.webdriver.support.select import Select


# 설정 > 쇼핑몰 관리 접속(TC_120)
def accessMalls():
    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.CSS_SELECTOR,'body > div > div.header-wrap > div.gnb-wrap > div.left-wrap > ul > li.on > a')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value='쇼핑몰관리').click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.LINK_TEXT,'기본정책')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value='쇼핑몰관리').click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.LINK_TEXT,'쇼핑몰관리')))
    element.ClickByLINKTEXT('쇼핑몰관리','120')


# 설정 > 쇼핑몰관리 > 신규 쇼핑몰 등록(TC_121)
def addMall():
    element.ClickByXPath('//*[@id="mall-list-grid"]/div/div/div/div[1]/div/button','121')


# 설정 > 쇼핑몰관리 > 쇼핑몰 수정(TC_141)
def accessEditMall():
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value='쇼핑몰관리').click()
    time.sleep(1)
    element.ClickByXPath('//*[@id="mall-list-grid"]/div/div/div/div[2]/div/div/'
                         'div[1]/div[2]/div[2]/div/div[1]/table/tbody/tr/td[1]/div/a','141')


# 쇼핑몰 수정 > 기본정보 > 쇼핑몰명(TC_143)
def mallName():
    element.InputByName('mall.mallName', 'autoqa' + str(element.randomNumI), '143')


# 쇼핑몰 수정 > 기본정보 > 고객센터 전화번호(TC_144)
def mallNumber():
    element.InputByName('mall.serviceCenter.phoneNo', '01000000000', '144')


# 쇼핑몰 수정 > 기본정보 > 고객센터 이메일(TC_145,146)
def mallEmail():
    element.InputByNameIndex('representative.email', 0, 'dlquddnr' + str(element.randomNumT), '145')
    element.InputByNameIndex('representative.email', 1, 'naver.com' + str(element.randomNumT), '146')


# 쇼핑몰 수정 > 접속설정 > PC웹 인트로(TC_147)
def intro_PC():
    element.ClickByNameIndex('introPage_PC', 0, '147-1')
    element.ClickByNameIndex('introPage_PC', 1, '147-2')
    element.ClickByNameIndex('introPage_PC', 2, '147-3')
    # element.ClickByNameIndex('introPage_PC', 3, '147-4') # 성인인증은 휴대폰 인증 등록되어 있어야만 가능


# 쇼핑몰 수정 > 접속설정 > 모바일웹 인트로(TC_148)
def intro_MO():
    element.ClickByNameIndex('introPage_Mobile', 0, '148-1')
    element.ClickByNameIndex('introPage_Mobile', 1, '148-2')
    element.ClickByNameIndex('introPage_Mobile', 2, '148-3')
    element.ClickByNameIndex('introPage_Mobile', 3, '148-4')


# 쇼핑몰 수정 > 접속설정 > 도메인(TC_149)
def domain():
    element.ClickByXPath('/html/body/div/div[3]/div[2]/div[1]/div[1]/'
                         'div[2]/div[2]/table/tbody/tr[2]/th/div/button', '149')

    login.create_driver.driver.switch_to.window(login.create_driver.driver.window_handles[1])
    login.create_driver.driver.close()
    login.create_driver.driver.switch_to.window(login.create_driver.driver.window_handles[0])


# 쇼핑몰 수정 > 접속설정 > 도메인 PC웹(TC_150)
def domain_PC():
    element.ClickByXPath('/html/body/div/div[3]/div[2]/div[1]/div[1]/div[2]/div[2]/'
                         'table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/a', '150')

    login.create_driver.driver.switch_to.window(login.create_driver.driver.window_handles[1])
    login.create_driver.driver.close()
    login.create_driver.driver.switch_to.window(login.create_driver.driver.window_handles[0])


# 쇼핑몰 수정 > 접속설정 > 도메인 모바일웹(TC_151)
def domain_MO():
    element.ClickByXPath('/html/body/div/div[3]/div[2]/div[1]/div[1]/div[2]/div[2]/'
                         'table/tbody/tr[2]/td/table/tbody/tr[2]/td/div/a', '151')

    login.create_driver.driver.switch_to.window(login.create_driver.driver.window_handles[1])
    login.create_driver.driver.close()
    login.create_driver.driver.switch_to.window(login.create_driver.driver.window_handles[0])


# 쇼핑몰 수정 > 결제수단 노출설정 > 무통장 입금(TC_152)
def account():
    # page down sleep 필수
    body = login.create_driver.driver.find_element(by=By.CSS_SELECTOR, value='body')
    body.send_keys(Keys.SPACE)
    time.sleep(1)

    element.ClickByNameIndex('orderConfig_account', 1, '152-1')
    element.ClickByNameIndex('orderConfig_account', 0, '152-2')


# 쇼핑몰 수정 > 결제수단 노출설정 > 신용카드(TC_153)
def creditCard():
    element.ClickByNameIndex('orderConfig_credit_card', 1, '153-1')
    element.ClickByNameIndex('orderConfig_credit_card', 0, '153-2')


# 쇼핑몰 수정 > 결제수단 노출설정 > 계좌이체(TC_154)
def realtimeAccount():
    element.ClickByNameIndex('orderConfig_realtime_account', 1, '154-1')
    element.ClickByNameIndex('orderConfig_realtime_account', 0, '154-2')


# 쇼핑몰 수정 > 결제수단 노출설정 > 가상계좌(TC_155)
def virtualAccount():
    element.ClickByNameIndex('orderConfig_virtual_account', 1, '155-1')
    element.ClickByNameIndex('orderConfig_virtual_account', 0, '155-2')


# 쇼핑몰 수정 > 결제수단 노출설정 > 에스크로 계좌이체(TC_156)
def escrowRealtimeAccount():
    element.ClickByNameIndex('orderConfig_escrow_realtime_account', 1, '156-1')
    element.ClickByNameIndex('orderConfig_escrow_realtime_account', 0, '156-2')


# 쇼핑몰 수정 > 결제수단 노출설정 > 에스크로 가상계좌(TC_157)
def escrowVirtualAccount():
    element.ClickByNameIndex('orderConfig_escrow_virtual_account', 1, '157-1')
    element.ClickByNameIndex('orderConfig_escrow_virtual_account', 0, '157-2')


# 쇼핑몰 수정 > 결제수단 노출설정 > 간편결제 PAYCO (TC_158)
def payco():
    element.ClickByNameIndex('orderConfig_payco', 1, '158-1')
    element.ClickByNameIndex('orderConfig_payco', 0, '158-2')


# 쇼핑몰 수정 > 결제정보 > 계좌정보 수정 (TC_161)
def accountInfoEdit():
    # page down sleep 필수
    body = login.create_driver.driver.find_element(by=By.CSS_SELECTOR, value='body')
    body.send_keys(Keys.SPACE)
    time.sleep(1)

    element.ClickByXPath('/html/body/div[1]/div[3]/div[2]/div[1]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td/button', '161-1')
    element.ClickByXPath('/html/body/div[1]/div[5]/div[1]/div/div/div[2]/div[2]/button[1]', '161-2')


# 쇼핑몰 수정 > 회원인증 설정 > 사용여부 (TC_162)
def memberAuth():
    element.ClickByNameIndex('orderConfig_member_authentication', 0, '162-1')
    element.ClickByNameIndex('orderConfig_member_authentication', 1, '162-2')
    alert = login.create_driver.driver.switch_to.alert
    alert.accept()


# 쇼핑몰 수정 > 회원인증 설정 > 인증시점 (TC_163)
def authTime():
    # 회원인증 설정 > 사용여부 ㅇ사용함으로 설정
    login.create_driver.driver.find_elements(by=By.NAME, value='orderConfig_member_authentication')[0].click()

    element.ClickByNameIndex('mallJoinConfig.authenticationTimeType', 0, '163-1')
    element.ClickByNameIndex('mallJoinConfig.authenticationTimeType', 1, '163-2')


# 쇼핑몰 수정 > 회원인증 설정 > 인증종류 (TC_164)
def authType():
    # 회원인증 설정 > 사용여부 ㅇ사용함으로 설정
    login.create_driver.driver.find_elements(by=By.NAME, value='orderConfig_member_authentication')[0].click()

    element.ClickByNameIndex('memberAuthenticationType', 0, '164-1')
    # element.ClickByNameIndex('memberAuthenticationType', 1, '164-2')  # SMS인증은 설정을 따로 해야함
    # element.ClickByNameIndex('memberAuthenticationType', 2, '164-3')  # SMS인증은 설정을 따로 해야함


# 쇼핑몰 수정 > 주문 설정 > 취소/반품/교환 신청 기능 (TC_168)
def customerClaim():
    # page down sleep 필수
    body = login.create_driver.driver.find_element(by=By.CSS_SELECTOR, value='body')
    body.send_keys(Keys.SPACE)
    time.sleep(1)

    element.ClickByNameIndex('orderConfig_customer_cancel', 1, '168-1')
    element.ClickByNameIndex('orderConfig_customer_cancel', 0, '168-2')


# 쇼핑몰 수정 > 장바구니 설정 > 보관 기간 (TC_170)
def storagePeriod():
    element.ClickByNameIndex('cartConfig.storagePeriodNoLimit', 0, '170-1')
    element.ClickByNameIndex('cartConfig.storagePeriodNoLimit', 1, '170-2')


# 쇼핑몰 수정 > 장바구니 설정 > 보관 기간 날짜 드롭박스(TC_171)
def storagePeriodSelect():
    # 보관 기간 ㅇ최대 [7일]드롭박스 일까지 보관 가능 라디오버튼 선택
    element.ClickByNameIndex('cartConfig.storagePeriodNoLimit', 1, '171-1')

    try:
        select = Select(
            login.create_driver.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/div[2]/div[1]'
                                                                       '/div[4]/div[2]/div[2]/table/tbody/tr[1]'
                                                                       '/td/label[2]/select'))
        select.select_by_index(random.randrange(0, 30))
        time.sleep(1)
        print("TC " + '171-2' + " PASS")
        return True
    except Exception as e:
        print(e)
        print("TC " + '171-2' + " Fail")
        return False


# 쇼핑몰 수정 > 장바구니 설정 > 보관 수량 (TC_172)
def storageQuantity():

    try:
        select = Select(
            login.create_driver.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/div[2]/div[1]'
                                                                       '/div[4]/div[2]/div[2]/table/tbody/tr[2]'
                                                                       '/td/select'))
        select.select_by_index(random.choice([0, 1, 2, 3, 4, 5]))
        time.sleep(1)
        print("TC " + '172' + " PASS")
        return True
    except Exception as e:
        print(e)
        print("TC " + '172' + " Fail")
        return False


# 설정 > 쇼핑몰 수정 > 저장 버튼(TC_173)
def save():
    try:
        savebutton = login.create_driver.driver.find_element(By.XPATH,
                                                             value='/html/body/div[1]/div[4]/div/div[2]/button')
        login.create_driver.driver.execute_script("arguments[0].click();", savebutton)
        time.sleep(1)
        WebDriverWait(login.create_driver.driver, 3).until(EC.alert_is_present())
        alert = login.create_driver.driver.switch_to.alert
        alert.accept()
        print("TC " + '173' + " PASS")
        return True
    except Exception as e:
        print(e)
        print("TC " + '173' + " Fail")
        return False


# 설정 > 쇼핑몰관리 > 쇼핑몰 등록/수정 이외의 부분(TC_139,140)
def mallManage():

    # 내부 class 스크롤
    mallList = login.create_driver.driver.find_element(by=By.CLASS_NAME,
                                                     value='tui-grid-body-area')
    login.create_driver.driver.execute_script("arguments[0].scrollBy(0,470)", mallList)

    # PC웹 클릭
    element.ClickByXPath('//*[@id="mall-list-grid"]/div/div/div/div[2]/div/div/'
                         'div[1]/div[2]/div[2]/div/div[1]/table/tbody/tr/td[2]/div', '139')

    # 현재 탭을 1번 탭으로 변경 후 해당 탭 닫기
    login.create_driver.driver.switch_to.window(login.create_driver.driver.window_handles[1])
    login.create_driver.driver.close()
    # 다시 현재 탭 0번 탭으로 변경
    login.create_driver.driver.switch_to.window(login.create_driver.driver.window_handles[0])

    element.ClickByXPath('//*[@id="mall-list-grid"]/div/div/div/div[2]/div/div/'
                         'div[1]/div[2]/div[2]/div/div[1]/table/tbody/tr/td[3]/div/a', '140')

    # 현재 탭을 1번 탭으로 변경 후 해당 탭 닫기
    login.create_driver.driver.switch_to.window(login.create_driver.driver.window_handles[1])
    login.create_driver.driver.close()
    # 다시 현재 탭 0번 탭으로 변경
    login.create_driver.driver.switch_to.window(login.create_driver.driver.window_handles[0])



# 설정 > 기본정책 > 쇼핑몰관리
# 신규 쇼핑몰 등록(TC 120~121)
# def addMall() :
#
#     # 쇼핑몰 관리 접속
#     option.mallManagement()
#     try:
#     # 신규 쇼핑몰 등록 버튼 클릭
#         addMall = libs.create_driver.driver.find_element(by=By.XPATH,
#                                                         value='//*[@id="mall-list-grid"]/div/div/div/div[1]/div/button')
#         addMall.click()
#         WebDriverWait(libs.create_driver.driver, 3).until(EC.alert_is_present())
#         alert = libs.create_driver.driver.switch_to.alert
#         print(alert.text)
#         alert.accept()
#     except:
#         print('신규 쇼핑몰 등록 버튼 클릭 시 alert 미출력됨')

# 쇼핑몰 수정(TC 141~
# def editMall():
#
#     # 내부 class 스크롤
#     mallList = libs.create_driver.driver.find_element(by=By.CLASS_NAME,
#                                                      value='tui-grid-body-area')
#     libs.create_driver.driver.execute_script("arguments[0].scrollBy(0,470)", mallList)
#
#     # 쇼핑몰명 클릭
#     try:
#         mallName = libs.create_driver.driver.find_element(by=By.LINK_TEXT,
#                                                          value='autoqa01')
#         mallName.click()
#         WebDriverWait(libs.create_driver.driver, 3).until(EC.alert_is_present())
#         alert = libs.create_driver.driver.switch_to.alert
#         print(alert.text)
#         alert.accept()
#     except:
#         print('쇼핑몰명 클릭 시 alert 미출력됨')
#
#     WebDriverWait(libs.create_driver.driver, 10).until(EC.presence_of_element_located((By.NAME, 'mall.mallName')))
#
#     # 쇼핑몰 기본정보 > 쇼핑몰명
#     name = libs.create_driver.driver.find_element(by=By.NAME, value='mall.mallName')
#     name.clear()
#     name.send_keys('autoqa' + str(randomNumI))
#
#     # 쇼핑몰 기본정보 > 고객센터 전화번호
#     number = libs.create_driver.driver.find_element(by=By.NAME, value='mall.serviceCenter.phoneNo')
#     number.clear()
#     number.send_keys('0100000' + str(randomNumI))
#
#     # 쇼핑몰 기본정보 > 고객센터 이메일
#     email1 = libs.create_driver.driver.find_elements(by=By.NAME, value='representative.email')[0]
#     email1.clear()
#     email1.send_keys('dlquddnr' + str(randomNumT))
#
#     email2 = libs.create_driver.driver.find_elements(by=By.NAME, value='representative.email')[1]
#     email2.clear()
#     email2.send_keys('naver.com' + str(randomNumT))
#
#     # 쇼핑몰 접속설정 > 인트로페이지(PC)
#     intro_PC_none = libs.create_driver.driver.find_elements(by=By.NAME, value='introPage_PC')[0]
#     intro_PC_none.click()
#
#     intro_PC_no_access = libs.create_driver.driver.find_elements(by=By.NAME, value='introPage_PC')[1]
#     intro_PC_no_access.click()
#
#     intro_PC_member = libs.create_driver.driver.find_elements(by=By.NAME, value='introPage_PC')[2]
#     intro_PC_member.click()
#
#     # intro_PC_adult = login.create_driver.driver.find_elements(by=By.NAME,value='introPage_PC')[3] # 성인인증은 휴대폰 인증 등록되어 있어야만 가능
#     # intro_PC_adult.click()
#
#     # 쇼핑몰 접속설정 > 인트로페이지(MO)
#     intro_MO_none = libs.create_driver.driver.find_elements(by=By.NAME, value='introPage_Mobile')[0]
#     intro_MO_none.click()
#
#     intro_MO_no_access = libs.create_driver.driver.find_elements(by=By.NAME, value='introPage_Mobile')[1]
#     intro_MO_no_access.click()
#
#     intro_MO_member = libs.create_driver.driver.find_elements(by=By.NAME, value='introPage_Mobile')[2]
#     intro_MO_member.click()
#
#     intro_MO_adult = libs.create_driver.driver.find_elements(by=By.NAME, value='introPage_Mobile')[3]
#     intro_MO_adult.click()
#
#     # 쇼핑몰 접속설정 > 도메인
#     try:
#         domain = login.create_driver.driver.find_element(by=By.XPATH,
#                                                          value='/html/body/div/div[3]/div[2]/div[1]/div[1]/'
#                                                                'div[2]/div[2]/table/tbody/tr[2]/th/div/button')
#         domain.click()
#         WebDriverWait(login.create_driver.driver, 3).until(EC.alert_is_present())
#         alert = login.create_driver.driver.switch_to.alert
#         print(alert.text)
#         alert.accept()
#     except:
#         print('도메인 연결 클릭 시 alert 미출력됨')
#
#     time.sleep(1)
#
#     login.create_driver.driver.switch_to.window(login.create_driver.driver.window_handles[1])
#     login.create_driver.driver.close()
#     login.create_driver.driver.switch_to.window(login.create_driver.driver.window_handles[0])
#
#     try:
#         domain_PC = login.create_driver.driver.find_element(by=By.XPATH,
#                                                             value='/html/body/div/div[3]/div[2]/div[1]/div[1]/'
#                                                                   'div[2]/div[2]/table/tbody/tr[2]/td/table/'
#                                                                   'tbody/tr[1]/td/div/a')
#         domain_PC.click()
#         WebDriverWait(login.create_driver.driver, 3).until(EC.alert_is_present())
#         alert = login.create_driver.driver.switch_to.alert
#         print(alert.text)
#         alert.accept()
#     except:
#         print('PC웹 클릭 시 alert 미출력됨')
#
#     time.sleep(1)
#
#     login.create_driver.driver.switch_to.window(login.create_driver.driver.window_handles[1])
#     login.create_driver.driver.close()
#     login.create_driver.driver.switch_to.window(login.create_driver.driver.window_handles[0])
#
#     try:
#         domain_MO = login.create_driver.driver.find_element(by=By.XPATH,
#                                                             value='/html/body/div/div[3]/div[2]/div[1]/div[1]/'
#                                                                   'div[2]/div[2]/table/tbody/tr[2]/td/table/'
#                                                                   'tbody/tr[2]/td/div/a')
#         domain_MO.click()
#         WebDriverWait(login.create_driver.driver, 3).until(EC.alert_is_present())
#         alert = login.create_driver.driver.switch_to.alert
#         print(alert.text)
#         alert.accept()
#     except:
#         print('모바일웹 클릭 시 alert 미출력됨')
#
#     time.sleep(1)
#
#     login.create_driver.driver.switch_to.window(login.create_driver.driver.window_handles[1])
#     login.create_driver.driver.close()
#     login.create_driver.driver.switch_to.window(login.create_driver.driver.window_handles[0])
#
#
#     # 결제수단 노출설정 > 일반결제
#     # page down sleep 필수
#     body = libs.create_driver.driver.find_element(by=By.CSS_SELECTOR, value='body')
#     body.send_keys(Keys.SPACE)
#     time.sleep(1)
#
#     # 무통장입금 사용안함
#     account_no = libs.create_driver.driver.find_elements(by=By.NAME, value='orderConfig_account')[1]
#     account_no.click()
#
#     # 무통장입금 사용함
#     account_yes = libs.create_driver.driver.find_elements(by=By.NAME, value='orderConfig_account')[0]
#     account_yes.click()
#
#
#
# # 쇼핑몰 등록/수정 이외의 부분(TC 139,140)
# def mallMange() :
#
#     # 쇼핑몰 관리 접속
#     option.mallManagement()
#
#     # 내부 class 스크롤
#     mallList = libs.create_driver.driver.find_element(by=By.CLASS_NAME,
#                                                      value='tui-grid-body-area')
#     libs.create_driver.driver.execute_script("arguments[0].scrollBy(0,470)", mallList)
#
#     # PC웹 클릭
#     try:
#         _PCWeb = libs.create_driver.driver.find_element(by=By.XPATH,
#                                                        value='//*[@id="mall-list-grid"]/div/div/div/div[2]/div'
#                                                    '/div/div[1]/div[2]/div[2]/div/div[1]/table/tbody/tr/td[2]/div')
#         _PCWeb.click()
#         WebDriverWait(libs.create_driver.driver, 3).until(EC.alert_is_present())
#         alert = libs.create_driver.driver.switch_to.alert
#         print(alert.text)
#         alert.accept()
#     except:
#         print('PC웹 클릭 시 alert 미출력됨')
#
#     time.sleep(1)  # PC웹 출력되고 1초 대기
#
#     # 현재 탭을 1번 탭으로 변경 후 해당 탭 닫기
#     libs.create_driver.driver.switch_to.window(libs.create_driver.driver.window_handles[1])
#     libs.create_driver.driver.close()
#
#     # 다시 현재 탭 0번 탭으로 변경
#     libs.create_driver.driver.switch_to.window(libs.create_driver.driver.window_handles[0])
#
#     # 모바일웹 클릭
#     try:
#         _MobileWeb = libs.create_driver.driver.find_element(by=By.XPATH,
#                                                            value='//*[@id="mall-list-grid"]/div/div/div/div[2]/div/'
#                                                 'div/div[1]/div[2]/div[2]/div/div[1]/table/tbody/tr/td[3]/div/a')
#         _MobileWeb.click()
#         WebDriverWait(libs.create_driver.driver, 3).until(EC.alert_is_present())
#         alert = libs.create_driver.driver.switch_to.alert
#         print(alert.text)
#         alert.accept()
#     except:
#         print('모바일웹 클릭 시 alert 미출력됨')
#
#     # 현재 탭을 1번 탭으로 변경 후 해당 탭 닫기
#     libs.create_driver.driver.switch_to.window(libs.create_driver.driver.window_handles[1])
#     libs.create_driver.driver.close()
#
#     # 다시 현재 탭 0번 탭으로 변경
#     libs.create_driver.driver.switch_to.window(libs.create_driver.driver.window_handles[0])





