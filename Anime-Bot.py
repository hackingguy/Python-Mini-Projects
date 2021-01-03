import sys,os
import urllib.request
import bs4
from bs4 import BeautifulSoup as soup
import html
try:
    from selenium import webdriver
except:
    SELINIUM_CHECK=1
import time


BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'
