import bs4
from urllib.request import urlopen as uReq
from win10toast import ToastNotifier
from bs4 import BeautifulSoup as soup
toaster = ToastNotifier()
my_url="https://thehackernews.com"
try:
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html,"html.parser")
    containers = page_soup.findAll("div",{"class":"img-ratio"})
    toaster.show_toast("The Hacker News",containers[0].img["alt"],icon_path="favicon.ico")
    pass
except Exception as e:
    raise 
