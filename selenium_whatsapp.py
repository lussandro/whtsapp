from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class WhatsAppBot:
    def __init__(self):
        print("Starting Whtasapp Bot")
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=webdriver.DesiredCapabilities.CHROME
        )
        self.login()

    def login(self):
        self.driver.get("https://web.whatsapp.com")
        print("Please scan the QR code to log in.")
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "._2_1wd"))
        )
        print("Logged in.")

    def send_message(self, contact_name, message):
        try:
            self.driver.find_element_by_css_selector("._2_1wd").click()
            search_box = self.driver.switch_to.active_element
            search_box.send_keys(contact_name)
            search_box.send_keys(Keys.RETURN)

            message_input = self.driver.find_element_by_css_selector("._2A8P4")
            message_input.send_keys(message)
            message_input.send_keys(Keys.RETURN)
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
