from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait   # 로딩될 때까지 대기
from selenium.webdriver.support import expected_conditions as EC # 로딩될 때까지 대기
import time
from pages.setting import option
import random
from lib import element
from lib import login

BI = '/html/body/div/div[3]/div[2]/div[1]/div[1]/div[2]/table/tbody/'
MI = '/html/body/div/div[3]/div[2]/div[1]/div[2]/div[2]/table/tbody/'


# 설정 > 기본정보
def accessBI():
    # 설정 > 기본정책 > 기본정보 접속
    WebDriverWait(login.create_driver.driver, 10).until\
        (EC.presence_of_element_located ((By.CSS_SELECTOR,'body > div > div.header-wrap > div.gnb-wrap > '
                                                          'div.left-wrap > ul > li.on > a')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="설정").click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located \
                                                            ((By.LINK_TEXT, '기본정책')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="기본정책").click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located \
                                                            ((By.LINK_TEXT, '기본정보')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="기본정보").click()


# 설정 > 기본정보 > 회사명(TC_98)
def companyName():
    element.InputByXPath(BI + 'tr[1]/td[1]/div/div/input', '테스트' + str(element.randomNumT), '98')


# 설정 > 기본정보 > 대표자명(TC_99)
def representativeName():
    element.InputByXPath(BI + 'tr[1]/td[2]/div/div/input', '테스트' + str(element.randomNumT), '99')


# 설정 > 기본정보 > 사업자등록번호(TC_100)
def companyRegistrationNumber():
    element.InputByXPath(BI + 'tr[2]/td/div/div/input', '000000' + str(element.randomNumI), '100')


# 설정 > 기본정보 > 대표전화번호(TC_101)
def representativeNumber():
    element.InputByXPath(BI + 'tr[3]/td[1]/div/div/input', '01000000000', '101')


# 설정 > 기본정보 > 통신판매업 신고번호(TC_102)
def telemarketingNumber():
    element.InputByXPath(BI + 'tr[3]/td[2]/div/div/input', '0101111' + str(element.randomNumI), '102')


# 설정 > 기본정보 > 대표이메일(TC_103~104)
def representativeEmail():
    element.InputByXPath(BI + 'tr[4]/td[1]/div/div[1]/div/input', 'byungwook.lee'+ str(element.randomNumT), '103')
    element.InputByXPath(BI + 'tr[4]/td[1]/div/div[2]/div/input', 'nhnsoft.com'+ str(element.randomNumT), '104')


# 설정 > 기본정보 > 팩스번호(TC_105)
def faxNumber():
    element.InputByXPath(BI + 'tr[4]/td[2]/div/div/input', '0101111' + str(element.randomNumI), '105')


# 설정 > 기본정보 > 업종(TC_106)
def businessType():
    element.InputByXPath(BI + 'tr[5]/td[1]/div/div/input', '업종 의류' + str(element.randomNumT), '106')


# 설정 > 기본정보 > 업태(TC_107)
def businessConditions():
    element.InputByXPath(BI + 'tr[5]/td[2]/div/div/input', '업태 의류' + str(element.randomNumT), '107')


# 설정 > 기본정보 > 사업장 주소(TC_108~112)
def businessAddress():
    element.ClickByXPath(BI + 'tr[6]/td/div[1]/button', '108')

    login.create_driver.driver.find_element(by=By.XPATH,
                                          value='//*[@id="searchForm"]/table/tbody'
                                                '/tr/td[1]/div/div/div/input').send_keys('판교')
    element.ClickByXPath('//*[@id="searchForm"]/table/tbody/tr/td[2]/div/button', '109')

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located \
                                        ((By.XPATH, '/html/body/div/div[5]/div[1]/div/div/div[2]/div[2]/ul/li[1]/button')))
    element.ClickByXPath('/html/body/div/div[5]/div[1]/div/div/div[2]/div[2]/ul/li[1]/button', '110')

    element.InputByXPath(BI + 'tr[6]/td/div[2]/div[2]/div/input', '123333' + str(element.randomNumI), '111')
    element.InputByXPath(BI + 'tr[6]/td/div[3]/div[2]/div/input', '456666' + str(element.randomNumI), '112')


# 설정 > 기본정보 > 보호책임자 이름(TC_113)
def managerName():

    # 가장 하단으로 스크롤
    login.create_driver.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    element.InputByXPath(MI + 'tr[1]/td[1]/div/div/input', '책임자 이름' + str(element.randomNumT), '113')


# 설정 > 기본정보 > 보호책임자 전화번호(TC_114)
def managerNumber():
    element.InputByXPath(MI + 'tr[1]/td[2]/div/div/input', '0101111' + str(element.randomNumI), '114')


