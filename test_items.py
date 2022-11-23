from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_basket_button_visible(browser):
    browser.get(link)
    btn = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    assert btn.is_displayed()
    time.sleep(20)
