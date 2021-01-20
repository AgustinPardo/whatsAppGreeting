import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

# ChromeOptions allows us use the userdata of chrome 
# so that you don't have to sign in manually everytime. 
chropt = webdriver.ChromeOptions() 
  
# adding userdata argument to ChromeOptions object 
chropt.add_argument("user-data-dir=/home/agustin/.config/google-chrome/prueba2") 
  
# Creating a Chrome webdriver object 
driver = webdriver.Chrome(options = chropt)
try:
    driver.get("https://web.whatsapp.com/") 
except:
    driver.close()

# delay added to give time for all elements to load 
time.sleep(7) 

# Buscar cada chat
chats=driver.find_elements_by_class_name("_1MZWu")
panel = driver.find_element_by_class_name('_3Xjbn')

timeout=time.time()+10 # 5 segundos

a=0
name_chats=[]
chat_msg={}
while True:
    for i in chats:
        #print(i.text.split("\n")[0])
        i.click()
        name_chat=i.text.split("\n")[0]
        name_chats.append(name_chat)

        htmlcode=(driver.page_source).encode('utf-8')
        soup = BeautifulSoup(htmlcode,features="html.parser")
        take=False
        msg=[]
        for tag in soup.find_all('span'):
            classid=tag.get('class')
            if classid!=None and len(classid)>0 and classid[0]== "_1VzZY" and tag.text=="HOY":
                take=True
            if take and classid!=None and len(classid)>0 and classid[0]== "_1VzZY" and tag.text!="HOY" :
                msg.append(tag.text)
                if tag.text == "Pebete":
                    string='En que andas?'
                    input_box=driver.find_element_by_class_name('DuUXI')
                    input_box.send_keys(string+Keys.ENTER)

        chat_msg[name_chat]=msg

    a += 1200

    driver.execute_script('arguments[0].scrollTop = %s' %a, panel)
    time.sleep(1)

    chats=driver.find_elements_by_class_name("_1MZWu")

    if time.time() > timeout:
        break


driver.close()



# for i in chats[1:15]:
#     #print(i.text.split("\n")[0])
#     i.click()
#     name_chat=i.text.split("\n")[0]
#     name_chats.append(name_chat)

#     htmlcode=(driver.page_source).encode('utf-8')
#     soup = BeautifulSoup(htmlcode,features="html.parser")
#     take=False
#     msg=[]
#     for tag in soup.find_all('div', class_="_1ij5F"):
#             persona=tag.find_all("div", class_="_2XJpe")
#             if persona:
#                 name_persona=persona[0].find_all("div", class_="copyable-text")
#                 if name_persona:
#                     print(name_persona[0].get_attribute_list("data-pre-plain-text"))
#                     print(name_persona[0].text)

