#write thhe dictnorry with keys and value and convert it
import json
a=[
    ["neelam","programer","24","2400"],
    ["komal","trainer","24","20000"],
    ["anuradha","HR","25","40000"],
    ["Abhishek","manager","29","63000"] 
    ]
number_of_empl=["empl1","empl2","empl3","empl4"]
list_q=["neme","designations",'age',"salary"]
list1=[]
dict2={}
for i in a:
    j=0
    dict1={}
    while j<len(i):
        dict1[list_q[j]]=i[j]
        j+=1
    list1.append(dict1)
for k in list1:
    for j in number_of_empl:
        dict2[j]=k
print(dict2)
with open("json_saral_q8.json","w")as b:
    json.dump(dict2,b,indent=6)