# 설정 > 기본정보 > 보호책임자 전화번호(TC_115~116)
def managerInfo():
    element.InputByXPath(MI + 'tr[2]/td/div[1]/div/input', '소속' + str(element.randomNumT), '115')
    element.InputByXPath(MI + 'tr[2]/td/div[2]/div/input', '직위' + str(element.randomNumT), '116')


# 설정 > 기본정보 > 보호책임자 이메일(TC_117~118)
def managerEmail():
    element.InputByXPath(MI + 'tr[3]/td/div/div[1]/div/input', 'byungwook.lee' + str(element.randomNumT), '117')
    element.InputByXPath(MI + 'tr[3]/td/div/div[2]/div/input', 'nhnsoft.com' + str(element.randomNumT), '118')


# 설정 > 기본정보 > 저장 버튼(TC_119)
def save():
    try:
        savebutton = login.create_driver.driver.find_element(By.XPATH, value='/html/body/div/div[4]/div/div[2]/button')
        login.create_driver.driver.execute_script("arguments[0].click();", savebutton)
        time.sleep(1)
        WebDriverWait(login.create_driver.driver, 3).until(EC.alert_is_present())
        alert = login.create_driver.driver.switch_to.alert
        alert.accept()
        print("TC " + '119' + " PASS")
        return True
    except Exception as e:
        print(e)
        print("TC " + '119' + " Fail")
        return False


