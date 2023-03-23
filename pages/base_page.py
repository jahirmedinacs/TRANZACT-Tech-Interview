from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


import random

class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def click(self, by_locator):
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def click_random_element_from_list(self, by_locator):
        elements = WebDriverWait(self.browser, 10).until(EC.visibility_of_all_elements_located(by_locator))
        random_element = random.choice(elements)
        random_element.click()

    def get_elements(self, by_locator):
        return WebDriverWait(self.browser, 10).until(EC.visibility_of_all_elements_located(by_locator))

    def enter_text(self, by_locator, text):
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_text(self, by_locator):
        return WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(by_locator)).text

    def select_dropdown_option(self, by_locator, choice):
        dropdown_element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(by_locator))
        select = Select(dropdown_element)
        select.select_by_visible_text(choice)

    def switch_to_iframe_by_xpath(self, by_locator):
        iframe_element = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(by_locator))
        self.browser.switch_to.frame(iframe_element)

    def switch_to_main_content(self):
        self.browser.switch_to.default_content()