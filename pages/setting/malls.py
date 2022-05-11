from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait   # 로딩될 때까지 대기
from selenium.webdriver.support import expected_conditions as EC # 로딩될 때까지 대기
from pages import login
from pages.setting import option
import time,random
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


# 설정 > 기본정책 > 쇼핑몰관리
# 신규 쇼핑몰 등록(TC 120~121)
def addMall() :

    # 쇼핑몰 관리 접속
    option.mallManagement()
    try:
    # 신규 쇼핑몰 등록 버튼 클릭
        addMall = login.create_driver.driver.find_element(by=By.XPATH,
                                            value='//*[@id="mall-list-grid"]/div/div/div/div[1]/div/button')
        addMall.click()
        WebDriverWait(login.create_driver.driver, 3).until(EC.alert_is_present())
        alert = login.create_driver.driver.switch_to.alert
        print(alert.text)
        alert.accept()
    except:
        print('신규 쇼핑몰 등록 버튼 클릭 시 alert 미출력됨')

# 쇼핑몰 수정(TC 141~
def editMall():

    randomNumT = random.randrange(1,1000)
    randomNumI = random.randrange(1000,10000)

    # 쇼핑몰 관리 접속
    option.mallManagement()

    # 내부 class 스크롤
    mallList = login.create_driver.driver.find_element(by=By.CLASS_NAME,
                                                value='tui-grid-body-area')
    login.create_driver.driver.execute_script("arguments[0].scrollBy(0,470)", mallList)

    # 쇼핑몰명 클릭
    try:
        mallName = login.create_driver.driver.find_element(by=By.LINK_TEXT,
                                                value='autoqa01')
        mallName.click()
        WebDriverWait(login.create_driver.driver, 3).until(EC.alert_is_present())
        alert = login.create_driver.driver.switch_to.alert
        print(alert.text)
        alert.accept()
    except:
        print('쇼핑몰명 클릭 시 alert 미출력됨')

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located((By.NAME,'mall.mallName')))

    # 쇼핑몰 기본정보 > 쇼핑몰명
    name = login.create_driver.driver.find_element(by=By.NAME,value='mall.mallName')
    name.clear()
    name.send_keys('autoqa' + str(randomNumI))

    # 쇼핑몰 기본정보 > 고객센터 전화번호
    number = login.create_driver.driver.find_element(by=By.NAME,value='mall.serviceCenter.phoneNo')
    number.clear()
    number.send_keys('0100000' + str(randomNumI))

    # 쇼핑몰 기본정보 > 고객센터 이메일
    email1 = login.create_driver.driver.find_elements(by=By.NAME,value='representative.email')[0]
    email1.clear()
    email1.send_keys('dlquddnr' + str(randomNumT))

    email2 = login.create_driver.driver.find_elements(by=By.NAME,value='representative.email')[1]
    email2.clear()
    email2.send_keys('naver.com' + str(randomNumT))

    # 쇼핑몰 접속설정 > 인트로페이지(PC)
    intro_PC_none = login.create_driver.driver.find_elements(by=By.NAME,value='introPage_PC')[0]
    intro_PC_none.click()

    intro_PC_no_access = login.create_driver.driver.find_elements(by=By.NAME,value='introPage_PC')[1]
    intro_PC_no_access.click()

    intro_PC_member = login.create_driver.driver.find_elements(by=By.NAME,value='introPage_PC')[2]
    intro_PC_member.click()

    # intro_PC_adult = login.create_driver.driver.find_elements(by=By.NAME,value='introPage_PC')[3] # 성인인증은 휴대폰 인증 등록되어 있어야만 가능
    # intro_PC_adult.click()

    # 쇼핑몰 접속설정 > 인트로페이지(MO)
    intro_MO_none = login.create_driver.driver.find_elements(by=By.NAME, value='introPage_Mobile')[0]
    intro_MO_none.click()

    intro_MO_no_access = login.create_driver.driver.find_elements(by=By.NAME, value='introPage_Mobile')[1]
    intro_MO_no_access.click()

    intro_MO_member = login.create_driver.driver.find_elements(by=By.NAME, value='introPage_Mobile')[2]
    intro_MO_member.click()

    intro_MO_adult = login.create_driver.driver.find_elements(by=By.NAME, value='introPage_Mobile')[3]
    intro_MO_adult.click()

    # # 쇼핑몰 접속설정 > 도메인
    # try:
    #     domain = login.create_driver.driver.find_element(by=By.XPATH,
    #                                                      value='/html/body/div/div[3]/div[2]/div[1]/div[1]/'
    #                                                            'div[2]/div[2]/table/tbody/tr[2]/th/div/button')
    #     domain.click()
    #     WebDriverWait(login.create_driver.driver, 3).until(EC.alert_is_present())
    #     alert = login.create_driver.driver.switch_to.alert
    #     print(alert.text)
    #     alert.accept()
    # except:
    #     print('도메인 연결 클릭 시 alert 미출력됨')
    #
    # time.sleep(1)
    #
    # login.create_driver.driver.switch_to.window(login.create_driver.driver.window_handles[1])
    # login.create_driver.driver.close()
    # login.create_driver.driver.switch_to.window(login.create_driver.driver.window_handles[0])
    #
    # try:
    #     domain_PC = login.create_driver.driver.find_element(by=By.XPATH,
    #                                                         value='/html/body/div/div[3]/div[2]/div[1]/div[1]/'
    #                                                               'div[2]/div[2]/table/tbody/tr[2]/td/table/'
    #                                                               'tbody/tr[1]/td/div/a')
    #     domain_PC.click()
    #     WebDriverWait(login.create_driver.driver, 3).until(EC.alert_is_present())
    #     alert = login.create_driver.driver.switch_to.alert
    #     print(alert.text)
    #     alert.accept()
    # except:
    #     print('PC웹 클릭 시 alert 미출력됨')
    #
    # time.sleep(1)
    #
    # login.create_driver.driver.switch_to.window(login.create_driver.driver.window_handles[1])
    # login.create_driver.driver.close()
    # login.create_driver.driver.switch_to.window(login.create_driver.driver.window_handles[0])
    #
    # try:
    #     domain_MO = login.create_driver.driver.find_element(by=By.XPATH,
    #                                                         value='/html/body/div/div[3]/div[2]/div[1]/div[1]/'
    #                                                               'div[2]/div[2]/table/tbody/tr[2]/td/table/'
    #                                                               'tbody/tr[2]/td/div/a')
    #     domain_MO.click()
    #     WebDriverWait(login.create_driver.driver, 3).until(EC.alert_is_present())
    #     alert = login.create_driver.driver.switch_to.alert
    #     print(alert.text)
    #     alert.accept()
    # except:
    #     print('모바일웹 클릭 시 alert 미출력됨')
    #
    # time.sleep(1)
    #
    # login.create_driver.driver.switch_to.window(login.create_driver.driver.window_handles[1])
    # login.create_driver.driver.close()
    # login.create_driver.driver.switch_to.window(login.create_driver.driver.window_handles[0])


    # 결제수단 노출설정 > 일반결제
    # page down sleep 필수
    body = login.create_driver.driver.find_element(by=By.CSS_SELECTOR,value='body')
    body.send_keys(Keys.SPACE)
    time.sleep(1)

    # 무통장입금 사용안함
    account_no = login.create_driver.driver.find_elements(by=By.NAME,value='orderConfig_account')[1]
    account_no.click()

    # 무통장입금 사용함
    account_yes = login.create_driver.driver.find_elements(by=By.NAME, value='orderConfig_account')[0]
    account_yes.click()



