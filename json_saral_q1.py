import json
a={"Name":"Ram", 
     "Class":"IV", 
     "Age":9 }
with open("json_saral_q1.json","w",)as  b:
    json.dump(a,b,indent=6)
with open("json_saral_q1.json","r")as b:
    x=json.load(b)
    print(x)


 