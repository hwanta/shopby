from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait   # 로딩될 때까지 대기
from selenium.webdriver.support import expected_conditions as EC # 로딩될 때까지 대기
from pages.setting import option
import time, random
from selenium.webdriver.common.keys import Keys
from lib import login,element
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains


# 설정 > 약관/개인정보처리방침 관리 진입
def accessTerm():
    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.CSS_SELECTOR,'body > div > div.header-wrap > div.gnb-wrap > div.left-wrap > ul > li.on > a')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="설정").click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.LINK_TEXT,'기본정책')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="기본정책").click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.LINK_TEXT,'약관/개인정보처리방침 관리')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="약관/개인정보처리방침 관리").click()

# 설정 > 약관/개인정보처리방침 관리 > 쇼핑몰 탭(TC_174)
def choiceMall():
    element.ClickByXPath('/html/body/div[1]/div[3]/div[1]/div[2]/div/div/div[1]/div/div/div/div[2]/div/div/a','174')


# 설정 > 약관/개인정보처리방침 관리 > 쇼핑몰 탭 좌측 목록 버튼 (TC_175,176)
def clickList():
    # 목록버튼 클릭
    element.ClickByXPath('/html/body/div[1]/div[3]/div[1]/div[2]/div/div/div[1]/button','175')

    # 출력된 쇼핑몰 선택
    element.ClickByXPath('/html/body/div[1]/div[3]/div[1]/div[2]/div/div/div[2]/ul/li[2]/a/span','176')


# 설정 > 약관/개인정보처리방침 관리 > 쇼핑몰/회사소개 탭(TC_177)
def companyIntroduction():
    # 쇼핑몰/회사소개 탭 클릭
    element.ClickByLINKTEXT('쇼핑몰/회사소개','177')


# 쇼핑몰/회사소개 > 사용여부 라디오버튼(TC_178)
def introductionUsed():
    element.ClickByNameIndex('radio-MALL_INTRODUCTION',0,'178-1')
    element.ClickByNameIndex('radio-MALL_INTRODUCTION',1,'178-2')


# 쇼핑몰/회사소개 > 내용(TC_179)
def introductionContent():
    element.InputByXPath('/html/body/div[1]/div[3]/div[2]/div[1]/div/div[2]/div[2]/'
                         'table/tbody/tr[2]/td/div/div[2]/div[3]/div[2]','회사소개 내용입력테스트' + str(element.randomNumT),'179')


# 쇼핑몰/회사소개 > 내용 저장(TC_180)
def introductionSave():
    try:
        savebutton = login.create_driver.driver.find_element(By.XPATH,
                                                             value='/html/body/div[1]/div[4]/div/div[2]/button')
        login.create_driver.driver.execute_script("arguments[0].click();", savebutton)
        time.sleep(1)
        WebDriverWait(login.create_driver.driver, 3).until(EC.alert_is_present())
        alert = login.create_driver.driver.switch_to.alert
        alert.accept()
        print("TC " + '180' + " PASS")
        return True
    except Exception as e:
        print(e)
        print("TC " + '180' + " Fail")
        return False


# 설정 > 약관/개인정보처리방침 관리 > 이용약관 탭(TC_181)
def termsService():
    element.ClickByLINKTEXT('이용약관','181')


# 이용약관 > 날짜(TC_182)
def termsDate():
    element.ClickByID('selectedYmd_calendar', '182-1')

    # 다음달로 이동
    element.ClickByXPath('//*[@id="selectYmdt_layer_calendar"]/div/div/div/div/div[1]/div[1]/button[2]', '182-2')
    element.ClickByXPath('//*[@id="selectYmdt_layer_calendar"]/div/div/div/div/div[2]/table/tbody/tr[2]/td[2]', '182-3')


