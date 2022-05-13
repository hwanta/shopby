import time
import login


def close():
    time.sleep(3)
    login.create_driver.driver.quit()