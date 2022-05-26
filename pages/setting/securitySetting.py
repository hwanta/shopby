from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # 로딩될 때까지 대기
from selenium.webdriver.support import expected_conditions as EC  # 로딩될 때까지 대기
from pages.setting import option
import time, random
from selenium.webdriver.common.keys import Keys
from libs import login, element
from selenium.webdriver.support.select import Select


# 설정 > 보안정책 > 운영 보안 설정
def accessSecuritySetting() :
    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.CSS_SELECTOR,'body > div > div.header-wrap > div.gnb-wrap > div.left-wrap > ul > li.on > a')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="설정").click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.LINK_TEXT,'보안정책')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="보안정책").click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.LINK_TEXT,'운영 보안 설정')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="운영 보안 설정").click()


# 설정 > 운영 보안 설정 > 관리자 보안인증 설정(TC_334)
def securityAuthentication():
    element.ClickByID('AuthSecurityCheckBox_LOGIN', '334-1')
    element.ClickByID('AuthMethodFromSecurityCheckBox_OTP', '334-2')

    try:
        button = login.create_driver.driver.find_element(By.XPATH,
                                                             value='/html/body/div[1]/div[4]/div/div[2]/button')
        login.create_driver.driver.execute_script("arguments[0].click();", button)
        time.sleep(1)
        WebDriverWait(login.create_driver.driver, 3).until(EC.alert_is_present())
        alert = login.create_driver.driver.switch_to.alert
        alert.accept()
        print("TC " + '334-3' + " PASS")
        return True
    except Exception as e:
        print(e)
        print("TC " + '334-3' + " Fail")
        return False


# 설정 > 운영 보안 설정 > 관리자 보안인증 설정 ㅁ보안로그인 체크해제(TC_335)
def securityAuthentication2():
    element.ClickByID('AuthSecurityCheckBox_LOGIN', '335-1')

    try:
        button = login.create_driver.driver.find_element(By.XPATH,
                                                             value='/html/body/div[1]/div[4]/div/div[2]/button')
        login.create_driver.driver.execute_script("arguments[0].click();", button)
        time.sleep(1)
        WebDriverWait(login.create_driver.driver, 3).until(EC.alert_is_present())
        alert = login.create_driver.driver.switch_to.alert
        alert.accept()
        print("TC " + '335-2' + " PASS")
        return True
    except Exception as e:
        print(e)
        print("TC " + '335-2' + " Fail")
        return False


# 설정 > 운영 보안 설정 > 관리자 IP 접속제한 설정 등록(TC_336)
def accessIPSetting():
    element.ClickByNameIndex('radio-access-restrict', 0, '336-1')
    for index in range(1, 5):
        element.InputByXPath(
            '/html/body/div/div[3]/div[2]/div[1]/div/div[3]/table/tbody/tr[2]/td/div/div/div/div['+ str(index) +']/div/div/input', 111,
            '336-' + str(index + 1))

    element.ClickByXPath('/html/body/div/div[3]/div[2]/div[1]/div/div[3]/table/tbody/tr[2]/td/div/div[1]/div/button', '336-6')
    for index in range(1, 5):
        element.InputByXPath(
            '/html/body/div/div[3]/div[2]/div[1]/div/div[3]/table/tbody/tr[2]/td/div/div[2]/div/div['+ str(index) +']/div/div/input', 111,
            '336-' + str(index + 6))

    try:
        button = login.create_driver.driver.find_element(By.XPATH,
                                                             value='/html/body/div[1]/div[4]/div/div[2]/button')
        login.create_driver.driver.execute_script("arguments[0].click();", button)
        time.sleep(1)
        WebDriverWait(login.create_driver.driver, 3).until(EC.alert_is_present())
        alert = login.create_driver.driver.switch_to.alert
        alert.accept()
        print("TC " + '336-11' + " PASS")
        return True
    except Exception as e:
        print(e)
        print("TC " + '336-11' + " Fail")
        return False


# 설정 > 운영 보안 설정 > 관리자 IP 접속제한 설정 변경(TC_337)
def changeIPSetting():
    element.ClickByNameIndex('radio-access-restrict', 0, '337-1')
    for index in range(1, 5):
        element.InputByXPath(
            '/html/body/div/div[3]/div[2]/div[1]/div/div[3]/table/tbody/tr[2]/td/div/div/div/div['+ str(index) +']/div/div/input', 222,
            '337-' + str(index + 1))

    try:
        button = login.create_driver.driver.find_element(By.XPATH,
                                                             value='/html/body/div[1]/div[4]/div/div[2]/button')
        login.create_driver.driver.execute_script("arguments[0].click();", button)
        time.sleep(1)
        WebDriverWait(login.create_driver.driver, 3).until(EC.alert_is_present())
        alert = login.create_driver.driver.switch_to.alert
        alert.accept()
        print("TC " + '337-6' + " PASS")
        return True
    except Exception as e:
        print(e)
        print("TC " + '337-6' + " Fail")
        return False


# 설정 > 운영 보안 설정 > 관리자 IP 접속제한 설정 사용안함으로 변경(TC_338)
def disableIPSetting():
    element.ClickByNameIndex('radio-access-restrict', 1, '338-1')

    try:
        button = login.create_driver.driver.find_element(By.XPATH,
                                                             value='/html/body/div[1]/div[4]/div/div[2]/button')
        login.create_driver.driver.execute_script("arguments[0].click();", button)
        time.sleep(1)
        WebDriverWait(login.create_driver.driver, 3).until(EC.alert_is_present())
        alert = login.create_driver.driver.switch_to.alert
        alert.accept()
        print("TC " + '338-2' + " PASS")
        return True
    except Exception as e:
        print(e)
        print("TC " + '338-2' + " Fail")
        return False