# 이용약관 > 내용(TC_183)
def termsContent():
    element.InputByXPath('/html/body/div[1]/div[3]/div[2]/div[1]/div/div[2]/div[2]/'
                         'table/tbody/tr[2]/td/div/div[2]/div[3]/div[2]', '이용약관 내용입력테스트' + str(element.randomNumT), '183')


# 이용약관 > 공정거래위원회 로고 사용여부(TC_185)
def termsUsed():
    # page down sleep 필수
    body = login.create_driver.driver.find_element(by=By.CSS_SELECTOR, value='body')
    body.send_keys(Keys.SPACE)
    time.sleep(1)

    element.ClickByNameIndex('radio-useFairLogo', 0, '185-1')
    element.ClickByNameIndex('radio-useFairLogo', 1, '185-2')


# 이용약관 > 내용 저장(TC_186)
def termsSave():
    try:
        savebutton = login.create_driver.driver.find_element(By.XPATH,
                                                             value='/html/body/div[1]/div[4]/div/div[2]/button')
        login.create_driver.driver.execute_script("arguments[0].click();", savebutton)
        time.sleep(1)
        WebDriverWait(login.create_driver.driver, 3).until(EC.alert_is_present())
        alert1 = login.create_driver.driver.switch_to.alert
        alert1.accept()
        WebDriverWait(login.create_driver.driver, 3).until(EC.alert_is_present())
        alert2 = login.create_driver.driver.switch_to.alert
        alert2.accept()
        print("TC " + '186' + " PASS")
        return True
    except Exception as e:
        print(e)
        print("TC " + '186' + " Fail")
        return False


# 설정 > 약관/개인정보처리방침 관리 > 개인정보처리방침 탭(TC_187)
def privacy():
    element.ClickByLINKTEXT('개인정보처리방침','187')


# 개인정보처리방침 > 날짜(TC_188)
def privacyDate():
    element.ClickByID('selectedYmd_calendar', '188-1')

    # 다음달로 이동
    element.ClickByXPath('//*[@id="selectYmdt_layer_calendar"]/div/div/div/div/div[1]/div[1]/button[2]', '188-2')
    element.ClickByXPath('//*[@id="selectYmdt_layer_calendar"]/div/div/div/div/div[2]/table/tbody/tr[2]/td[2]', '188-3')


# 개인정보처리방침 > 내용(TC_189)
def privacyContent():
    element.InputByXPath('/html/body/div[1]/div[3]/div[2]/div[1]/div/div[2]/div[2]'
                         '/table/tbody/tr[2]/td/div/div[2]/div[3]/div[2]', '개인정보처리방침 내용입력테스트' + str(element.randomNumT), '189')


# 개인정보처리방침 > 내용 저장(TC_191)
def privacySave():
    try:
        savebutton = login.create_driver.driver.find_element(By.XPATH,
                                                             value='/html/body/div[1]/div[4]/div/div[2]/button')
        login.create_driver.driver.execute_script("arguments[0].click();", savebutton)
        time.sleep(1)
        WebDriverWait(login.create_driver.driver, 3).until(EC.alert_is_present())
        alert1 = login.create_driver.driver.switch_to.alert
        alert1.accept()
        WebDriverWait(login.create_driver.driver, 3).until(EC.alert_is_present())
        alert2 = login.create_driver.driver.switch_to.alert
        alert2.accept()
        print("TC " + '191' + " PASS")
        return True
    except Exception as e:
        print(e)
        print("TC " + '191' + " Fail")
        return False


# 설정 > 약관/개인정보처리방침 관리 > 개인정보 수집/동의 항목 탭(TC_192)
def personalInfo():
    element.ClickByLINKTEXT('개인정보 수집/동의 항목','192')


# [필수]개인정보 수집/이용 > 내용(TC_193)
def personalInfoContent1():
    element.InputByXPath('/html/body/div[1]/div[3]/div[2]/div[1]/div/div[2]/div[2]/'
                         'table/tbody/tr/td/div/div[2]/div[3]/div[2]', '[필수]개인정보 수집/이용 내용입력테스트' + str(element.randomNumT), '193')


