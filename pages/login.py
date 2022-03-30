from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager  # import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait   # 로딩될 때까지 대기
from selenium.webdriver.support import expected_conditions as EC # 로딩될 때까지 대기
import time

# driver 옵션 추가(시스템에 부착된 장치가 작동하지 않습니다. 삭제 옵션)
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
url = 'https://alpha-admin.shopby.co.kr'
driver.get(url)

# 쇼핑몰 로그인
def login() :
    try :
        WebDriverWait(driver, 10).until(EC.presence_of_element_located\
                                    ((By.XPATH,'//*[@id="container"]/div[2]/div/form/div/table/tr[1]/td/input')))
        driver.find_element(by=By.XPATH, value='//*[@id="container"]/div[2]/div/form/div/table/tr[1]/td/input').send_keys('shopbyproadmin')  # xpath 사용
        driver.find_element(by=By.CSS_SELECTOR, value='#container > div.content_login > div > form > div > table > tr:nth-child(2) > td > input').send_keys('WkaQhd@629') # css_selector 사용
        driver.find_element(by=By.CSS_SELECTOR, value='#container > div.content_login > div > form > button:nth-child(2)').click()
    
        # alert 존재하면 내용 출력, 없으면 pass 출력
        WebDriverWait(driver, 3).until(EC.alert_is_present()) 
        alert = driver.switch_to.alert
        print(alert.text)
        alert.accept()
    except : 
        print("pass")
