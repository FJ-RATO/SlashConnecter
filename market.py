import json
import nextcord
import random
from nextcord.ext import commands,tasks
from os.path import exists

#checks if the player is already registerd if not registers
async def register(ctx):
    path = "./save/"+str(ctx.author.id)
    if(exists(path)):
        await ctx.author.send("O teu id já existe na nossa base de dados.")
    else:
        file=open(path,"w")
        body ={
            "name":ctx.author.name,
            "status": "ok",
            "money": 0,
            "neectcoin": 0,#crypto
            "miners":0,#for myning crypto
            "botes": 0,#stock B
            "doggos": 0,#stock C
            "weebs":0,#stock D
            "inventory":[]
        }
        json.dump(body, file)
        file.close()
        await ctx.author.send(embed=status(ctx))

def init():
    pass


async def _status(ctx):
    ctx.author.send(embed=status(ctx))

def status(ctx):
    status = read(ctx)
    embed=nextcord.Embed(title=status["name"], description="Status da tua conta", color=0x00ff00)
    embed.add_field(name="money", value=status["money"], inline=False)
    embed.add_field(name="status", value=status["status"], inline=False)
    embed.add_field(name="neectcoin", value=status["neectcoin"], inline=False)
    embed.add_field(name="miners", value=status["miners"], inline=False)
    embed.add_field(name="botes", value=status["botes"], inline=False)
    embed.add_field(name="doggos", value=status["doggos"], inline=False)
    embed.add_field(name="weebs", value=status["weebs"], inline=False)
    embed.add_field(name="inventory", value=status["inventory"], inline=False)
    return embed    
    
def read(ctx): #le os status do ovo
    try:
        file = open("./save/"+str(ctx.author.id), "r")
    except:
        print(str(ctx.author.name)+" user file not found")
    status = json.load(file)
    file.close()
    return status

#every 24h
#update the stocks
#checks the electric bills
BOTES_PRICE = 99999
DOGGOS_PRICE = 99999
WEEBS_PRICE = 99999
STATE = 9

@tasks.loop(hours=24)
def loop24():
    STATE = random.randrange(1,3)
    # BOTES HIGH RISK HIGH REWARD
    # DOGGOS LOW PRICE STABLE
    # WEEBS HIGH PRICE ALWAYS NOT SO STABLE
    if(STATE == 1):
        BOTES_PRICE = random.randrange(10,3000) 
        DOGGOS_PRICE = random.randrange(100,300) 
        WEEBS_PRICE = random.randrange(5000,6000) 
    if(STATE == 2):
        BOTES_PRICE = random.randrange(10,300) 
        DOGGOS_PRICE = random.randrange(50,300) 
        WEEBS_PRICE = random.randrange(5000,8000) 
    if(STATE == 3):
        BOTES_PRICE = random.randrange(1,3) 
        DOGGOS_PRICE = random.randrange(200,450) 
        WEEBS_PRICE = random.randrange(5000,10000) 
    NEECTCOIN_PRICE = (WEEBS_PRICE/STATE - (BOTES_PRICE + DOGGOS_PRICE)*STATE)
#every 1h
#update crypto price
@tasks.loop(hours=1)
def loop1():
    NEECTCOIN_PRICE = random.randrange(int(NEECTCOIN_PRICE*0.05),int(NEECTCOIN_PRICE*0.3))