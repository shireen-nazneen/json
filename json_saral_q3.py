import json
dic={"a":"1","b":"2","c":"3","d":"4"}
with  open("json_sarl_q3.json","w")as json_file:
    json_file=json.dump(dic,json_file,indent=3)
with open("json_sarl_q3.json","r")as json_file:
    b=json.load(json_file)
    print(b)
