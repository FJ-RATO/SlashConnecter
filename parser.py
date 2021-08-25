import json

f = open("whitelist.txt","r")
dic = dict()

for x in f:
    x = x.replace('\n', '')
    dic[x] = False
f.close()

f= open("whitelist.json","w")
json.dump(dic, f)
f.close()