# [선택]개인정보 수집/이용 > 사용여부(TC_195)
def personalInfoUsed2():
    element.ClickByNameIndex('radio-PI_COLLECTION_AND_USE_OPTIONAL', 0, '195-1')
    element.ClickByNameIndex('radio-PI_COLLECTION_AND_USE_OPTIONAL', 1, '195-2')


# [선택]개인정보 수집/이용 > 내용(TC_196)
def personalInfoContent2():
    element.InputByXPath('/html/body/div[1]/div[3]/div[2]/div[1]/div/div[2]/div[3]/'
                         'table/tbody/tr[2]/td/div/div[2]/div[3]/div[2]', '[선택]개인정보 수집/이용 내용입력테스트' + str(element.randomNumT), '196')


# [선택]개인정보 처리/위탁 > 사용여부(TC_198)
def personalInfoUsed3():
    element.ClickByNameIndex('radio-PI_PROCESS_CONSIGNMENT', 0, '198-1')
    element.ClickByNameIndex('radio-PI_PROCESS_CONSIGNMENT', 1, '198-2')


# [선택]개인정보 처리/위탁 > 내용(TC_199)
def personalInfoContent3():
    element.InputByXPath('/html/body/div[1]/div[3]/div[2]/div[1]/div/div[2]/div[4]/'
                         'table/tbody/tr[2]/td/div/div[2]/div[3]/div[2]', '[선택]개인정보 처리/위탁 내용입력테스트' + str(element.randomNumT), '199')


# [선택]개인정보 제 3자 제공 > 사용여부(TC_201)
def personalInfoUsed4():
    element.ClickByNameIndex('radio-PI_THIRD_PARTY_PROVISION', 0, '201-1')
    element.ClickByNameIndex('radio-PI_THIRD_PARTY_PROVISION', 1, '201-2')


# [선택]개인정보 제 3자 제공 > 내용(TC_202)
def personalInfoContent4():
    element.InputByXPath('/html/body/div[1]/div[3]/div[2]/div[1]/div/div[2]/div[5]/'
                         'table/tbody/tr[2]/td/div/div[2]/div[3]/div[2]', '[선택]개인정보 제 3자 제공 내용입력테스트' + str(element.randomNumT), '202')


# [필수]개인정보 수집/이용 > 내용(TC_204)
def personalInfoContent5():
    element.InputByXPath('/html/body/div[1]/div[3]/div[2]/div[1]/div/div[2]/div[6]/'
                         'table/tbody/tr/td/div/div[2]/div[3]/div[2]', '[필수]개인정보 수집/이용 내용입력테스트' + str(element.randomNumT), '204')


# [필수]주문 상품정보 동의 > 내용(TC_206)
def personalInfoContent6():
    element.InputByXPath('/html/body/div[1]/div[3]/div[2]/div[1]/div/div[2]/div[7]/'
                         'table/tbody/tr/td/div/div[2]/div[3]/div[2]', '[필수]주문 상품정보 동의 내용입력테스트' + str(element.randomNumT), '206')


# [선택]통관정보 수집/이용 > 사용여부(TC_208)
def personalInfoUsed7():
    element.ClickByNameIndex('radio-CLEARANCE_INFO_COLLECTION_AND_USE', 0, '208-1')
    element.ClickByNameIndex('radio-CLEARANCE_INFO_COLLECTION_AND_USE', 1, '208-2')


# [선택]통관정보 수집/이용 > 내용(TC_209)
def personalInfoContent7():
    element.InputByXPath('/html/body/div[1]/div[3]/div[2]/div[1]/div/div[2]/div[8]/'
                         'table/tbody/tr[2]/td/div/div[2]/div[3]/div[2]', '[필수]통관정보 수집/이용 내용입력테스트' + str(element.randomNumT), '209')


