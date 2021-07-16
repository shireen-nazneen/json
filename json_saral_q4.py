import json
a={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4} 
dic={}
s=sorted(a.keys())   
print(s)
for i in s:
    for k in a:
        dic.update({i:a[i]})
with open("json_saral_q4.json","w")as json_file:
    json_file=json.dump(dic,json_file)
with open("json_saral_q4.json","r")as json_file:
    json_file=json.load(json_file)
    print(json_file)


j=1
while j<=4:
    i=1
    n=65
    while i<=4:
        if j==1 and i==3:
            print(chr(n),end=" ")
        i+=1
    print()
    j+=1
    n+=1