from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait   # 로딩될 때까지 대기
from selenium.webdriver.support import expected_conditions as EC # 로딩될 때까지 대기
import time

driver = webdriver.Chrome("./chromedriver.exe")
url = 'https://alpha-admin.shopby.co.kr'
driver.get(url)

# 쇼핑몰 로그인
def login() :
    WebDriverWait(driver, 10).until(EC.presence_of_element_located\
                                   ((By.XPATH,'//*[@id="container"]/div[2]/div/form/div/table/tr[1]/td/input')))
    driver.find_element(by=By.XPATH, value='//*[@id="container"]/div[2]/div/form/div/table/tr[1]/td/input').send_keys('shopbyproadmin')  # xpath 사용
    driver.find_element(by=By.CSS_SELECTOR, value='#container > div.content_login > div > form > div > table > tr:nth-child(2) > td > input').send_keys('WkaQhd@629') # css_selector 사용
    driver.find_element(by=By.CSS_SELECTOR, value='#container > div.content_login > div > form > button:nth-child(2)').click()
