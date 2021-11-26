from Firsttaxt import task1
# list=task1()
import pprint
list_1=task1()
import json
def droup_decode(movies):
    list_1=[]
    for i in movies:
        # print(i)movie ka data yani task2 movies pr loop chlane ka kam
        mod=i["year"]%10
        # mod ki velue 3 kiyoki remainder 3 hai
        dec=i["year"]-mod
        # koi v dec list1 k under repet nahi hoga isliye not in ka use..
        if dec not in list_1:
            list_1.append(dec)
    list_1.sort()
    movies_dec={}
    # key keieat dec me list chalane k bad year key bna or khali list
    for i in list_1:
        # dic pr loop chalaya or jo v movie ki detel bani hai uske liye
        movies_list=[]
        for   x in movies:
            # task2 pr loop chalaya
            if x["year"]>=i and x["year"]<=i+10:
                # taxk2 ki jab key aai tab sampair kiya ki x bda hai ya =hai fir x chota hai ya =
                movies_list.append(x)
                movies_dec[i]=movies_list
                # print(movies_list)
    #             with open("movies_dec.json","w")as f:
    #                 json.dump(movies_dec,f,indent=5)
    # return movies_dec
droup_decode(list_1)





























# def group_year(movies):
    # moviedec={}
    # years=[]
    # list1=[]
    # for i in movies:
        # print(i)(movie ka data)
        # mod=i["year"]%10
        # decode=i["year"]-mod
        # if decode not in list1:
            # print(decode)
            # list1.append(decode)
            # p/rint(list1)
    # list1.sort()
    # print(list1)() year)
    # for i in list1:
        # moviedec[i]=[]
        # print(moviedec)
        # print(moviedec)=dic k ander year and kha
        # for i in moviedec:
            # dec10=i+9
            # for x in movies:
                # print(x)
                # if x <=dec10 and x >=i:
                    # print(x)
                # for v in movies[x]:
                    # movies1[i].append(v)
                    # print(v)
    # with open("3task.json","w") as file:
        # json.dump(movies1,file,indent=4)        
    # return(movies1)
# group_year(list)
# 
# 


















# def droup_decode():
    # movies_dec={}
    # list_of_dec=[]
    # for year in movies_year:
        # mod=year%10
        # print(year)
        # dec=year-mod
        # if dec not in list_of_dec:
            # list_of_dec.append(dec)
            # print(list_of_dec)






































# def group_year(movies):
    # moviedec={}
    # years=[]
    # list1=[]
    # for i in movies:
        # print(i)(movie ka data)
        # mod=i["year"]%10
        # decode=i["year"]-mod
        # if decode not in list1:
            # print(decode)
            # list1.append(decode)
            # p/rint(list1)
    # list1.sort()
    # print(list1)() year)
    # for i in list1:
        # moviedec[i]=[]
        # print(moviedec)
        # print(moviedec)=dic k ander year and khali list
        # for i in moviedec:
            # dec10=i+9
            # for x in movies:
                # print(x)
                # if x <=dec10 and x >=i:
                    # print(x)
                # for v in movies[x]:
                    # movies1[i].append(v)
                    # print(v)
    # with open("3task.json","w") as file:
        # json.dump(movies1,file,indent=4)                
    # return(movies1)
# group_year(list)
# 
# 
























# for i in list1:
    # print(list1)
    # movies1[i]=[]
# for i in movies1:
    # dec10=i+9
    # print(i)
    # for x in movies:
        # 
        # if x<=i["year"] and x>=i["y
            # for v in movies[x]:
                # movies1[i].append(v
                # print(v)
# with open("3task.json","w") as file
    # json.dump(movies1,file,indent=4
# return(movies1)
# group_year(list)