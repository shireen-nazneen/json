import json
dict1={
      "name": "David",
     "class":"I",
     "age": 6  
 }
with open("json_saral_q2.json","w")as a: 
    json.dump(dict1,a,indent=6)
with open("json_saral_q2.json","r")as a:
    b=json.load(a)
    print(b)
import json
list_of_empl=[
    ["neelam","programer","24","2400"],
    ["komal","trainer","24","20000"],
    ["anuradha","HR","25","40000"],
    ["Abhishek","manager","29","63000"] 
    ]
number_of_empl=["empl1","empl2","empl3","empl4"]
print(number_of_empl)
dic={}
for i in list_of_empl:
    for j in number_of_empl:
        s=" "
        for k in i:
            s=s+k
            s=s+" "
            dic.update({j:{s}}) 
print(dic)
with  open("json_saral_q8.json","w") as json_file:
    json.dump(dic,json_file,indent=3)

