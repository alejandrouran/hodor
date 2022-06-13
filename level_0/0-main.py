#!/usr/bin/python3

import requests

from bs4 import BeautifulSoup

url = "http://158.69.76.135/level0.php"
resp = requests.get(url)
soup = BeautifulSoup(resp.text, "html.parser")
inputs = soup.find_all("input")
data = {
        "id": "4530",
        "holdthedoor": "submit"
}
bot = requests.post(url, data=data)
soup = BeautifulSoup(bot.text, "html.parser")
print(bot.status_code)
