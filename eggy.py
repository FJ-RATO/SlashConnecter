import discord
from discord.ext import commands, tasks
from discord_slash import SlashCommand, SlashContext

import json

def read(): #le os status do ovo
    file = open("./egg.json", "r")
    egg = json.load(file)
    file.close()
    return egg

def write(egg): #escreve os status do roler
    file= open("./egg.json", "w")
    json.dump(egg,file)
    file.close()

@tasks.loop(seconds = 60) #loop de jogo
async def play(client): 
    egg = read()
    egg["heat"] -= 1 #pontos decrementados a cada loop
    write(egg)
    temp = egg["heat"]

    if temp <= 0: #check para aleterar a gamepresence
        await client.change_presence(activity=discord.Game(name="egg is dead"))
    else:
        text = "egg is at " + str(temp) +"º"
        await client.change_presence(activity=discord.Game(name= text))
    
def heat(): #função de incremento de pontos
    egg = read()
    egg["heat"] += 1
    write(egg)

def revive(): #função de resurrect  
    egg = read()
    egg["heat"] = 100
    write(egg)
