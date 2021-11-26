import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json
url="https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/"
top_movi_api=requests.get(url)
soup=BeautifulSoup(top_movi_api.text,"html.parser")
# print(soup)
div=soup.find("table",class_="table")
trs=div.find_all("tr")
movie_no=[]
for i in trs:
    main=i.find_all("td",class_="bold")
    # print(main)first possition k liye
    for j in main:
        rank=j.get_text()
        movie_no.append(rank)
        # print(movie_no)
    movie_reating=[]
    for k in main:
        reating=i.find("span",class_="tMeterScore").get_text().strip()
        movie_reating.append(reating)
    movie_name1=[]
    for l in main:
        movie_name2=i.find("a",class_="unstyled articleLink").get_text()
        movie_name1.append(movie_name2)
        # print(movie_name1)
    top_movies=[]
    for n in main:
        movie_name=i.find("a",class_="unstyled articleLink").get_text().strip()
        movie_year=movie_name.split()
        year=movie_year[-1][1:5]
        # string ko htane k liye [-1][1:5] ka used kiya gya
        top_movies.append(year)
    reviews=[]
    for x in main:
        reviews1=i.find("td",class_="right hidden-xs").get_text()
        reviews.append(reviews1)
    movie=[]
    for m in main:
        movie_url=i.find("a",class_="unstyled articleLink")["href"]
        movie_link="https://www.rottentomatoes.com/"+ movie_url
        deaitals={"possition":rank,"Reating":reating,"movies_name1":movie_name,"movies_year":year,"reviews3":reviews1,"Likn":movie_link}
        movie_no.append(deaitals)
        # print(movie_no)
        with open("movies.json","w")as f:
            json.dump(movie_no,f,indent=4)



# def scrap_movi_details():
#     url="https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/"
#     page=requests.get(url)
#     soup=BeautifulSoup(page.content,"html.parser")
#     main=soup.find("table",class_="table")
#     trs=main.find_all("tr")
#     list=[]
#     # possition=0
#     for i in trs:
#         Rank=i.find("td",class_="bold")
        # rating=i.find("span",class_="tMeterScore")
        # movi_name=i.find("a",class_="unstyled articleLink")
        # link=i.find("a",class_="unstyled articleLink")
        

# scrap_movi_details()



















# rating=i.find("span",class_="tMeterScore")
        # movi_name=i.find("a",class_="unstyled articleLink")
        # link=i.find("a",class_="unstyled articleLink")
        