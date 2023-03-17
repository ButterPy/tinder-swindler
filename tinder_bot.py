from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import selenium.webdriver.support.ui as ui

import time


class TinderBot():
    path = '/usr/bin/chromedriver'
    web = 'https://tinder.com'
    service = Service(executable_path=path)
    opening_line = "HI :)"

    def __init__(self):
        self.options = Options()
        self.options.add_experimental_option("debuggerAddress", "localhost:9222")
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        self.driver.get(self.web)
        self.wait = ui.WebDriverWait(self.driver, 10)
        time.sleep(3)

    def like(self):
        like_button = self.driver.find_element(by='xpath', value='//button//span[text()="Like"]')
        self.wait.until(lambda driver: self.driver.find_element(by='xpath', value='//button//span[text()="Like"]'))
        self.driver.execute_script("arguments[0].click();", like_button)
        time.sleep(3)
        self.match()

    def send_message(self):
        send_message_button = self.driver.find_element(by='xpath', value='//button/span[text()="Send"]')
        send_message_button.click()
        self.close_match_window()

    def match(self):
        try:
            its_match_window = self.driver.find_element(by='xpath',
                                                        value='//textarea[@placeholder="Say something nice!"]')
            its_match_window.send_keys(self.opening_line)
            self.send_message()
        except:
            pass

    def search_for_like_button(self):
        like_button_check = False
        while not like_button_check:
            like_button = self.driver.find_element(by='xpath', value='//button//span[text()="Like"]')
            if like_button:
                like_button_check = True

    def close_match_window(self):
        close_its_match_window = self.driver.find_element(by='xpath', value='//button[@title="Back to Tinder"]')
        close_its_match_window.click()

    def advert_close(self):
        box = self.driver.find_element(by='xpath',
                                  value='//button/span[text()="Maybe Later"] | //button/span[text()="Not interested"] | //button/span[text()="No Thanks"]')
        box.click()



bot = TinderBot()
bot.like()