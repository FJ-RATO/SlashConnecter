import discord
from discord_slash import SlashCommand, SlashContext,ComponentContext
from discord_slash.utils.manage_commands import create_choice, create_option
from discord_slash.utils.manage_components import create_select, create_select_option, create_actionrow

from secret import code as code
from secret import servers as servers

import autoroler

client = discord.Client(intents = discord.Intents.all())
slash = SlashCommand(client, sync_commands=True)

guild_id = servers

@client.event
async def on_ready():
    print("SlashConnecter is online")


#Test slash ping command
@slash.slash(name="ping",description="Reply pong",guild_ids=guild_id)
async def _ping(ctx:SlashContext):
    await ctx.send(f"Pong! ({client.latency*1000}ms)")

@slash.slash(name="autoroler",description="summons the auto roller post",guild_ids=guild_id)
async def _autoroler(ctx:SlashContext):
   await ctx.send("AUTOROLER", components=[create_actionrow(autoroler.matriculas_create()),create_actionrow(autoroler.atividades_create()),create_actionrow(autoroler.button_create())])

@client.event
async def on_component(ctx: ComponentContext):
    if(ctx.custom_id == "matriculas"):
        options =["1º ano","2º ano","3º ano","4º ano","5º ano"]
        await autoroler.handler(ctx,options)
        
    if(ctx.custom_id == "atividades"):
        options =["empresas,faina"]
        await autoroler.handler(ctx,options)
    

client.run(code)
