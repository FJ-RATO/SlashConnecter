import json
#recebe um file no estilo numero1\n numero2\n numero3\n
#trnasforma num json no estilo {numero1:false} {numero2:false} {numero3:false}

f = open("whitelist.txt","r")
dic = dict()

for x in f:
    x = x.replace('\n', '') #retira os /n
    dic[x] = False #adiciona o valor false 
f.close()

f= open("whitelist.json","w")
json.dump(dic, f)
f.close()