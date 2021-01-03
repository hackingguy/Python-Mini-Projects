#!/usr/bin/env python3
import requests
from win10toast import ToastNotifier
import time


toaster = ToastNotifier()
req = requests.session()

login_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '74',
    'Origin': 'https://10.10.11.1:8090',
    'DNT': '1',
    'Connection': 'close',
    'Referer': 'https://10.10.11.1:8090/httpclient.html'
}

live_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'DNT': '1',
    'Connection': 'close',
    'Referer': 'https://10.10.11.1:8090/httpclient.html'
}

json_data = {
    'mode': '191', 'username': '18104005', 'password': '18104005', 'a': '1578496066016', 'producttype': '0'
}


def login(username, pwd):
    json_data["a"] = int(round(time.time() * 1000))
    r = req.post("https://10.10.11.1:8090/login.xml", json_data, headers=login_headers, verify=False)
    response = r.content
    if (b"signed" in response):
        toaster.show_toast("Login Successful", "You Are Sucessfully Logged In")


def live_mode():
    while (True):
        time.sleep(120)
        url = "https://10.10.11.1:8090/live?mode=192&username=18104005&a=" + str(
            int(round(time.time() * 1000))) + "&producttype=0"
        r = req.get(url, headers=live_headers, verify=False)
    pass


login("18104005", "18104005")
live_mode()
