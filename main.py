import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
# ---- creates driver ---- #
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
user_data_dir = os.path.join(os.getcwd(),"chrome_profile")

chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)

# ---- constants ---- #
PROMISED_UP = 50
PROMISED_DOWN = 256

Y_EMAIL = "omerkumble@gmail.com"
Y_PASSWORD = "jgpj9wgh1t2nY0Yt"
Y_LOGIN_URL = "https://app.100daysofpython.dev/services/y/login"
SPEED_URL = "https://speedtest.net"

# ---- logic ---- #
class InternetSpeedYBot:
    def __init__(self):
        self.driver = driver
        self.up = None
        self.down = None

    def get_internet_speed(self):
        self.driver.get(SPEED_URL)

        go = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[4]/div/div/div/div[2]/div[2]/div/div[2]/a/span[4]' )
        #go = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[4]/div/div/div/div[2]/div[2]/div/div[2]/a/span[4]' )

        if go:

            print("got go ")
        go.click()

        time.sleep(60)
        print("done")

        self.down = self.driver.find_element(By.CLASS_NAME,"download-speed").text
        self.up= self.driver.find_element(By.CLASS_NAME,"upload-speed").text
        if self.up and self.down:
            print(self.up)
            print(self.down)

        if float(self.up) <PROMISED_UP or  float(self.down) < PROMISED_DOWN:
            self.tweet_at_provider()

    def tweet_at_provider(self):
        self.driver.get(Y_LOGIN_URL)

        y_email = self.driver.find_element(By.ID,"email")
        y_password = self.driver.find_element(By.ID,"password")
        y_login_button = self.driver.find_element(By.CLASS_NAME,"y-login-submit")

        y_email.send_keys(Y_EMAIL)
        y_password.send_keys(Y_PASSWORD)
        y_login_button.click()

        y_tweet = self.driver.find_element(By.CLASS_NAME,"x-compose")
        y_send = self.driver.find_element(By.ID,"post-btn")

        y_tweet.send_keys(f"why is my internet speed {self.up} up/{self.down} down when i pay for {PROMISED_UP} up/{PROMISED_DOWN} down")
        y_send.click()


# ---- Execution ---- #

InternetSpeedYBot = InternetSpeedYBot()

InternetSpeedYBot.get_internet_speed()


