from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import os
import pickle

class WhatsAppBot:
    def __init__(self):
        print("Starting Whtasapp Bot")
        self.timeout = 60
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=webdriver.DesiredCapabilities.CHROME
        )
        self.login()


    def save_session(self, session_file):
        session_data = {
            'cookies': self.driver.get_cookies(),
            'url': self.driver.current_url
        }

        with open(session_file, 'wb') as f:
            pickle.dump(session_data, f)


    def load_session(self, session_file):
        if os.path.exists(session_file):
            with open(session_file, 'rb') as f:
                session_data = pickle.load(f)
                self.driver.get(session_data['url'])

                for cookie in session_data['cookies']:
                    if 'expiry' in cookie:
                        del cookie['expiry']
                    self.driver.add_cookie(cookie)

    def login(self):
        self.driver.get("https://web.whatsapp.com/")
        print("Por favor, escaneie o QR Code.")

        WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "._3PwsU"))
        )
        print("Login bem-sucedido.")

    def is_logged_in(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, "._3PwsU")
            return True
        except NoSuchElementException:
            return False

    def send_message(self, contact_name, message):
        search_input = self.driver.find_element(By.CSS_SELECTOR, "._3FRCZ")
        search_input.clear()
        search_input.send_keys(contact_name)
        time.sleep(1)

        contact = self.driver.find_element(By.CSS_SELECTOR, "._2UaNq")
        contact.click()
        time.sleep(1)

        input_box = self.driver.find_element(By.CSS_SELECTOR, "._3uMse")
        input_box.send_keys(message)
        input_box.send_keys(Keys.RETURN)

    def get_unread_messages(self):
        unread_messages = []
        chats = self.driver.find_elements(By.CSS_SELECTOR, "._3Xjbn")  # Atualize o seletor CSS para os chats

        for chat in chats:
            try:
                name = chat.find_element(By.CSS_SELECTOR, "._2PKKH").text  # Atualize o seletor CSS para o nome
                last_message = chat.find_element(By.CSS_SELECTOR, ".copyable-text").text  # Atualize o seletor CSS para a última mensagem
                message_count = int(chat.find_element(By.CSS_SELECTOR, "._38M1B").text)  # Atualize o seletor CSS para a contagem de mensagens

                unread_messages.append({
                    "name": name,
                    "last_message": last_message,
                    "message_count": message_count
                })
            except Exception as e:
                continue

            return unread_messages
