from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # 로딩될 때까지 대기
from selenium.webdriver.support import expected_conditions as EC  # 로딩될 때까지 대기
from pages import login

def enter_Board():
    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located \
                                              ((By.LINK_TEXT, '게시판')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value='게시판').click()
    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located \
                                                            ((By.LINK_TEXT, '게시판 관리')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value='게시판 관리').click()
    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located \
                                                            ((By.LINK_TEXT, '게시판 리스트')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value='게시판 리스트').click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located \
                                                            ((By.CSS_SELECTOR, '#tui-tree-node-4 > div')))
    login.create_driver.driver.find_element(by=By.CSS_SELECTOR, value='#tui-tree-node-4 > div').click()

    login.create_driver.driver.find_element(by=By.NAME, value='boardCommon2').click()

    element = login.create_driver.driver.find_element(by=By.XPATH, value='/html/body/div/div[4]/div/div[2]')
    login.create_driver.driver.execute_script("arguments[0].click();",element)