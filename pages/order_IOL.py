from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait   # 로딩될 때까지 대기
from selenium.webdriver.support import expected_conditions as EC # 로딩될 때까지 대기
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.support.select import Select # 드롭박스 클릭
from pages import login,order,front_login,front_purchase,create_driver

def findOrder() :
    front_login.login()
    front_purchase.productPurchase()

    time.sleep(3)
    # 주문번호 획득
    orderNum = front_login.create_driver.driver.find_element(by=By.XPATH,
                              value='//*[@id="orderInfoTable"]/table/tbody/tr[3]/td').text
    print(orderNum)

    # admin 로그인
    login.login()
    time.sleep(2)
    order.integratedOrderList()

    # 드롭박스 클릭
    select = Select(login.create_driver.driver.find_element(by=By.NAME, value='mallNo'))
    select.select_by_value("3224")
    login.create_driver.driver.find_element(by=By.CSS_SELECTOR, value='#searchForm > table > tbody > tr:nth-child(2) '
                                                        '> td:nth-child(2) > td > div > div > div > input').send_keys(orderNum)
    login.create_driver.driver.find_element(by=By.CSS_SELECTOR, value='#searchForm > table > tbody > tr:nth-child(2) >'
                                                        ' td.search_btn_wrap > div > button.tbBtn.type-red').click()

    time.sleep(3)
    # ActionChains 사용하여 해당 요소에 접근 후 클릭
    element = front_login.create_driver.driver.\
        find_element(by=By.CSS_SELECTOR, value="body > div > div.container-wrap > "
                                        "div.content-bottom-wrap > div.contents > "
                                        "div > div.mall-orders-view > div > "
                                        "div.content_item_bx > div > div > "
                                        "div.tui-pagination.tui-grid-pagination > strong")
    action = ActionChains(front_login.create_driver.driver).move_to_element(element)
    action.perform()

    time.sleep(5)  # 5초 대기
    login.create_driver.driver.quit()

