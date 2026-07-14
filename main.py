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
PROMISED_UP = None
PROMISED_DOWN = None

Y_EMAIL = "omerkumble@gmail.com"
Y_PASSWORD = "jgpj9wgh1t2nY0Yt"
Y_LOGIN_URL = "https://app.100daysofpython.dev/services/y/login"
SPEED_URL = "https://speedtest.net"

# ---- logic ---- #
class InternetSpeedYBot:
    def __init__(self, up, down):
        self.driver = driver
        self.up = up
        self.down = down

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

    def tweet_at_provider(self):
        pass

# ---- Execution ---- #
InternetSpeedYBot = InternetSpeedYBot(100, 10)

InternetSpeedYBot.get_internet_speed()
InternetSpeedYBot.tweet_at_provider()


