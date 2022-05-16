from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # 로딩될 때까지 대기
from selenium.webdriver.support import expected_conditions as EC  # 로딩될 때까지 대기
from pages.setting import option
import time, random
from selenium.webdriver.common.keys import Keys
from lib import login, element
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains


# 설정 > 기본정책 > 외부서비스 설정 진입
def accessExternal():
    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located \
                                                            ((By.CSS_SELECTOR,
                                                              'body > div > div.header-wrap > div.gnb-wrap > div.left-wrap > ul > li.on > a')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="설정").click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located \
                                                            ((By.LINK_TEXT, '기본정책')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="기본정책").click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located \
                                                            ((By.LINK_TEXT, '외부서비스 설정')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="외부서비스 설정").click()


# 설정 > 외부서비스 설정 > 쇼핑몰 탭(TC_231)
def choiceMall():
    element.ClickByXPath('/html/body/div[1]/div[3]/div[1]/div[2]/div/div/div[1]/div/div/div/div[2]/div/div/a', '231')


# 외부서비스 설정 > 구글통계 (TC_232,233)
def google():
    # 내용입력
    element.InputByName('googleAppKey', 'test' + str(element.randomNumT), '232')

    # 구글 애널리틱스 바로가기 클릭
    element.ClickByLINKTEXT('구글 애널리틱스 바로가기', '233')
    time.sleep(2)

    # 새로 출력된 탭 닫기
    login.create_driver.driver.switch_to.window(login.create_driver.driver.window_handles[1])
    login.create_driver.driver.close()
    login.create_driver.driver.switch_to.window(login.create_driver.driver.window_handles[0])


# 외부서비스 설정 > 네이버 웹마스터 (TC_234,235)
def naver():
    # 내용입력
    element.InputByName('naverAppKey', 'test' + str(element.randomNumT), '234')

    # 네이버 웹마스터 바로가기 클릭
    element.ClickByLINKTEXT('네이버 웹마스터 바로가기', '235')
    time.sleep(2)

    # 새로 출력된 탭 닫기
    login.create_driver.driver.switch_to.window(login.create_driver.driver.window_handles[1])
    login.create_driver.driver.close()
    login.create_driver.driver.switch_to.window(login.create_driver.driver.window_handles[0])


# 외부서비스 설정 > 카카오맵 (TC_236~239)
def kakao():
    # 스크롤 내리기
    login.create_driver.driver.find_element(By.NAME,value='PAYCO.id').send_keys('')

    # 내용입력
    element.InputByName('kakaoAppKey', 'test' + str(element.randomNumT), '236')

    # 카카오 개발자 센터 바로가기 클릭
    element.ClickByLINKTEXT('카카오 개발자 센터 바로가기', '237')
    time.sleep(2)

    # 새로 출력된 탭 닫기
    login.create_driver.driver.switch_to.window(login.create_driver.driver.window_handles[1])
    login.create_driver.driver.close()
    login.create_driver.driver.switch_to.window(login.create_driver.driver.window_handles[0])

    # 내용입력
    element.InputByName('latitude', '123' + str(element.randomNumI), '238-1')
    element.InputByName('longitude', '456' + str(element.randomNumI), '238-2')

    # 위도/경도 찾기 클릭
    element.ClickByLINKTEXT('위도 / 경도 찾기', '239')
    time.sleep(2)

    # 새로 출력된 탭 닫기
    login.create_driver.driver.switch_to.window(login.create_driver.driver.window_handles[1])
    login.create_driver.driver.close()
    login.create_driver.driver.switch_to.window(login.create_driver.driver.window_handles[0])


# 외부서비스 설정 > 인스타그램 (TC_240)
def instagram():
    # 스크롤 내리기
    body = login.create_driver.driver.find_element(by=By.CSS_SELECTOR, value='body')
    body.send_keys(Keys.SPACE)
    time.sleep(2)

    # 인스타그램 연동 클릭
    element.ClickByXPath('/html/body/div[1]/div[3]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr/td/button', '240')
    time.sleep(2)

    # 새로 출력된 탭 닫기
    login.create_driver.driver.switch_to.window(login.create_driver.driver.window_handles[1])
    login.create_driver.driver.close()
    login.create_driver.driver.switch_to.window(login.create_driver.driver.window_handles[0])


