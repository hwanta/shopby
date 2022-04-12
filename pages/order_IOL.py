from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait   # 로딩될 때까지 대기
from selenium.webdriver.support import expected_conditions as EC # 로딩될 때까지 대기
import time
from selenium.webdriver.support.select import Select # 드롭박스 클릭
from pages import login,order,front_login,front_purchase

def findOrder() :
    front_login.login()
    front_purchase.productPurchase()

    time.sleep(2)
    # 주문번호 획득
    orderNum = front_login.driver.find_element(by=By.XPATH,
                              value='//*[@id="orderInfoTable"]/table/tbody/tr[3]/td').text
    print(orderNum)
    # front driver 닫음
    front_login.driver.close()

    # admin 로그인
    login.login()
    order.integratedOrderList()

    # 드롭박스 클릭
    select = Select(login.driver.find_element(by=By.NAME, value='mallNo'))
    select.select_by_value("3224")
    login.driver.find_element(by=By.CSS_SELECTOR, value='#searchForm > table > tbody > tr:nth-child(2) '
                                                        '> td:nth-child(2) > td > div > div > div > input').send_keys(orderNum)
    login.driver.find_element(by=By.CSS_SELECTOR, value='#searchForm > table > tbody > tr:nth-child(2) >'
                                                        ' td.search_btn_wrap > div > button.tbBtn.type-red').click()
