from config import config_browser, get_data
from driver import Browser

from logger import CustomLogger
from Pages.captcha_page import CaptchaPage
import time
LOGGER = CustomLogger.get_logger(__name__)

if '__main__' == __name__:
    '''Configuring browser'''
    config_browser_data = config_browser()
    data = get_data()
    browser_i = Browser(config_browser_data)
    browser_i.driver.get(data["start_url"])
    captcha_page = CaptchaPage(browser_i.wait_time)
    captcha_page.solve_captcha()
    browser_i.save_screenshot()  # for reuslt check the result image in Resources folder
    browser_i.quit()
