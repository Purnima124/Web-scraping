mport json
# from fist_task import adventure_movie
# import json
# name=adventure_movie()
# def group_by_year(movise):
#     years=[]
#     for i in movise:
#         year=i["year"]
#         if year not in years:
#             years.append(year)
#     movise_dict={i:[]for i in years}
#     print(movise_dict)        

from Firsttaxt import task1()
khushboo=task1()
import json
def group_of_year(movise):
    years=[]
    for i in movise:
        # print(i)
        # year=i["year_of release"]
        if i["Year"] not in years:
            years.append(i['Year'])
    # print(years)
    movise_dict={i:[]for i in years}
    for i in movise:
        # name=1
        year=i["Year"]
        for x in movise_dict:
            if (x)==(year):
                movise_dict[x].append(i)
                # movise_dict[x].append(i)
                with open("khusboo.json","w")as file:
                    json.dump(movise_dict,file,indent=3)
                print(movise_dict)    

    return(movise_dict)
print(group_of_year(khushboo))