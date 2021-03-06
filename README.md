# whatsAppGreeting

The idea is based on capturing words or phrases of the whastApp web chat and responding to them. Once the application is executed, it will go through the chats, verifying if there was a message on the day where the phrase or word being searched is found. If it finds it, it responds with the indicated greeting (If the greeting has already been made, it will not do it again).

Based on python3, selenium, and BeautifulSoup

## Install requierements
```python
pip install -r requirements/requirements.txt
```
## install ChromeDriver - WebDriver for Chrome

Download the lastest release for your platform:

https://chromedriver.storage.googleapis.com/index.html?path=88.0.4324.96/

### For linux
```bash
cd ~/Downloads/
```

```bash
unzip chromedriver_linux64
```

```bash
mv chromedriver_linux64 /usr/local/bin
```

## Usage
```python
python3 main.py -c capture.txt -r "respond to send"
```
Put the words/phrase that you want to respond in a file (See example file in example/capture.txt). The words/phrase that you want to respond should be one by line. The capture isn't case sensitive, so dont worry aboyt the case:

![](https://github.com/AgustinPardo/whatsAppGreeting/blob/main/example/capture.png)

## Create binaries for Linux
```bash
bash binary/binary.sh
```

In the binary folder you will have the binary of the app called "main" ready to run

## Use cron to set the auto running in Linux

Run:
```bash
crontab -e
```

Add the next line to the end of the file:

```bash
0 20 * * * dt=$(date '+%d/%m/%Y %H:%M:%S'); echo "$dt" >> /home/user/whatsAppGreeting/config/cronLog/log.log; python3 /home/user/whatsAppGreeting/app/main.py -h >> /home/user/whatsAppGreeting/config/cronLog/log.log
```

This is set up to run every day at 20 hs. You can set up diferent time chaning 0 20 * * * cron time schedule.


