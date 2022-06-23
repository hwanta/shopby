from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # 로딩될 때까지 대기
from selenium.webdriver.support import expected_conditions as EC  # 로딩될 때까지 대기
from pages.setting import option
import time, random
from selenium.webdriver.common.keys import Keys
from libs import login, element, create_driver
from selenium.webdriver.support.select import Select

# 상품 > 상품 관리 > 상품 리스트
def accessProductList() :
    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.CSS_SELECTOR,'body > div > div.header-wrap > div.gnb-wrap > div.left-wrap > ul > li.on > a')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="상품").click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.LINK_TEXT,'상품 관리')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="상품 관리").click()

    WebDriverWait(login.create_driver.driver, 10).until(EC.presence_of_element_located\
                                   ((By.LINK_TEXT,'상품 리스트')))
    login.create_driver.driver.find_element(by=By.LINK_TEXT, value="상품 리스트").click()

# 상품 리스트 > 검색조건 설정하여 상태로 [검색] (TC_1) *** 상품 검색 후 검증 필요
def searchProduct() :
    # 검색조건 > 쇼핑몰 > '전체' 선택 (쇼핑몰이 1개인 경우 비활성화)
    # element.SelectBoxByName('mallNo', '전체', '1-1')
    # 검색조건 > 파트너사 > '전체' 선택
    element.ClickById('all', '1-2')
    # 검색조건 > 검색어 > '상품명' + 인풋박스 공란
    element.SelectBoxById('searchKeywordType', 'PRODUCT_NAME', '1-3')
    element.InputClearById('searchKeywordInput', '', '1-4')
    # 검색조건 > 기간 > '상품등록일' + '1개월' 선택
    element.SelectBoxByName('periodInfo', 'REGISTER_DATE', '1-5')
    element.ClickByText('1개월', '1-6')
    # 검색조건 > 상품상태 > '승인상태' + 체크박스 전체 선택
    element.SelectBoxByName('applyStatus', 'ALL', '1-7')
    # 검색조건 > 카테고리 > '전시 카테고리' + 1 Depth 선택
    element.ClickByCSS_Selector('#searchForm > table > tbody > tr:nth-child(7) > td > div > select > option:nth-child(1)', '1-8')
    # 검색조건 > [검색] 버튼 클릭
    element.ClickByText(' 검색 ', '1')

# 상품 리스트 > 검색조건 설정 후 [초기화] (TC_2) *** 초기화 후 검증 필요
def searchProductReset() :
    # 검색조건 > 쇼핑몰 > '전체' 선택 (쇼핑몰이 1개인 경우 비활성화)
    # element.SelectBoxByName('mallNo', '전체', '2-1')
    # 검색조건 > 파트너사 > '전체' 선택
    element.ClickById('all', '2-2')
    # 검색조건 > 검색어 > '상품명' + 인풋박스 공란
    element.SelectBoxById('searchKeywordType', 'PRODUCT_NAME', '2-3')
    element.InputClearById('searchKeywordInput', '', '2-4')
    # 검색조건 > 기간 > '상품등록일' + '1개월' 선택
    element.SelectBoxByName('periodInfo', 'REGISTER_DATE', '2-5')
    element.ClickByText('1개월', '2-6')
    # 검색조건 > 상품상태 > '승인상태' + 체크박스 전체 선택
    element.SelectBoxByName('applyStatus', 'ALL', '2-7')
    # 검색조건 > 카테고리 > '전시 카테고리' + 1 Depth 선택
    element.ClickByCSS_Selector('#searchForm > table > tbody > tr:nth-child(7) > td > div > select > option:nth-child(1)', '2-8')
    # 검색조건 > [초기화] 버튼 클릭
    element.ClickByText(' 초기화 ', '2')

