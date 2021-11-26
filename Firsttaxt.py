from  bs4 import BeautifulSoup
import requests
import json
def task1():
    url="https://www.imdb.com/india/top-rated-indian-movies/"
    page=requests.get(url)
    # print(page)
    soup=BeautifulSoup(page.text,"html.parser")
    # html ka code(soup ,me)
    # list1=[]
    main=soup.find("div",class_="lister")
    main1=main.find("tbody",class_="lister-list")
    trs=main1.find_all("tr")

    list1=[]
    a=1
    for i in trs:
        position=i.find('style',Class_="position:relative")
        movie_name=i.find("td",class_="titleColumn").a.get_text()
        name=movie_name
        release_year=i.find("td",class_="titleColumn").span.get_text()[1:5]
        year=int(release_year)
        mov=i.find("td",class_="ratingColumn imdbRating").strong.get_text()
        movie_rate=float(mov)
        y=i.find("td",class_="posterColumn").a["href"]
        link="https://www.imdb.com"+y
        url=link
        k={"position":a,"movie_name":name,"year":year,"IMDb_Rating":movie_rate,"url":url}
        list1.append(k)
        a+=1
    with open("file.json","w") as open_file:
        json.dump(list1,open_file,indent=4)
    return list1
(task1())






# soup=BeautifulSoup(page.text,'html.parser')
# def sc
# ap_top_list():
    # main_div=soup.find('today',Class='lister')
    # today=main_div.find('today',Class='lister'-list)
    # trs=today.find_all('tr')
# 
    # movie_ranks=[]
    # movie_name=[]
    # year_of_realease=[]
    # movie_urls=[]
    # movie_ratings=[]
    # 
    # for tr in trs:
        # position=tr.find('td',Class="titeCoumn").get_text().st
        # rank=''
        # for i in position:
            # if '.' not in i:
                # rank=rank+i
            # else:
                # break
        # movie_ranks.append(rank)