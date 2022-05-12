import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))) # 폴더 다를 때 사용

from lib import login
from pages.setting import option
import time

# 로그인
login.login()

# 설정 > 기본정책
option.basicInformation()

option.mallManagement()

option.terms()

option.externalService()

# # 설정 > 관리정책
option.operatorManagement()

option.permissionGroup()

# # 설정 > 보안정책
option.operationalSecuritySettings()

option.personalInformationAccess()

option.securityManagementServer()

# 설정 > 배송정책
option.shippingCostManagement()

# 설정 > 결제정책
option.pgSettings()

option.paycoPaymentSettings()

option.naverPaymentSettings()

time.sleep(5) # 5초 대기
lib.create_driver.driver.quit()
