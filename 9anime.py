import urllib.request
import bs4
from bs4 import BeautifulSoup as soup
import html
from selenium import webdriver

my_url = input('Enter The URL:')
Format = input('Type Of File:')
Element = input('Element to be Scrapped:')
check = ''
AttributeRequired = input("Attribute Required[y/N]")
if(AttributeRequired == 'y'):
    Attribute = input('Attribute to be Scrapped:')
    Key = input('Key Of Attribute to be Scrapped:')
    
Property = input("Any Specific Property Needed[Y/n]:")


if(Property!='n'):
    check = input("Is It a Link(Y/n):")
    name = input("Enter The Name Of Property:")
    
    
    
Header_Check = input('Do You Wanna Use Custom Headers[y/N]')
if(Header_Check=='y'):
    hdr = {'User-Agent':input("Input Headers:")}
else:
    hdr = { 'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0' }
req = urllib.request.Request(my_url, headers=hdr)
response = urllib.request.urlopen(req, timeout=4)
print(response)
page_html = response.read()
page_soup = soup(page_html,Format)
if(AttributeRequired == 'y'):
    containers = page_soup.findAll(Element,{Attribute:Key})
else:
    containers = page_soup.findAll(Element)

if(check=='n'):
    k = open("9anime.txt","w+")
    for i in range(0,len(containers)):
        try:
            k.write(str(containers[i][name])+"\n")
        except:
            print("1")
    k.close()
    print('Saved In the File')
else:
    string=''
    str1="https:"
    for i in range(0,len(containers)):
        try:
            string=str1+html.unescape(containers[i][name])
            driver = webdriver.Chrome()
            driver.get(string)
            print(string)
        except:
            print("1")
    