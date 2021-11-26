from Firsttaxt import task1
from bs4 import BeautifulSoup
import requests
def task4():
    url="https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/"
    page=requests.get(url)
    soup=BeautifulSoup(page.text,"html.parser")
    print(soup)


task4()