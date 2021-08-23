import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext,ComponentContext
from discord_slash.utils.manage_commands import create_choice, create_option
from discord_slash.utils.manage_components import create_select, create_select_option, create_actionrow

from secret import code as code
from secret import servers as servers

import autoroler
import eggy

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
@commands.has_permissions(administrator=True)
async def _autoroler(ctx:SlashContext):
   await ctx.send("AUTOROLER", components=[create_actionrow(autoroler.matriculas_create()),create_actionrow(autoroler.atividades_create()),create_actionrow(autoroler.button_create())])

@slash.slash(name="egg",description="starts the egg game",guild_ids=guild_id)
@commands.has_permissions(administrator=True) #move to on_ready when finished
async def _egg(ctx:SlashContext):
    eggy.play.start()

@slash.slash(name="revive",description="revive the egg",guild_ids=guild_id)
@commands.has_permissions(administrator=True) #move to on_ready when finished
async def _revive(ctx:SlashContext):
    eggy.revive()

@slash.slash(name="rub",description="gives heat to the egg",guild_ids=guild_id)
@commands.cooldown(1, 10, commands.BucketType.user)
async def _rub(ctx:SlashContext):
    eggy.rub()

@client.event
async def on_component(ctx: ComponentContext):
    if(ctx.custom_id == "matriculas"):
        options =["1º ano","2º ano","3º ano","4º ano","5º ano"]
        await autoroler.handler(ctx,options)
        
    if(ctx.custom_id == "atividades"):
        options =["empresas" ,"aluvião","desporto"]
        await autoroler.handler(ctx,options)

    if(ctx.custom_id == "info_roles"):
        await ctx.edit_origin(content="Help Sent!") #must put in autoroler
        await ctx.author.send(embed=autoroler.info(ctx))


client.run(code)
