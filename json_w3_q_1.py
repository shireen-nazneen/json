#If you have a JSON string, you can parse it by using the json.loads() method.
import json
x={ "name":"John","age":30,"city":"New York"}
with open("w3_q1.json","w")as y:
    json.dump(x,y)
with open("w3_q1.json","r")as y:
    a=json.load(y)
    print(type(a))

    
