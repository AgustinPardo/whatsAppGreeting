import time
import datetime
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

class Driver:

    def __init__(self,  exec_time, browser_user="prueba2"):
        self.browser_user=browser_user
        self.lapse_time=lapse_time
        self.exec_time=exec_time

    def run(self):
        # ChromeOptions allows us use the userdata of chrome 
        # so that you don't have to sign in manually everytime. 
        chropt = webdriver.ChromeOptions() 
        
        # adding userdata argument to ChromeOptions object 
        chropt.add_argument("user-data-dir=/home/agustin/.config/google-chrome/"+self.browser_user) 
        
        # Creating a Chrome webdriver object 
        driver = webdriver.Chrome(options = chropt)

        driver.get("https://web.whatsapp.com/")

        # delay added to give time for all elements to load 
        time.sleep(7)

        return driver

    def getUser(self, driver):
        pass

class Panel:

    def __init__(self, driver, timeout=time.time()+5, chats= {}:

        self.driver=driver
        self.timeout=timeout
        self.dirver=chats
    
    def spanPanel(self):

        panel = self.driver.find_element_by_class_name('_3Xjbn')
        span += 1200
        self..execute_script('arguments[0].scrollTop = %s' %span, panel)
        time.sleep(1)


    def addChats(self):

        while True:
            driver_chats = self.driver.find_elements_by_class_name("_1MZWu")

            for driver_chat in driver_chats:
                driver_chat.click()
                chat=Chat(driver_chat)

                chats[chat.chatName()]=chat.readMsgs()

            self.spanPanel()

            if time.time() > self.timeout:
                break

    def greetChats(self):

        pass


class Chat:

    def __ini__(self, driver_chat):

        self.driver_chat=driver_chat
        
    def chatName(self):

        name_chat=self.driver_chat.split("\n")[0]

        return name_chat

    def readMsgs(self):

        chat_msgs=[]
        htmlcode=(driver.page_source).encode('utf-8')
        soup = BeautifulSoup(htmlcode,features="html.parser")
            for tag in soup.find_all('div', class_="_1ij5F"):
            persona=tag.find_all("div", class_="_2XJpe")
            if persona:
                name_persona=persona[0].find_all("div", class_="copyable-text")
                if name_persona:
                    name_msg=(name_persona[0].get_attribute_list("data-pre-plain-text"))
                    name_msg=name_msg[0].split("]")[1]
                    time_msg=name_msg[0].split("]")[0]
                    text_msg=(name_persona[0].text)
                    chat_msgs.append((name_msg, time_msg, text_msg))

        return chat_msgs