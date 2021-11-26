from  bs4 import BeautifulSoup
import requests
import json
def tk_5():
  url="https://en.wikipedia.org/wiki/Python_(programming_language)"
  page5=requests.get(url)
  soup=BeautifulSoup(page5.text,"html.parser")
  soup1=soup.find("table",class_="infobox vevent")
  m=soup1.find_all("th",class_="infobox-label")
  # print(m)
  list=[]
  dict={}
  for i in m:
    a=i.get_text()
    print(i)
    # list.append(a)
    # print(list)
    # dict.update([list])
    # with open("shra.json","w+") as file:
    #   json.dump(dict,file,indent=6)
  # return dict    
tk_5()
