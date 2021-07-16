import json


dict1_itimes={
    "shopping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 

}
with open("json_saral_q9.json","w")as jsonfile:
    json.dump(dict1_itimes,jsonfile)
with open("json_saral_q9.json","r")as jsonfile:
    c=json.load(jsonfile)
    print(c)
for i in c.values():
    for j in i:
        print(j)
    user=input("what you want???-")
    if user in i:
        user1=int(input("how many items you want??-"))
        for k in i.values():
            k=int(k)
            if user1<=k:
                a=k-user1
                a=str(a)
                dict1_itimes["shopping_list"][user]=a
                break
            elif user1>k:
                k=int(k)
                a=user1-k
                a=a+k
                c=a-a
                c=str(c)
                dict1_itimes["shopping_list"][user]=c
                break
    else:
        print("not avaleble")
with open("json_saral_q9.json","w")as s:
    json.dump(dict1_itimes,s)
    print(type(s))
with open("json_saral_q9.json","r")as s:
    s=json.load(s)
    print(type(s))

