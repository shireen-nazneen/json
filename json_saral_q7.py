# convert text deta ko json deta me convert karo
import json
a=open("file.txt","w")
a.write(" Name Abhishek \n Designation  CEO of  navgurukul \n Gender male \n Age 29")
a.close()
a=open("file.txt","r")
a1=a.read()
b=a1.split("\n")
dict1={}
for i in b:
    i.split()
    c=i.split()
    if len(c)==2:
        dict1[c[0]]=c[1]
    if len(c)>2:
        j=1
        k=" "
        while j<len(c):
            k+=c[j]
            j+=1
            k+=" "
        dict1[c[0]]=k
print(dict1)
a.close()
c=open("json_saral_q7.json","w")
json.dump(dict1,c)
