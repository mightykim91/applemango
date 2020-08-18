# -*- coding: utf-8 -*- 
res = [['https://scontent-ssn1-1.cdninstagram.com/v/t51.2885-15/e35/117839959_2589252991385145_9156213434913585787_n.jpg?_nc_ht=scontent-ssn1-1.cdninstagram.com&_nc_cat=109&_nc_ohc=JIs9FodRnIEAX_SeJj1&oh=f6da5a1e7b2ed316d8899ee6e2b08640&oe=5F63C584', '짜장면'], ['https://scontent-ssn1-1.cdninstagram.com/v/t51.2885-15/e35/117414873_335406607494768_4708920457310828297_n.jpg?_nc_ht=scontent-ssn1-1.cdninstagram.com&_nc_cat=100&_nc_ohc=xaR7-sJiSeYAX_VgSDX&oh=8d835d471b5b8d6154addc15ae0f8262&oe=5F64023F', '짜장면'], ['https://scontent-ssn1-1.cdninstagram.com/v/t51.2885-15/e35/117665068_642844309668828_7077740974176388789_n.jpg?_nc_ht=scontent-ssn1-1.cdninstagram.com&_nc_cat=100&_nc_ohc=pTvfCRq1okUAX9f3mOV&oh=d092d2772ccaf8b68aab0ac7d3bc8140&oe=5F630BB0', '짜장면'], ['https://scontent-ssn1-1.cdninstagram.com/v/t51.2885-15/e35/s1080x1080/117408317_637350880542459_8259403870692513365_n.jpg?_nc_ht=scontent-ssn1-1.cdninstagram.com&_nc_cat=103&_nc_ohc=RY2E0K5GUNkAX_Ajljg&oh=7f3a7601eca4cea524368d1d1d790baf&oe=5F643363', '짜장면']]
file_data = []
# data = {
#         "irid" : "",
#         "rname" : "",
#         "rbranch" : "", # 지점명은 일단 비워두자
#         "instaid" : "",
#         "iurl" : "",
#         "ifood": "",
#         "likes" : "",
#         "idate" : "",
#     }
irid = 1
en_name = 'afsagsdf'
account = 'asdasd'
for food_info in res:
    # print("##########################################################################")
    # print("food_info ==>", food_info)
    data = {
        "irid" : "",
        "rname" : "",
        "rbranch" : "", # 지점명은 일단 비워두자
        "instaid" : "",
        "iurl" : "",
        "ifood": "",
        "likes" : "",
        "idate" : "",
    }
    
    img_url = food_info[0]
    food = food_info[1]
    data["irid"] = irid
    data["rname"] = en_name 
    data["instaid"] = account
    data["iurl"] = img_url
    data["ifood"] = food
    # data["likes"] = int(likes)
    # data["idate"] = my_date.isoformat()
    file_data.append(data)
print(file_data)