# 외부서비스 설정 > 간편로그인 (TC_241~248)
def easyLogin():
    # 페이코 내용입력
    element.InputByName('PAYCO.id', '3RDj49g3K2S8Ru3oOsFB', '241-1')
    element.InputByName('PAYCO.secret', 'FlWZ6CbzOiSkuzOynKPGMUfk', '241-2')

    # 페이코 개발자 센터 클릭
    element.ClickByLINKTEXT('페이코 개발자 센터', '242')
    time.sleep(2)

    # 새로 출력된 탭 닫기
    login.create_driver.driver.switch_to.window(login.create_driver.driver.window_handles[1])
    login.create_driver.driver.close()
    login.create_driver.driver.switch_to.window(login.create_driver.driver.window_handles[0])


    # 네이버 내용입력
    element.InputByName('NAVER.id', 'fE4npmCX5GRBX3YNbuYm', '243-1')
    element.InputByName('NAVER.secret', 'BxXlG3O5JH', '243-2')

    # 네이버 개발자 센터 클릭
    element.ClickByLINKTEXT('네이버 개발자 센터', '244')
    time.sleep(2)

    # 새로 출력된 탭 닫기
    login.create_driver.driver.switch_to.window(login.create_driver.driver.window_handles[1])
    login.create_driver.driver.close()
    login.create_driver.driver.switch_to.window(login.create_driver.driver.window_handles[0])


    # 카카오 내용입력
    element.InputByName('KAKAO.id', '784e707db546d9e6b46395a7258a3894', '245-1')
    element.InputByName('KAKAO.secret', 'tWEdKWgsMoMWIK7EPhpuDeWHtZrFhpfW', '245-2')

    # 카카오 개발자 센터 클릭
    element.ClickByLINKTEXT('카카오 개발자 센터', '246')
    time.sleep(2)

    # 새로 출력된 탭 닫기
    login.create_driver.driver.switch_to.window(login.create_driver.driver.window_handles[1])
    login.create_driver.driver.close()
    login.create_driver.driver.switch_to.window(login.create_driver.driver.window_handles[0])


    # 페이스북 내용입력
    element.InputByName('FACEBOOK.id', '928973311110482', '247-1')
    element.InputByName('FACEBOOK.secret', '65103b9729aa3dfd43aa641dc09ea644', '247-2')

    # 페이스북 개발자 센터 클릭
    element.ClickByLINKTEXT('페이스북 개발자 센터', '248')
    time.sleep(2)

    # 새로 출력된 탭 닫기
    login.create_driver.driver.switch_to.window(login.create_driver.driver.window_handles[1])
    login.create_driver.driver.close()
    login.create_driver.driver.switch_to.window(login.create_driver.driver.window_handles[0])


# 외부서비스 설정 > 외부 스크립트 (TC_249)
def externalScript():
    # 사용여부
    element.ClickByNameIndex('radio-external-script', 0, '249-1')
    element.ClickByNameIndex('radio-external-script', 1, '249-2')


# 외부서비스 설정 > 저장 (TC_263)
def save():
    try:
        savebutton = login.create_driver.driver.find_element(By.XPATH,
                                                             value='/html/body/div[1]/div[4]/div/div[2]/button')
        login.create_driver.driver.execute_script("arguments[0].click();", savebutton)
        time.sleep(1)
        WebDriverWait(login.create_driver.driver, 3).until(EC.alert_is_present())
        alert = login.create_driver.driver.switch_to.alert
        alert.accept()
        print("TC " + '263' + " PASS")
        return True
    except Exception as e:
        print(e)
        print("TC " + '263' + " Fail")
        return False