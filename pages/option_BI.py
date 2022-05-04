from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait   # 로딩될 때까지 대기
from selenium.webdriver.support import expected_conditions as EC # 로딩될 때까지 대기
import time
from pages import login
from pages.setting import option
from selenium.webdriver import ActionChains

# 설정 > 기본정책 > 기본정보
def inputBI() :

    BI = '/html/body/div/div[3]/div[2]/div[1]/div[1]/div[2]/table/tbody/'
    MI = '/html/body/div/div[3]/div[2]/div[1]/div[2]/div[2]/table/tbody/'

    # 설정 > 기본정책 > 기본정보 접속
    option.basicInformation()

    # 기본정보 > 회사명
    companyName = login.create_driver.driver.find_element(by=By.XPATH,
                              value= BI + 'tr[1]/td[1]/div/div/input')
    companyName.clear() # input box 내용 지우기
    companyName.send_keys('테스트')  # input box 내용 입력

    # 기본정보 > 대표자명

    representativeName = login.create_driver.driver.find_element(by=By.XPATH,
                              value= BI + 'tr[1]/td[2]/div/div/input')
    representativeName.clear()
    representativeName.send_keys('테스트')

    # 기본정보 > 사업자등록번호
    companyRegistrationNumber = login.create_driver.driver.find_element(by=By.XPATH,
                              value= BI + 'tr[2]/td/div/div/input')
    companyRegistrationNumber.clear()
    companyRegistrationNumber.send_keys('0000000000')

    # 기본정보 > 대표전화번호
    representativePhoneNumber = login.create_driver.driver.find_element(by=By.XPATH,
                              value= BI + 'tr[3]/td[1]/div/div/input')
    representativePhoneNumber.clear()
    representativePhoneNumber.send_keys('01011111111')

    # 기본정보 > 통신판매업 신고번호
    telemarketingNumber = login.create_driver.driver.find_element(by=By.XPATH,
                             value= BI + 'tr[3]/td[2]/div/div/input')
    telemarketingNumber.clear()
    telemarketingNumber.send_keys('01011111111')

    # 기본정보 > 대표이메일
    representativeEmail1 = login.create_driver.driver.find_element(by=By.XPATH,
                             value= BI + 'tr[4]/td[1]/div/div[1]/div/input')
    representativeEmail1.clear()
    representativeEmail1.send_keys('byungwook.lee')
    representativeEmail2 = login.create_driver.driver.find_element(by=By.XPATH,
                             value= BI + 'tr[4]/td[1]/div/div[2]/div/input')
    representativeEmail2.clear()
    representativeEmail2.send_keys('nhnsoft.com')

    # 기본정보 > 팩스번호
    faxNumber = login.create_driver.driver.find_element(by=By.XPATH,
                             value= BI + 'tr[4]/td[2]/div/div/input')
    faxNumber.clear()
    faxNumber.send_keys('01011111111')

    # 기본정보 > 업종
    businessType = login.create_driver.driver.find_element(by=By.XPATH,
                             value= BI + 'tr[5]/td[1]/div/div/input')
    businessType.clear()
    businessType.send_keys('업종 의류')

    # 기본정보 > 업태
    businessConditions = login.create_driver.driver.find_element(by=By.XPATH,
                             value= BI + 'tr[5]/td[2]/div/div/input')
    businessConditions.clear()
    businessConditions.send_keys('업태 의류')

    # 기본정보 > 사업장 주소
    login.create_driver.driver.find_element(by=By.XPATH,
                              value= BI + 'tr[6]/td/div[1]/button').click()
    login.create_driver.driver.find_element(by=By.XPATH,
                              value='//*[@id="searchForm"]/table/tbody/tr/td[1]/div/div/div/input').send_keys('판교')
    login.create_driver.driver.find_element(by=By.XPATH,
                              value='//*[@id="searchForm"]/table/tbody/tr/td[2]/div/button').click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located \
                                        ((By.XPATH, '/html/body/div/div[5]/div[1]/div/div/div[2]/div[2]/ul/li[1]/button'))) # 해당 버튼이 출력되지 않는 경우 존재하여 버튼 존재하면 아래 진행되게 함
    login.create_driver.driver.find_element(by=By.XPATH,
                              value='/html/body/div/div[5]/div[1]/div/div/div[2]/div[2]/ul/li[1]/button').click() # 첫번째로 출력되는 주소 선택
    login.create_driver.driver.find_element(by=By.XPATH,
                              value= BI + 'tr[6]/td/div[2]/div[2]/div/input').send_keys('123333')
    login.create_driver.driver.find_element(by=By.XPATH,
                              value= BI + 'tr[6]/td/div[3]/div[2]/div/input').send_keys('456666')

    # 가장 하단으로 스크롤
    login.create_driver.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 개인정보 > 보호책임자 이름
    managerName = login.create_driver.driver.find_element(by=By.XPATH,
                                            value= MI + 'tr[1]/td[1]/div/div/input')

    managerName.clear()
    managerName.send_keys('책임자 이름')

    # 개인정보 > 보호책임자 전화번호
    managerNumber = login.create_driver.driver.find_element(by=By.XPATH,
                                              value= MI + 'tr[1]/td[2]/div/div/input')
    managerNumber.clear()
    managerNumber.send_keys('01011111111')

    # 개인정보 > 보호책임자 소속/직위
    managerInfo1 = login.create_driver.driver.find_element(by=By.XPATH,
                                             value=MI + 'tr[2]/td/div[1]/div/input')
    managerInfo1.clear()
    managerInfo1.send_keys('소속')

    managerInfo2 = login.create_driver.driver.find_element(by=By.XPATH,
                                              value=MI + 'tr[2]/td/div[2]/div/input')
    managerInfo2.clear()
    managerInfo2.send_keys('직위')

    # 개인정보 > 보호책임자 이메일
    managerEmail1 = login.create_driver.driver.find_element(by=By.XPATH,
                                              value=MI + 'tr[3]/td/div/div[1]/div/input')
    managerEmail1.clear()
    managerEmail1.send_keys('byungwook.lee')

    managerEmail2 = login.create_driver.driver.find_element(by=By.XPATH,
                                              value=MI + 'tr[3]/td/div/div[2]/div/input')
    managerEmail2.clear()
    managerEmail2.send_keys('nhnsoft.com')

    time.sleep(2)
    try :
        # [저장] 버튼 클릭
        save = login.create_driver.driver.find_element(by=By.LINK_TEXT,
                                     value='저장')
        action = ActionChains(login.create_driver)
        action.click().perform()

        # alert 존재하면 내용 출력, 없으면 pass 출력
        WebDriverWait(login.create_driver.driver, 3).until(EC.alert_is_present())
        alert = login.create_driver.driver.switch_to.alert
        print(alert.text)
        alert.accept()
    except :
        print('pass')




