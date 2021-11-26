from  bs4 import BeautifulSoup
import requests
import json
def ek():
    url="https://webscraper.io/test-sites"
    page=requests.get(url)
    soup=BeautifulSoup(page.text,"html.parser")
    main=soup.find("div",class_="container test-sites")
    main1=main.find_all("div",class_="col-md-7 pull-right")
    list=[]
    possion=0
    for i in main1:
        possion+=1
        name1=i.find("h2",class_="site-heading").a.get_text().strip()
        link=i.find("h2",class_="site-heading").a["href"]
        link2="https://webscraper.io/test-sites"+link
        possion+=1
        d={"possion1":possion,"name":name1,"link1":link2}
        list.append(d)
    with open("kumari.json","w") as open_file:
        json.dump(list,open_file,indent=4)

    return list
# ek()
