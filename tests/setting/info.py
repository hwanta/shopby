import sys, os # 폴더 다를 때 사용
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from lib import login
from pages.setting import info
import time


def infoTC():
    login.login()
    time.sleep(2)

    info.accessBI()

    info.companyName()

    info.representativeName()

    info.companyRegistrationNumber()

    info.representativeNumber()

    info.telemarketingNumber()

    info.representativeEmail()

    info.faxNumber()

    info.businessType()

    info.businessConditions()

    info.businessAddress()

    info.managerName()

    info.managerNumber()

    info.managerInfo()

    info.managerEmail()

    info.save()

    time.sleep(3)  # 3초 대기
    login.create_driver.driver.quit()
