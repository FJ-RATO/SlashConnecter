import nextcord
from nextcord.ext import application_checks

import json

def read(): 
    file = open("./caderno.json", "r")
    caderno = json.load(file)
    file.close()
    return caderno

def write(caderno): 
    file= open("./caderno.json", "w")
    json.dump(caderno,file)
    file.close()
    
def add(amount): 
    caderno = read()
    total = caderno["marcas"] + int(amount)
    caderno["marcas"] += int(amount)
    write(caderno)
    return total

def sub(amount): 
    caderno = read()
    total = caderno["marcas"] - int(amount)
    if total < 0:
        caderno["marcas"] = 0
        write(caderno)
        return 0
    else:
        caderno["marcas"] = total
        write(caderno)
        return total

async def caderno(ctx,command,amount):
    if command.upper() == "ADD":
        total = add(amount)
        await ctx.send(f"Caderno updated, agora tem {total} traços",ephemeral= True)
    elif command.upper() == "SUB":
        total = sub(amount)
        await ctx.send(f"Caderno updated, agora tem {total} traços",ephemeral= True)
    else:
        await ctx.send(f"Wrong argumnet, the valid arguments are ADD or SUB (in any case)",ephemeral= True)