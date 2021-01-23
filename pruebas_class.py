import time
import datetime
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import InvalidArgumentException

import sys

class Driver:

    def __init__(self, greet_string, browser_user="prueba2"):

        self.browser_user=browser_user
        self.greet_string=greet_string

        self.driver=self.connect()

    def connect(self):
        try:
            # ChromeOptions allows us use the userdata of chrome 
            # so that you don't have to sign in manually everytime. 
            chropt = webdriver.ChromeOptions()
            # adding userdata argument to ChromeOptions object 
            chropt.add_argument("user-data-dir=/home/agustin/.config/google-chrome/"+self.browser_user) 
            # Creating a Chrome webdriver object 
            driver = webdriver.Chrome(options = chropt)
            driver.get("https://web.whatsapp.com/")
            # delay added to give time for all elements to load 
            time.sleep(10)

        except InvalidArgumentException as exception:
            print("Error:")
            print(exception)
            print ("Close all the Browser windows cotrolled by Selenium and re-start the execution!")
            sys.exit(1)


        return driver

    def getUser(self):
        try:
            self.driver.find_elements_by_class_name("rlUm6")[0].click()
            time.sleep(1)
            user_name= self.driver.find_elements_by_class_name("_1awRl")[0].text
            self.driver.find_elements_by_class_name("hYtwT")[0].click()
        except IndexError as exception:
            print("Error:")
            print ("Log-in to WhatsApp web scanning the logo!")
            sys.exit(1)

            return user_name
        
    def closeDriver(self):

        self.driver.close()

        return 0

class Panel:

    def __init__(self, driver, user, greet_string, chats=[], timeout=time.time()+60):

        self.driver=driver
        self.user=user
        self.greet_string=greet_string
        self.chats=chats
        self.timeout=timeout

    def greetChats(self):
        span=0
        driver_chats = self.driver.find_elements_by_class_name("_1MZWu")
        panel = self.driver.find_element_by_class_name('_3Xjbn')

        while True:
            
            for driver_chat in driver_chats:

                driver_chat.click()
                chat=Chat(self.driver, self.user , self.greet_string)

                if chat.greet() and (chat.name() not in self.chats):

                    input_box=self.driver.find_element_by_class_name('DuUXI')
                    input_box.send_keys(self.greet_string+Keys.ENTER)

                self.chats.append(chat.name())

            span += 1200
            self.driver.execute_script('arguments[0].scrollTop = %s' %span, panel)
            driver_chats = self.driver.find_elements_by_class_name("_1MZWu")

            if time.time() > self.timeout:
                break
        
        return 0

class Chat:

    def __init__(self, driver, user_name, greet_string):

        self.driver=driver
        self.user_name=user_name
        self.greet_string=greet_string

    def name(self):
        return self.driver.find_elements_by_class_name("YEe1t")[0].text

    def actuaDate():
        now = datetime.datetime.now()
        return (now.strftime("%d/%m/%Y"))

    def readMsgs(self):

        chat_msgs=[]
        today=actuaDate()

        htmlcode=(self.driver.page_source).encode('utf-8')
        soup = BeautifulSoup(htmlcode,features="html.parser")
        for tag in soup.find_all('div', class_="_1ij5F"):
            persona=tag.find_all("div", class_="_2XJpe")
            if persona:
                name_persona=persona[0].find_all("div", class_="copyable-text")
                if name_persona:

                    info_msg=(name_persona[0].get_attribute_list("data-pre-plain-text"))
                    name_msg=info_msg[0].split("]")[1].strip(" ")[:-1]
                    time_msg=info_msg[0].split("]")[0].split(",")[1].lstrip(" ")
                    text_msg=(name_persona[0].text)
                    if time_msg = today:
                        chat_msgs.append((name_msg, time_msg, text_msg))

        return chat_msgs

    def greet(self):

        chat_msgs = self.readMsgs()
        word=["pepito125"]

        res=False
        user_greet=True
        else_greet=False

        for msg in chat_msgs:
            for element in word:
                if element in msg[2].lower() and msg[0] != self.user_name :
                    else_greet=True

            if msg[2] == self.greet_string and msg[0] == self.user_name:
                user_greet=False

        return else_greet and user_greet

if __name__ == '__main__':


    driver = Driver("Bien02")
    panel=Panel(driver.driver, driver.getUser(), driver.greet_string)
    panel.greetChats()
    driver.closeDriver()