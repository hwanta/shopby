from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait   # 로딩될 때까지 대기
from selenium.webdriver.support import expected_conditions as EC # 로딩될 때까지 대기
from pages import login


# 메인(TC 1~119)
# 메인 > 판매현황
def sales():
    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located \
                                              ((By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[1]/div[1]/'
                                                              'div[1]/div[2]/div/div/ul[1]/li[2]/p[2]/a')))
    # # 메인 > 입금대기 카운트
    # waitingm = login.create_driver.driver.find_element(by=By.XPATH,
    #                                                   value='/html/body/div[1]/div[3]/div[2]/div[1]/div[1]'
    #                                                         '/div[1]/div[2]/div/div/ul[1]/li[1]/p[2]/a').text

    element = login.create_driver.driver.find_element(by=By.XPATH, value='/html/body/div/div[3]/div[2]/div[1]/div[1]'
                                                                         '/div[1]/div[2]/div/div/ul[1]/li[1]/p[2]/a/strong')
    login.create_driver.driver.execute_script("arguments[0].click();", element)

    # 입금대기 리스트 출력되는지 확인
    try:
        login.create_driver.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[3]/div[2]/div[1]'
                                                                  '/div[1]/div[1]/div[2]/div/div/ul[1]/'
                                                                  'li[1]/p[2]/a/strong').is_displayed()
        print("입금대기 리스트 출력됨")

    except:
        print("입금대기 리스트 미출력됨")

    # 메인 > 입금대기 카운트와 주문 > 입금대기 리스트에 출력되는 카운트 비교
    # try:
    #     waitingo = login.create_driver.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[3]/div[2]/div[1]/div/div[2]/div/div[1]/span[1]/span').text
    #     result = waitingm == waitingo
    #     if(result):
    #         print("카운트 동일")
    #     else:
    #         print("카운트 다름")
    # except:
    #     print("비교가 안되구나")

# # 메인 > 문의/답변 현황
# def inquiry():
#
# # 메인 > 클레임 현황
# def claim():
#
# # 메인 > 처리지연 현황
# def delay():
#
# # 메인 > 상품 현황
# def product():
#
# # 메인 > 공지사항
# def announcement():
#
# # 메인 > 업그레이드
# def upgrade():
#
# # 메인 > 샵바이프로 매뉴얼 다운로드, 자주 묻는 질문 바로가기
# def manual():