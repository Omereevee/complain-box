import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# ---- creates driver ---- #
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

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
        print("done")
        time.sleep(60)

        self.down = self.driver.find_element(By.CLASS_NAME,"download-speed").text
        self.up= self.driver.find_element(By.CLASS_NAME,"upload-speed").text

        print(self.up)
        print(self.down)

        if int(self.up) > PROMISED_UP or  int(self.down) > PROMISED_DOWN:
            self.tweet_at_provider()

    def tweet_at_provider(self):
        self.driver.get(Y_LOGIN_URL)

        self.y_email = self.driver.find_element(By.ID,"email")
        self.y_password = self.driver.find_element(By.ID,"password")
        self.y_login_button = self.driver.find_element(By.CLASS_NAME,"y-login-submit")

        self.y_email.send_keys(Y_EMAIL)
        self.y_password.send_keys(Y_PASSWORD)
        self.y_login_button.click()

        self.y_tweet = self.driver.find_element(By.CLASS_NAME,"x-compose")
        self.y_send = self.driver.find_element(By.ID,"post-btn")

        self.y_tweet.send_keys(f"why is my internet speed {self.up} up/{self.down} down when i pay for {PROMISED_UP} up/{PROMISED_DOWN} down")
        self.y_send.click()


# ---- Execution ---- #

InternetSpeedYBot = InternetSpeedYBot()

InternetSpeedYBot.get_internet_speed()


