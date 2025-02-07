import time

from selenium.webdriver.common.by import By


class TestBasket:

    def test_languages(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        assert browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket").is_enabled(), \
            "There is no button to add item to basket"
        time.sleep(30)
