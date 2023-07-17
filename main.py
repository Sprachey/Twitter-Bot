from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

PROMISED_UP=30.00
PROMISED_DOWN=30.00
TWITTER_EMAIL='Your Email'
TWITTER_PASSWORD='Your Password'

CHROME_DRIVER_PATH="D:\Chrome Driver\chromedriver.exe"

class InternetSpeedTwitterBot:
    def __init__(self) -> None:
        self.driver=webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.driver.maximize_window()
        self.down=''
        self.up=''
    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        sleep(5)
        Go=self.driver.find_element(By.CLASS_NAME,'start-text')
        Go.click()
        sleep(60)
        down_speed=self.driver.find_element(By.CLASS_NAME,'download-speed')
        up_speed=self.driver.find_element(By.CLASS_NAME,'upload-speed')
        self.up=float(up_speed.text)
        self.down=float(down_speed.text)
        sleep(2)
        
    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/')
        sleep(2)
        login=self.driver.find_element(By.XPATH,'//*[@id="layers"]/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/a')
        login.click()
        sleep(3)
        email=self.driver.find_element(By.NAME,'text')
        email.send_keys(TWITTER_EMAIL)
        next_button=self.driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
        next_button.click()
        sleep(2)
        password=self.driver.find_element(By.NAME,'password')
        password.send_keys(TWITTER_PASSWORD)
        log_in=self.driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
        log_in.click()
        sleep(6)
        tweet=self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[1]')
        tweet.click()
        sleep(2)
        tweet_text=self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet_text.send_keys(f"Hey internt provier {PROMISED_UP} is {self.up}")
        tweet_send=self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div')
        tweet_send.click()
        sleep(200)

bot=InternetSpeedTwitterBot()
bot.get_internet_speed()
if PROMISED_UP>bot.up and PROMISED_DOWN>bot.down:
    bot.tweet_at_provider()