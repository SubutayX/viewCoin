from colorama import Fore, Back, Style
from bs4 import BeautifulSoup
import requests
import time
import datetime
import os

if os.name  == "nt":
    os.system("cls")
else:
    os.system("clear")

end = '\033[0m'
count = 0
while count != 100:

    try:

        responseBTC = requests.get("https://www.trbinance.com/trade/BTC_TRY").content
        responseETH = requests.get("https://www.trbinance.com/trade/ETH_TRY").content
    except:
        print("Bağlantı sorunu ")
        break
    
    soupBTC = BeautifulSoup(responseBTC, "html.parser")
    soupETH = BeautifulSoup(responseETH, "html.parser")    
    
    textBTC = soupBTC.find("div",{"class":"latest-price"}).find("span").text
    textETH = soupETH.find("div",{"class":"latest-price"}).find("span").text    
    
    
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    count += 1
    print(f"{count}: BTC: {Fore.GREEN + textBTC.ljust(10) + end}",end="")
    print(f" ETH: {Fore.GREEN + textETH.ljust(10) + end}  {hour}:{minute}")
