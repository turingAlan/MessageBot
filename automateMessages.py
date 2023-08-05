from selenium import webdriver
import os
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service

option = webdriver.ChromeOptions()
option.add_argument("start-maximized")


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)


audience = ['sundarpichai','virat kohli','rudymancuso']
message = "this is an automated message"

class instaBot:

    def __init__(self, username, password,target, audience, message):

        self.username = username

        self.password = password

        self.user = audience
        
        self.message = message

        self.targetAudience = target

        self.base_url = 'https://www.instagram.com/'

        self.bot = driver

        self.login()
    
    def login(self):
        self.bot.get(self.base_url)

        enter_username = WebDriverWait(self.bot, 20).until(expected_conditions.presence_of_element_located((By.NAME, 'username')))
        enter_username.send_keys(self.username)

        enter_password = WebDriverWait(self.bot, 20).until(expected_conditions.presence_of_element_located((By.NAME, 'password')))
        enter_password.send_keys(self.password)

        enter_password.send_keys(Keys.RETURN)
        time.sleep(5)

        self.accountList()
        time.sleep(2)

        # to close popup
        self.bot.find_element("xpath",'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div').click()
        time.sleep(5)

        # to close popup
        self.bot.find_element("xpath",'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
        time.sleep(5)

        # to click on meassage icon
        self.bot.find_element("xpath",'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[5]/div/div/div/span/div/a').click()
        time.sleep(5)

        # to click on pencil icon
        self.bot.find_element("xpath",'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[1]/div/div[1]/div[2]/div/div').click()
        time.sleep(3)

        for i in audience:

            #for search bar
            self.bot.find_element("xpath",'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/input').send_keys(i)
            time.sleep(2)

            #for selecting top result
            self.bot.find_element("xpath",'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/div/div[1]').click()
            time.sleep(2)

            #for chat button
            self.bot.find_element("xpath",'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[4]/div').click()
            time.sleep(2)

            send = self.bot.find_element("xpath",'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]')
            
            send.send_keys(self.message)
            time.sleep(1)
            send.send_keys(Keys.RETURN)

            time.sleep(2)


            #to again click on the pencil button
            self.bot.find_element("xpath",'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[1]/div/div[1]/div[2]/div/div').click()
            time.sleep(3)

    def accountList(self):
        # to click on the search user icon
        self.bot.find_element("xpath",'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a').click()
        time.sleep(2)

        #to search on the search bar
        search_input = self.bot.find_element("xpath",'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input')
        search_input.send_keys(self.targetAudience)
        search_input.send_keys(Keys.RETURN)
        time.sleep(5)
        # to get the list of all the accouts
        account_conatiner = self.bot.find_element("xpath",'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div')
        account_list = account_conatiner.find_elements(By.CSS_SELECTOR,'span.x1s6885')
        print(account_list, "this is the full account list")
        # time.sleep(2)
        # new_list = [account_item for index,account_item in enumerate(account_list) if index % 3 ==0]
        # print(new_list, "this is the account list")

def init():
    instaBot("sarthak0jain@gmail.com","Sarthak@0909","marketing",audience,message)
    input("done")

init()






