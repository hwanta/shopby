import time
import create_driver

def close():
    time.sleep(3)
    create_driver.driver.quit()