#Python dictionary(sort by key) object and  excess uniqe value
import json
a={
 "a":  1,
 "a":  2,
 "a":  3, 
 "a": 4,   
 "b": 1, 
 "b": 2
}
with open("json_saral_q5.json","w")as dic:
    dic=json.dump(a,dic)




