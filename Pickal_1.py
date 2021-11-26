from  bs4 import BeautifulSoup
import requests
import json
# def task1_pickles():
url="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471"
page=requests.get(url)
soup=BeautifulSoup(page.text,"html.parser")
div1=soup.find("div",class_="_1EI9").span.get_text()
def web_pical():
    web_pical="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471"
    web=requests.get(web_pical)
    web1=BeautifulSoup(web.text,"html.parser")
    main_div=web1.find("div",class_="_3RA-")
# print(main_div)
    div=main_div.find_all("div",class_="UGUY")
# print(div)
    pickle_price=main_div.find_all("div",class_="_1kMS")
    link=main_div.find_all("div",class_="_3WhJ")
    i=0
    list=[]
    possition=0
    while i <len(link):
        possition+=1
        pickle_name=link[i].get_text()
        # pickle_name=div[i].get_text()
        price=pickle_price[i].span.get_text()
        # pickle_url="https://paytmmall.com"+link[i].a["herf"]
        link_1=(link[i].a["href"])
        pickle_url="https://paytmmall.com"+link_1
        # print(pickle_url)
        # link_1=(link[i].a["href"]).strip()
        dict={"possition1":possition,"pickle_names":pickle_name,"pickle":price,"link_name":pickle_url}
        # dict["possition"]=i
        list.append(dict)
        i=i+1
    with open("p.json","w") as file:
        json.dump(list,file,indent=5)
    return list   
web_pical()


