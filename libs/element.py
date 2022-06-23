from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager  # import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # 로딩될 때까지 대기
from selenium.webdriver.support import expected_conditions as EC  # 로딩될 때까지 대기
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import time
from libs import login, create_driver
import random

randomNumT = random.randrange(1, 1000)
randomNumI = random.randrange(1000, 10000)


# xpath로 버튼 클릭
def ClickByXPath(element, num):
    '''
    xpath로 버튼 클릭
    :param element: XPath
    :param num: TC_number
    :return:
    '''
    try:
        login.create_driver.driver.find_element(By.XPATH, value=element).click()
        time.sleep(1)
        print("TC " + num + " PASS")
        return True
    except Exception as e:
        print(e)
        print("TC " + num + " Fail")
        return False


# css_selector로 버튼 클릭
def ClickByCSS_Selector(element, num):
    '''
    css_selector로 버튼 클릭
    :param element: css_selector
    :param num: TC_num
    :return:
    '''
    try:
        login.create_driver.driver.find_element(By.CSS_SELECTOR, value=element).click()
        time.sleep(1)
        print("TC " + num + " PASS")
        return True
    except Exception as e:
        print(e)
        print("TC " + num + " Fail")
        return False


# linktext로 버튼 클릭
def ClickByLinkText(element, num):
    '''
    linktext로 버튼 클릭
    :param element: linktext
    :param num: TC_number
    :return:
    '''
    try:
        login.create_driver.driver.find_element(By.LINK_TEXT, value=element).click()
        time.sleep(1)
        print("TC " + num + " PASS")
        return True
    except Exception as e:
        print(e)
        print("TC " + num + " Fail")
        return False


# id로 버튼 클릭
def ClickById(element, num):
    '''
    id로 버튼 클릭
    :param element: ID
    :param num: TC_number
    :return:
    '''

    try:
        login.create_driver.driver.find_element(By.ID, value=element).click()
        time.sleep(1)
        print("TC " + num + " PASS")
        return True
    except Exception as e:
        print(e)
        print("TC " + num + " Fail")
        return False


# name으로 버튼 클릭
def ClickByName(element, num):
    '''
    name으로 버튼 클릭
    :param element: NAME
    :param num: TC_number
    :return:
    '''
    try:
        login.create_driver.driver.find_element(By.NAME, value=element).click()
        time.sleep(1)
        print("TC " + num + " PASS")
        return True
    except Exception as e:
        print(e)
        print("TC " + num + " Fail")
        return False


# Name으로 버튼 클릭(인덱스사용)
def ClickByNameIndex(element, index, num):
    '''
    Name으로 버튼 클릭(인덱스사용)
    :param element: NAME 요소
    :param index: 인덱스
    :param num: TC_number
    :return:
    '''
    try:
        login.create_driver.driver.find_elements(By.NAME, value=element)[int(index)].click()
        time.sleep(1)
        print("TC " + num + " PASS")
        return True
    except Exception as e:
        print(e)
        print("TC " + num + " Fail")
        return False


# classname으로 버튼 클릭
def ClickByClassName(element, num):
    '''
    classname으로 버튼 클릭
    :param element: ClassName
    :param num: TC_number
    :return:
    '''
    try:
        login.create_driver.driver.find_element(By.CLASS_NAME, value=element).click()
        time.sleep(1)
        print("TC " + num + " PASS")
        return True
    except Exception as e:
        print(e)
        print("TC " + num + " Fail")
        return False

# text로 특정 항목 클릭 > .click() 사용
def ClickByText(element, num):
    '''
    text로 특정 항목 클릭
    :param element: Text
    :param num: TC_number
    :return:
    '''
    try:
        text = "//*[contains(text(), '" + element + "')]"
        login.create_driver.driver.find_element(By.XPATH, value=text).click()
        time.sleep(1)
        print("TC " + num + " PASS")
        return True
    except Exception as e:
        print(e)
        print("TC " + num + " Fail")
        return False


# text로 특정 항목 클릭 > .send_keys(Keys.ENTER)
def SendClickByText(element, num):
    '''
    text로 특정 항목 클릭 (.click()이 동작하지 않을 때 대체하여 사용 > 이미지 클릭은 대체불가)
    :param element: Text
    :param num: TC_number
    :return:
    '''
    try:
        text = "//*[contains(text(), '" + element + "')]"
        login.create_driver.driver.find_element(By.XPATH, value=text).send_keys(Keys.ENTER)
        time.sleep(1)
        print("TC " + num + " PASS")
        return True
    except Exception as e:
        print(e)
        print("TC " + num + " Fail")
        return False


# xpath로 inputbox 내용 입력
def InputByXPath(element, input, num):
    '''
    xpath로 inputbox 내용 입력
    :param element: XPath
    :param input: input box 입력 내용
    :param num: TC_number
    :return:
    '''

    try:
        login.create_driver.driver.find_element(By.XPATH, value=element).clear()
        login.create_driver.driver.find_element(By.XPATH, value=element).send_keys(input)
        time.sleep(1)
        print("TC " + num + " PASS")
        return True
    except Exception as e:
        print(e)
        print("TC " + num + " Fail")
        return False


# Name으로 inputbox 내용 입력
def InputByName(element, input, num):
    '''
    Name으로 inputbox 내용 입력
    :param element: Name
    :param input: input box 입력 내용
    :param num: TC_number
    :return:
    '''
    try:
        login.create_driver.driver.find_element(By.NAME, value=element).clear()
        login.create_driver.driver.find_element(By.NAME, value=element).send_keys(input)
        time.sleep(1)
        print("TC " + num + " PASS")
        return True
    except Exception as e:
        print(e)
        print("TC " + num + " Fail")
        return False


