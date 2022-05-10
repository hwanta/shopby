from selenium.webdriver.common.by import By
from pages import login
from pages.setting import malls


# 설정 > 기본정책 > 쇼핑몰관리 > 쇼핑몰 수정
def mallEdit() :

    option_MM.clickMallName()

    # 쇼핑몰명 변경
    mallName = login.create_driver.driver.find_element(by=By.NAME,
                                        value='mall.mallName')
    mallName.clear()
    mallName.send_keys('shopbypro_QA_11111')

    # 고객센터 전화번호
    mallName = login.create_driver.driver.find_element(by=By.NAME,
                                         value='mall.serviceCenter.phoneNo')
    mallName.clear()
    mallName.send_keys('01054876598')

    # 고객센터 이메일
    email1 = login.create_driver.driver.find_elements(by=By.NAME,
                                         value='representative.email')[0]
    email1.clear()
    email1.send_keys('byungwook.lee')

    email2 = login.create_driver.driver.find_elements(by=By.NAME,
                                         value='representative.email')[1]
    email2.clear()
    email2.send_keys('nhnsoft.com')

