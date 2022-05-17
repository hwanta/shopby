from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait   # 로딩될 때까지 대기
from selenium.webdriver.support import expected_conditions as EC # 로딩될 때까지 대기
from libs import login

# 쇼핑몰 설정 > 기본정책 > 기본정보
def basicInformation() :
    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.CSS_SELECTOR,'body > div > div.header-wrap > div.gnb-wrap > div.left-wrap > ul > li.on > a'))) # 해당 css selector가 출력될 때까지 10초간 대기
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="설정").click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.LINK_TEXT,'기본정책'))) 
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="기본정책").click()
    
    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.LINK_TEXT,'기본정보'))) 
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="기본정보").click()
    
# 쇼핑몰 설정 > 기본정책 > 쇼핑몰관리
def mallManagement() :
    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.CSS_SELECTOR,'body > div > div.header-wrap > div.gnb-wrap > div.left-wrap > ul > li.on > a')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="설정").click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.LINK_TEXT,'기본정책'))) 
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="기본정책").click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.LINK_TEXT,'쇼핑몰관리'))) 
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="쇼핑몰관리").click() # link_text 사용(a태그)

# 설정 > 기본정책 > 약관/개인정보처리방침 관리
def terms() :
    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.CSS_SELECTOR,'body > div > div.header-wrap > div.gnb-wrap > div.left-wrap > ul > li.on > a')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="설정").click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.LINK_TEXT,'기본정책'))) 
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="기본정책").click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.LINK_TEXT,'약관/개인정보처리방침 관리')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="약관/개인정보처리방침 관리").click()
    
# 설정 > 기본정책 > 외부서비스 설정
def externalService() :
    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.CSS_SELECTOR,'body > div > div.header-wrap > div.gnb-wrap > div.left-wrap > ul > li.on > a')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="설정").click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.LINK_TEXT,'기본정책'))) 
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="기본정책").click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.LINK_TEXT,'외부서비스 설정')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="외부서비스 설정").click()

# 설정 > 관리정책 > 운영자 관리
def operatorManagement() :
    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.CSS_SELECTOR,'body > div > div.header-wrap > div.gnb-wrap > div.left-wrap > ul > li.on > a')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="설정").click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.LINK_TEXT,'관리정책'))) 
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="관리정책").click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.LINK_TEXT,'운영자 관리')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="운영자 관리").click()

# 설정 > 관리정책 > 권한 관리
def permissionGroup() :
    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.CSS_SELECTOR,'body > div > div.header-wrap > div.gnb-wrap > div.left-wrap > ul > li.on > a')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="설정").click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.LINK_TEXT,'관리정책'))) 
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="관리정책").click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.LINK_TEXT,'권한그룹 관리')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="권한그룹 관리").click()

# 설정 > 보안정책 > 운영 보안 설정
def operationalSecuritySettings() :
    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.CSS_SELECTOR,'body > div > div.header-wrap > div.gnb-wrap > div.left-wrap > ul > li.on > a')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="설정").click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.LINK_TEXT,'보안정책'))) 
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="보안정책").click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.LINK_TEXT,'운영 보안 설정')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="운영 보안 설정").click()

# 설정 > 보안정책 > 개인정보접속기록 조회
def personalInformationAccess() : 
    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.CSS_SELECTOR,'body > div > div.header-wrap > div.gnb-wrap > div.left-wrap > ul > li.on > a')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="설정").click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.LINK_TEXT,'보안정책'))) 
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="보안정책").click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.LINK_TEXT,'개인정보접속기록 조회')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="개인정보접속기록 조회").click()

# 설정 > 보안정책 > 보안서버 관리
def securityManagementServer() :
    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.CSS_SELECTOR,'body > div > div.header-wrap > div.gnb-wrap > div.left-wrap > ul > li.on > a')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="설정").click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.LINK_TEXT,'보안정책'))) 
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="보안정책").click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.LINK_TEXT,'보안서버 관리')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="보안서버 관리").click()

# 설정 > 배송정책 > 배송비 관리
def shippingCostManagement() :
    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.CSS_SELECTOR,'body > div > div.header-wrap > div.gnb-wrap > div.left-wrap > ul > li.on > a')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="설정").click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.LINK_TEXT,'배송정책'))) 
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="배송정책").click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.LINK_TEXT,'배송비 관리')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="배송비 관리").click()

# 설정 > 결제정책 > 전자 결제(PG) 설정
def pgSettings() :
    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.CSS_SELECTOR,'body > div > div.header-wrap > div.gnb-wrap > div.left-wrap > ul > li.on > a')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="설정").click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.LINK_TEXT,'결제정책'))) 
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="결제정책").click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.LINK_TEXT,'전자 결제(PG) 설정')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="전자 결제(PG) 설정").click()

# 설정 > 결제정책 > 페이코 결제 설정
def paycoPaymentSettings() :
    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.CSS_SELECTOR,'body > div > div.header-wrap > div.gnb-wrap > div.left-wrap > ul > li.on > a')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="설정").click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.LINK_TEXT,'결제정책'))) 
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="결제정책").click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.LINK_TEXT,'페이코 결제 설정')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="페이코 결제 설정").click()

# 설정 > 결제정책 > 네이버페이 설정
def naverPaymentSettings() :
    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.CSS_SELECTOR,'body > div > div.header-wrap > div.gnb-wrap > div.left-wrap > ul > li.on > a')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="설정").click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.LINK_TEXT,'결제정책'))) 
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="결제정책").click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.LINK_TEXT,'네이버페이 설정')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="네이버페이 설정").click()