# Name으로 inputbox 내용 입력(인덱스사용)
def InputByNameIndex(element, index, input, num):
    '''
    Name으로 inputbox 내용 입력(인덱스사용)
    :param element: Name
    :param index: 인덱스
    :param input: input box 입력 내용
    :param num: TC_number
    :return:
    '''
    try:
        name_index = login.create_driver.driver.find_elements(By.NAME, value=element)[int(index)]
        name_index.clear()
        name_index.send_keys(input)
        time.sleep(1)
        print("TC " + num + " PASS")
        return True
    except Exception as e:
        print(e)
        print("TC " + num + " Fail")
        return False


# ID로 inputbox 내용 입력 > clear 사용하여 기존 input 내용 초기화 후 input값 입력
def InputClearById(element, input, num):
    '''
    Id로 inputbox 내용 입력
    :param element: Id
    :param input: input box 입력 내용
    :param num: TC_number
    :return:
    '''
    try:
        login.create_driver.driver.find_element(By.ID, value=element).clear()
        login.create_driver.driver.find_element(By.ID, value=element).send_keys(input)
        time.sleep(1)
        print("TC " + num + " PASS")
        return True
    except Exception as e:
        print(e)
        print("TC " + num + " Fail")
        return False


# ID로 inputbox 내용 입력 > delete 사용하여 기존 input 내용 초기화 후 input값 입력
# clear 사용하여 기존 input 초기화 안 될 시 대체 사용
def InputDeleteById(element, input, num):
    '''
    Id로 inputbox 내용 입력
    :param element: Id
    :param input: input box 입력 내용
    :param num: TC_number
    :return:
    '''
    try:
        login.create_driver.driver.find_element(By.ID, value=element).send_keys(Keys.CONTROL + "a")
        login.create_driver.driver.find_element(By.ID, value=element).send_keys(Keys.DELETE)
        login.create_driver.driver.find_element(By.ID, value=element).send_keys(input)
        time.sleep(1)
        print("TC " + num + " PASS")
        return True
    except Exception as e:
        print(e)
        print("TC " + num + " Fail")
        return False


# Select box(xpath) > Value로 특정 값 선택
def SelectBoxByXpath(element, value, num):
    '''
    Select box(xpath 사용) > Value로 특정 값 선택
    :param element: Select box의 xpath 값 입력
    :param value: select box에서 선택할 특정 값 입력 (ex.'전체', '쇼핑몰1')
    :param num: TC_number
    :return:
    '''
    try:
        select = Select(login.create_driver.driver.find_element(by=By.XPATH,
                                                                value=element))
        select.select_by_value(value)
        time.sleep(1)
        print("TC " + num + " PASS")
        return True
    except Exception as e:
        print(e)
        print("TC " + num + " Fail")
        return False


# Select box(Name) > Value로 특정 값 선택
def SelectBoxByName(element, value, num):
    '''
    Select box(xpath 사용) > Value로 특정 값 선택
    :param element: Select box의 xpath 값 입력
    :param value: select box에서 선택할 특정 값 입력 (ex.'전체', '쇼핑몰1')
    :param num: TC_number
    :return:
    '''
    try:
        select = Select(login.create_driver.driver.find_element(by=By.NAME,
                                                                value=element))
        select.select_by_value(value)
        time.sleep(1)
        print("TC " + num + " PASS")
        return True
    except Exception as e:
        print(e)
        print("TC " + num + " Fail")
        return False

# Select box(ID) > Value로 특정 값 선택
def SelectBoxById(element, value, num):
    '''
    Select box(Id 사용) > Value로 특정 값 선택
    :param element: Select box의 Id 값 입력
    :param value: select box에서 선택할 특정 값 입력 (ex.'전체', '쇼핑몰1')
    :param num: TC_number
    :return:
    '''
    try:
        select = Select(login.create_driver.driver.find_element(by=By.ID,
                                                                value=element))
        select.select_by_value(value)
        time.sleep(1)
        print("TC " + num + " PASS")
        return True
    except Exception as e:
        print(e)
        print("TC " + num + " Fail")
        return False


# 크롬 브라우저 탭 이동
def ChangeTap(browernum, num):
    '''
    크롬 브라우저 탭 이동 ('0'부터 시작 ex.1번째 탭은 '0')
    :param browernum: 이동할 탭 위치 입력(정수로 입력 필수, 문자열로 입력하면 안 됨 ex.0)
    :param num: TC_number
    :return:
    '''
    try:
        create_driver.driver.switch_to.window(create_driver.driver.window_handles[browernum])
        time.sleep(3)
        print("TC " + num + " PASS")
        return True
    except Exception as e:
        print(e)
        print("TC " + num + " Fail")
        return False


# 알럿창 [확인] 클릭
def AlertAccept(num):
    '''
    :param num : TC_number
    알럿창 발생 시 알럿창 진입 후 [확인] 버튼 클릭하여 알럿창 종료
    :return:
    '''
    try:
        alert = create_driver.driver.switch_to.alert
        alert.accept()
        time.sleep(2)
        print("TC " + num + " PASS")
        return True
    except Exception as e:
        print(e)
        print("TC " + num + " Fail")
        return False


# 알럿창 [취소] 클릭
def AlertDismiss(num):
    '''
    :param num : TC_number
    알럿창 발생 시 알럿창 진입 후 [취소] 버튼 클릭하여 알럿창 종료
    :return:
    '''
    try:
        alert = create_driver.driver.switch_to.alert
        alert.dismiss()
        time.sleep(2)
        print("TC " + num + " PASS")
        return True
    except Exception as e:
        print(e)
        print("TC " + num + " Fail")
        return False