# 상품 리스트 > 검색조건 df 검색 후 와우상품 수정 (TC_3) *** 수정 후 검증 필요
def productModify() :
    # 검색조건 df로 검색 *** 추후 신규 상품 등록한 후 그걸 수정 확인 하는 것으로 변경 필요(그리드의 상품번호로 매칭 시키는 방법 생각해보기)
    element.ClickByText(' 검색 ', '3-1')
    # 상품리스트에서 가장 최근 등록 상품 [수정] 버튼 클릭
    element.ClickByXPath('/html/body/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div[1]/table/tbody/tr[1]/td[2]/div/a', '3-2')

    # 일반 상품 수정 > 상품명, 판매가, 재고수량 변경 후 [저장]
    # 일반 상품 수정 페이지로 이동 (1번 탭으로 이동)
    element.ChangeTap(-1, '3-3')
    # 현재 샵바이 프로 알파 > BPC 도입 관련 이슈 발생으로 '파트너사' 관련 알럿이 출력 됨(테스트를 위해 알럿 '확인' 클릭하여 제거)
    element.ClickById('productName', '3-991')
    element.AlertAccept('3-992')
    # 일반 상품 수정 > 상품명 수정
    element.InputDeleteById('productName', 'PL_test_tc_3', '3-4')
    # 일반 상품 수정 > 판매가 수정
    element.InputClearById('productSalePrice', '300', '3-5')
    # 일반 상품 수정 > 재고수량 수정
    element.InputClearById('productStockCnt', '30', '3-6')
    # 일반 상품 수정 > [저장] 버튼 클릭
    element.ClickByText(' 저장 ', '3-7')
    # '수정되었습니다.' 알럿 종료
    element.AlertAccept('3')

# 상품 리스트 > 검색조건 df 검색 후 상품 복사 등록 (TC_4) *** 등록 후 검증 필요
def productCopy():
    # 검색조건 df로 검색 *** 추후 신규 상품 등록한 후 그걸 복사 등록 해서 확인 하는 것으로 변경 필요
    element.ClickByText(' 검색 ', '4-1')
    # 상품리스트에서 가장 최근 등록 상품 [복사] 버튼 클릭
    element.ClickByXPath('/html/body/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div[1]/table/tbody/tr[1]/td[3]/div/a', '4-2')

    # 상품 복사 팝업 > 재고수량 연동/재고수량 복사 확인 후 [상품 복사]
    # 상품 복사 팝업으로 이동
    element.ChangeTap(-1, '4-3')
    # 재고수량 연동 : 연동 안함
    element.ClickById('N', '4-4')
    # 재고수량 복사 : 복사 안함
    element.ClickById('stock_N', '4-5')
    # [상품 복사] 버튼 클릭
    element.ClickByCSS_Selector('#wrapper > div > div.box-cont.type-3 > div.button-wrap > button.btnDef.type-red', '4-6')

    # 상품 복사 > 표준 카테고리, 전시 카테고리 선택 및 상품명, 판매가, 재고수량 변경 후 [저장]
    # 상품 복사 페이지로 이동
    element.ChangeTap(-1, '4-7')
    # 표준 카테고리 선택(검색하여 선택)
    element.InputByXPath('/html/body/div/div[3]/div[2]/div[1]/div[1]/div[2]/table/tbody/tr[5]/td/div[1]/div[1]/input', '롱부츠', '4-8')
    element.ClickByXPath('/html/body/div/div[3]/div[2]/div[1]/div[1]/div[2]/table/tbody/tr[5]/td/div[1]/div[1]/ul/li[1]', '4-9')
    # 전시 카테고리 선택(검색하여 선택)
    element.InputByXPath('/html/body/div/div[3]/div[2]/div[1]/div[1]/div[2]/table/tbody/tr[6]/td/div/div[1]/input', '예시', '4-10')
    element.ClickByXPath('/html/body/div/div[3]/div[2]/div[1]/div[1]/div[2]/table/tbody/tr[6]/td/div/div[1]/ul/li', '4-11')
    # 상품명 변경
    element.InputDeleteById('productName', '상품 복사등록 테스트', '4-12')
    # 판매가 변경
    element.InputClearById('productSalePrice', '500', '4-13')
    # 재고수량 변경
    element.InputClearById('productStockCnt', '50', '4-14')
    # [저장] 버튼 클릭
    element.ClickByText(' 저장 ', '4')