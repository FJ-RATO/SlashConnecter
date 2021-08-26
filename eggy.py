import discord
from discord.ext import commands, tasks
from discord_slash import SlashCommand, SlashContext

import json

def read():
    file = open("./egg.json", "r")
    egg = json.load(file)
    file.close()
    return egg

def write(egg):
    file= open("./egg.json", "w")
    json.dump(egg,file)
    file.close()

@tasks.loop(seconds = 10)
async def play(client):
    egg = read()
    egg["heat"] -= 10
    write(egg)
    temp = egg["heat"]

    if temp <= 0:
        await client.change_presence(activity=discord.Game(name="egg is dead"))
    else:
        text = "egg is at " + str(temp) +"º"
        await client.change_presence(activity=discord.Game(name= text))
    
def rub():
    egg = read()
    egg["heat"] += 10
    write(egg)

def revive():
    egg = read()
    egg["heat"] = 100
    write(egg)
