# whatsAppGreeting

The idea is based on capturing words or phrases of the whastApp web chat and responding to them. Once the application is executed, it will go through the chats, verifying if there was a message on the day where the phrase or word being searched is found. If it finds it, it responds with the indicated greeting (If the greeting has already been made, it will not do it again).

Based on python3, selenium, and BeautifulSoup

## Install requierements

pip install -r requirements/requirements.txt

## install ChromeDriver - WebDriver for Chrome

Download the lastest release for your platform:

https://chromedriver.storage.googleapis.com/index.html?path=88.0.4324.96/

For linux: Unzip and copy the chromedriver file in /usr/local/bin directory

Put the words/phrase that you want to respond in a file (See example file in example/capture.txt). They should be one by line.

## Usage

python3 main.py -c capture.txt -r "respond to send"