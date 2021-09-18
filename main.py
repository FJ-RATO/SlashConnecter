import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext,ComponentContext
from discord_slash.utils.manage_commands import create_choice, create_option
from discord_slash.utils.manage_components import create_select, create_select_option, create_actionrow

from secret import code as code
from secret import servers as servers

import autoroler
import eggy
import member_join
import curriculum

client = discord.Client(intents = discord.Intents.all())
slash = SlashCommand(client, sync_commands=True)

guild_id = servers

@client.event
async def on_ready():
    print("SlashConnecter is online")

@slash.slash(name="ping",description="Reply pong",guild_ids=guild_id)
async def _ping(ctx:SlashContext):
    await ctx.send(f"Pong! ({client.latency*1000}ms)")

@slash.slash(name="autoroler",description="summons the auto roller post",guild_ids=guild_id)
@commands.has_permissions(administrator=True)
async def _autoroler(ctx:SlashContext):
   await ctx.send("AUTOROLER", components=[create_actionrow(autoroler.matriculas_create()),create_actionrow(autoroler.atividades_create()),create_actionrow(autoroler.button_create())])

@slash.slash(name="egg",description="egg start|revive (starts or revives the game)",guild_ids=guild_id)
@commands.has_permissions(administrator=True)
async def _egg(ctx:SlashContext, arg0):
    if arg0 == "start":
        eggy.play.start(client)
    if arg0 == "revive":
        eggy.revive()

@client.event
async def on_message(message):
    if message.channel.id == 821134781839573032: #canal viveiro, se alguem escrever neste canal o ovo recebe x pontos
        eggy.heat()

@client.event
async def on_member_join(member):
    await member_join.welcome(member)    

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