# 쇼핑몰 등록/수정 이외의 부분(TC 139,140)
def mallMange() :

    # 쇼핑몰 관리 접속
    option.mallManagement()

    # 내부 class 스크롤
    mallList = login.create_driver.driver.find_element(by=By.CLASS_NAME,
                                                       value='tui-grid-body-area')
    login.create_driver.driver.execute_script("arguments[0].scrollBy(0,470)", mallList)

    # PC웹 클릭
    try:
        _PCWeb = login.create_driver.driver.find_element(by=By.XPATH,
                                             value='//*[@id="mall-list-grid"]/div/div/div/div[2]/div'
                                                   '/div/div[1]/div[2]/div[2]/div/div[1]/table/tbody/tr/td[2]/div')
        _PCWeb.click()
        WebDriverWait(login.create_driver.driver, 3).until(EC.alert_is_present())
        alert = login.create_driver.driver.switch_to.alert
        print(alert.text)
        alert.accept()
    except:
        print('PC웹 클릭 시 alert 미출력됨')

    time.sleep(1)  # PC웹 출력되고 1초 대기

    # 현재 탭을 1번 탭으로 변경 후 해당 탭 닫기
    login.create_driver.driver.switch_to.window(login.create_driver.driver.window_handles[1])
    login.create_driver.driver.close()

    # 다시 현재 탭 0번 탭으로 변경
    login.create_driver.driver.switch_to.window(login.create_driver.driver.window_handles[0])

    # 모바일웹 클릭
    try:
        _MobileWeb = login.create_driver.driver.find_element(by=By.XPATH,
                                          value='//*[@id="mall-list-grid"]/div/div/div/div[2]/div/'
                                                'div/div[1]/div[2]/div[2]/div/div[1]/table/tbody/tr/td[3]/div/a')
        _MobileWeb.click()
        WebDriverWait(login.create_driver.driver, 3).until(EC.alert_is_present())
        alert = login.create_driver.driver.switch_to.alert
        print(alert.text)
        alert.accept()
    except:
        print('모바일웹 클릭 시 alert 미출력됨')

    # 현재 탭을 1번 탭으로 변경 후 해당 탭 닫기
    login.create_driver.driver.switch_to.window(login.create_driver.driver.window_handles[1])
    login.create_driver.driver.close()

    # 다시 현재 탭 0번 탭으로 변경
    login.create_driver.driver.switch_to.window(login.create_driver.driver.window_handles[0])





