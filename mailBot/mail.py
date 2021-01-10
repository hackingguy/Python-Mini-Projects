from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from sys import platform
import html
import time
import re

NULL_PATH=""

if(platform=="win32"):
    NULL_PATH="nul"
else:
    NULL_PATH="/dev/null"

options = webdriver.ChromeOptions();
options.add_argument('--log-level=3')
#options.add_argument('--headless')
options.add_argument("--ignore-ssl-errors")
options.add_argument("--ignore-certificate-error")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options,service_log_path=NULL_PATH)


def getMail():
    driver.get("https://gmailnator.com")
    print("Waiting for a mail ID......")
    mail=driver.find_element_by_tag_name("input").get_attribute('value')
    while('com' not in mail):
        time.sleep(5)
        mail=driver.find_element_by_tag_name("input").get_attribute('value')
    return mail

def getScreenshot(url):
    print("Got A Mail.....")
    driver.get(url)
    time.sleep(5)
    data = driver.find_element_by_id("content").get_attribute("innerHTML")
    s1 = html.unescape(re.sub(r'<.*?>', '', data).strip())
    s = html.unescape(s1)
    print(s)
    while('\n\n' in s):
        s = s.replace('\n\n','\n')
    print(s.replace('\xc2\xa0'," "))
    driver.quit()

def checkInbox(email):
    num=0
    flag=0
    container=""
    while(len(container)==0):
        if(flag==1):
            time.sleep(2)
        driver.get("https://gmailnator.com/inbox/#"+email)
        time.sleep(2)
        container = driver.find_elements_by_xpath("//tr//td//a")
        flag=1
    getScreenshot(container[0].find_elements_by_xpath("//tr//td//a")[0].get_attribute("href"))
    pass

try:
    email = getMail()
    print("Got Mail ID: {}".format(email))
    checkInbox(email)
except:
    print("Interrupt Recieved")
finally:
    driver.quit()