# # 설정 > 기본정책 > 기본정보(TC 101~120)
# def inputBI() :
#
#
#
#
#
#     # # 기본정보 > 회사명
#     # companyName = login.create_driver.driver.find_element(by=By.XPATH,
#     #                                                     value= BI + 'tr[1]/td[1]/div/div/input')
#     # companyName.clear() # input box 내용 지우기
#     # companyName.send_keys('테스트' + str(randomNumT))  # input box 내용 입력
#     #
#     # # 기본정보 > 대표자명
#     # representativeName = login.create_driver.driver.find_element(by=By.XPATH,
#     #                                                            value= BI + 'tr[1]/td[2]/div/div/input')
#     # representativeName.clear()
#     # representativeName.send_keys('테스트' + str(randomNumT))
#     #
#     # # 기본정보 > 사업자등록번호
#     # companyRegistrationNumber = login.create_driver.driver.find_element(by=By.XPATH,
#     #                                                                   value= BI + 'tr[2]/td/div/div/input')
#     # companyRegistrationNumber.clear()
#     # companyRegistrationNumber.send_keys('000000'+ str(randomNumI))
#
#     # # 기본정보 > 대표전화번호
#     # representativePhoneNumber = login.create_driver.driver.find_element(by=By.XPATH,
#     #                                                                   value= BI + 'tr[3]/td[1]/div/div/input')
#     # representativePhoneNumber.clear()
#     # representativePhoneNumber.send_keys('01000000000')
#
#     # # 기본정보 > 통신판매업 신고번호
#     # telemarketingNumber = lib.create_driver.driver.find_element(by=By.XPATH,
#     #                                                             value= BI + 'tr[3]/td[2]/div/div/input')
#     # telemarketingNumber.clear()
#     # telemarketingNumber.send_keys('0101111' + str(randomNumI))
#
#     # # 기본정보 > 대표이메일
#     # representativeEmail1 = lib.create_driver.driver.find_element(by=By.XPATH,
#     #                                                              value= BI + 'tr[4]/td[1]/div/div[1]/div/input')
#     # representativeEmail1.clear()
#     # representativeEmail1.send_keys('byungwook.lee'+ str(randomNumT))
#     # representativeEmail2 = login.create_driver.driver.find_element(by=By.XPATH,
#     #                                                              value= BI + 'tr[4]/td[1]/div/div[2]/div/input')
#     # representativeEmail2.clear()
#     # representativeEmail2.send_keys('nhnsoft.com'+ str(randomNumT))
#
#     # # 기본정보 > 팩스번호
#     # faxNumber = login.create_driver.driver.find_element(by=By.XPATH,
#     #                                                   value= BI + 'tr[4]/td[2]/div/div/input')
#     # faxNumber.clear()
#     # faxNumber.send_keys('0101111' + str(randomNumI))
#
#     # # 기본정보 > 업종
#     # businessType = login.create_driver.driver.find_element(by=By.XPATH,
#     #                                                      value= BI + 'tr[5]/td[1]/div/div/input')
#     # businessType.clear()
#     # businessType.send_keys('업종 의류' + str(randomNumT))
#     #
#     # # 기본정보 > 업태
#     # businessConditions = lib.create_driver.driver.find_element(by=By.XPATH,
#     #                                                            value= BI + 'tr[5]/td[2]/div/div/input')
#     # businessConditions.clear()
#     # businessConditions.send_keys('업태 의류' + str(randomNumT))
#
#     # # 기본정보 > 사업장 주소
#     # lib.create_driver.driver.find_element(by=By.XPATH,
#     #                                       value= BI + 'tr[6]/td/div[1]/button').click()
#     # lib.create_driver.driver.find_element(by=By.XPATH,
#     #                                       value='//*[@id="searchForm"]/table/tbody/tr/td[1]/div/div/div/input').send_keys('판교')
#     # lib.create_driver.driver.find_element(by=By.XPATH,
#     #                                       value='//*[@id="searchForm"]/table/tbody/tr/td[2]/div/button').click()
#     #
#     # WebDriverWait(lib.create_driver.driver, 10).until(EC.presence_of_element_located \
#     #                                     ((By.XPATH, '/html/body/div/div[5]/div[1]/div/div/div[2]/div[2]/ul/li[1]/button'))) # 해당 버튼이 출력되지 않는 경우 존재하여 버튼 존재하면 아래 진행되게 함
#     # lib.create_driver.driver.find_element(by=By.XPATH,
#     #                                       value='/html/body/div/div[5]/div[1]/div/div/div[2]/div[2]/ul/li[1]/button').click() # 첫번째로 출력되는 주소 선택
#     # lib.create_driver.driver.find_element(by=By.XPATH,
#     #                                       value= BI + 'tr[6]/td/div[2]/div[2]/div/input').send_keys('123333' + str(randomNumI))
#     # lib.create_driver.driver.find_element(by=By.XPATH,
#     #                                       value= BI + 'tr[6]/td/div[3]/div[2]/div/input').send_keys('456666' + str(randomNumI))
#
#     # # 가장 하단으로 스크롤
#     # lib.create_driver.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
#     #
#     # # 개인정보 > 보호책임자 이름
#     # managerName = lib.create_driver.driver.find_element(by=By.XPATH,
#     #                                                     value= MI + 'tr[1]/td[1]/div/div/input')
#     #
#     # managerName.clear()
#     # managerName.send_keys('책임자 이름' + str(randomNumT))
#
#     # # 개인정보 > 보호책임자 전화번호
#     # managerNumber = lib.create_driver.driver.find_element(by=By.XPATH,
#     #                                                       value= MI + 'tr[1]/td[2]/div/div/input')
#     # managerNumber.clear()
#     # managerNumber.send_keys('0101111' + str(randomNumI))
#
#     # 개인정보 > 보호책임자 소속/직위
#     # managerInfo1 = lib.create_driver.driver.find_element(by=By.XPATH,
#     #                                                      value=MI + 'tr[2]/td/div[1]/div/input')
#     # managerInfo1.clear()
#     # managerInfo1.send_keys('소속' + str(randomNumT))
#     #
#     # managerInfo2 = lib.create_driver.driver.find_element(by=By.XPATH,
#     #                                                      value=MI + 'tr[2]/td/div[2]/div/input')
#     # managerInfo2.clear()
#     # managerInfo2.send_keys('직위' + str(randomNumT))
#     #
#     # # 개인정보 > 보호책임자 이메일
#     # managerEmail1 = lib.create_driver.driver.find_element(by=By.XPATH,
#     #                                                       value=MI + 'tr[3]/td/div/div[1]/div/input')
#     # managerEmail1.clear()
#     # managerEmail1.send_keys('byungwook.lee' + str(randomNumT))
#     #
#     # managerEmail2 = lib.create_driver.driver.find_element(by=By.XPATH,
#     #                                                       value=MI + 'tr[3]/td/div/div[2]/div/input')
#     # managerEmail2.clear()
#     # managerEmail2.send_keys('nhnsoft.com' + str(randomNumT))
#     #
#     # time.sleep(2)
#
#     # 저장 버튼 클릭 시 alert 존재하면 내용 출력 및 확인 버튼 클릭, 없으면 pass 출력
#     try :
#         # 저장버튼 XPATH사용하여 save 변수에 저장
#         save = lib.create_driver.driver.find_element(by=By.XPATH, value='/html/body/div/div[4]/div/div[2]/button')
#
#         # 자바스크립트로 클릭 실행
#         lib.create_driver.driver.execute_script("arguments[0].click();", save)
#
#         WebDriverWait(lib.create_driver.driver, 3).until(EC.alert_is_present())
#         alert = lib.create_driver.driver.switch_to.alert
#         print(alert.text)
#         alert.accept()
#     except :
#         print('pass')