# [선택]개인정보 국외이전 동의 > 사용여부(TC_211)
def personalInfoUsed8():
    element.ClickByNameIndex('radio-TRANSFER_AGREE', 0, '211-1')
    element.ClickByNameIndex('radio-TRANSFER_AGREE', 1, '211-2')


# [선택]개인정보 국외이전 동의 > 내용(TC_212)
def personalInfoContent8():
    element.InputByXPath('/html/body/div[1]/div[3]/div[2]/div[1]/div/div[2]/div[9]/'
                         'table/tbody/tr[2]/td/div/div[2]/div[3]/div[2]', '[필수]개인정보 국외이전 동의 내용입력테스트' + str(element.randomNumT), '212')


# [필수]개인정보 수집/이용(비회원) > 내용(TC_214)
def personalInfoContent9():
    element.InputByXPath('/html/body/div[1]/div[3]/div[2]/div[1]/div/div[2]/div[10]/'
                         'table/tbody/tr/td/div/div[2]/div[3]/div[2]', '[필수]개인정보 수집/이용(비회원) 내용입력테스트' + str(element.randomNumT), '214')


# 이용약관 > 내용 저장(TC_216)
def personalInfoSave():
    try:
        savebutton = login.create_driver.driver.find_element(By.XPATH,
                                                             value='/html/body/div[1]/div[4]/div/div[2]/button')
        login.create_driver.driver.execute_script("arguments[0].click();", savebutton)
        time.sleep(1)
        WebDriverWait(login.create_driver.driver, 3).until(EC.alert_is_present())
        alert = login.create_driver.driver.switch_to.alert
        alert.accept()
        print("TC " + '216' + " PASS")
        return True
    except Exception as e:
        print(e)
        print("TC " + '216' + " Fail")
        return False


# 설정 > 약관/개인정보처리방침 관리 > 이용/탈퇴안내 탭(TC_217)
def useInfo():
    element.ClickByLINKTEXT('이용/탈퇴안내','217')


# 이용안내 > 사용여부(TC_218)
def useInfoUsed1():
    element.ClickByNameIndex('radio-ACCESS_GUIDE', 0, '218-1')
    element.ClickByNameIndex('radio-ACCESS_GUIDE', 1, '218-2')


# 이용안내 > 내용(TC_219)
def useInfoContent1():
    element.InputByXPath('/html/body/div[1]/div[3]/div[2]/div[1]/div/div[2]/div[2]/'
                         'table/tbody/tr[2]/td/div/div[2]/div[3]/div[2]', '이용안내 내용입력테스트' + str(element.randomNumT), '219')


# 탈퇴안내 > 사용여부(TC_221)
def useInfoUsed2():
    element.ClickByNameIndex('radio-WITHDRAWAL_GUIDE', 0, '221-1')
    element.ClickByNameIndex('radio-WITHDRAWAL_GUIDE', 1, '221-2')


# 탈퇴안내 > 내용(TC_222)
def useInfoContent2():
    element.InputByXPath('/html/body/div[1]/div[3]/div[2]/div[1]/div/div[2]/div[3]/'
                         'table/tbody/tr[2]/td/div/div[2]/div[3]/div[2]', '탈퇴안내 내용입력테스트' + str(element.randomNumT), '222')


# 탈퇴안내 > 내용 저장(TC_223)
def useInfoSave():
    try:
        savebutton = login.create_driver.driver.find_element(By.XPATH,
                                                             value='/html/body/div[1]/div[4]/div/div[2]/button')
        login.create_driver.driver.execute_script("arguments[0].click();", savebutton)
        time.sleep(1)
        WebDriverWait(login.create_driver.driver, 3).until(EC.alert_is_present())
        alert = login.create_driver.driver.switch_to.alert
        alert.accept()
        print("TC " + '223' + " PASS")
        return True
    except Exception as e:
        print(e)
        print("TC " + '223' + " Fail")
        return False




















