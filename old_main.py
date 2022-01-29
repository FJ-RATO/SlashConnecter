import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from discord.file import File
from discord_slash import SlashCommand, SlashContext,ComponentContext
from discord_slash.utils.manage_commands import create_choice, create_option
from discord_slash.utils.manage_components import create_select, create_select_option, create_actionrow

from secret import code as code
from secret import servers as servers

import autoroler
import eggy
import member_join
import empresas

client = discord.Client(intents = discord.Intents.all())
slash = SlashCommand(client, sync_commands=True)

guild_id = servers

@client.event
async def on_ready():
    print("SlashConnecter is online")

############
# COMMANDS #
############

@slash.slash(name="ping",description="Reply pong",guild_ids=guild_id)
async def _ping(ctx:SlashContext):
    await ctx.send(f"Pong! ({client.latency*1000}ms)")

@slash.slash(name="tag",description="tags the role specificied in the arguemnt")
async def _tag(ctx:SlashContext, role):
    r = discord.utils.get(ctx.author.guild.roles, name = role)
    if r in ctx.author.roles:
        await ctx.send(r.mention)
    else:
       await ctx.author.send("You do not have the role {r.name}")

@slash.slash(name="autoroler",description="Summons the auto roller post",guild_ids=guild_id)
@commands.has_permissions(administrator=True)
async def _autoroler(ctx:SlashContext):
   await ctx.send("AUTOROLER", components=[create_actionrow(autoroler.matriculas_create()),create_actionrow(autoroler.atividades_create()),create_actionrow(autoroler.button_create_help(),autoroler.button_create_reset())])

@slash.slash(name="egg",description="egg start|revive (starts or revives the game)",guild_ids=guild_id)
@commands.has_permissions(administrator=True)
async def _egg(ctx:SlashContext, arg0):
    if arg0 == "start":
        eggy.play.start(client)
    if arg0 == "revive":
        eggy.revive()
    if arg0 == "kill":
        eggy.kill()

#@slash.slash(name="survive",description="Sends survior guide by PM", guild_ids=guild_id)
#@commands.cooldown(1,60,BucketType.user) #one use every 60 sec's by user
#async def _survive(ctx:SlashContext):
#    await ctx.author.send(file=File("PATH HERE"))

@slash.slash(name="autobuilder",description="Creates a role, text channel, voice channel, post channel in Empresas",guild_ids=guild_id)
@commands.has_permissions(administrator=True)
async def _autobuilder(ctx:SlashContext,name):
    await empresas.create(ctx,name)


##################
# EVENT LISTENER #
##################

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
        options =["empresas","TaçaUa","aluvião","Antigo Aluno"]
        await autoroler.handler(ctx,options)

    if(ctx.custom_id == "info_roles"):
        await ctx.edit_origin(content="Help Sent!") #must put in autoroler
        await ctx.author.send(embed=autoroler.info())
    
    if(ctx.custom_id == "reset"):
        await ctx.edit_origin(content="Reseted the roles!") #must put in autoroler
        await autoroler.reset(ctx)


client.run(code)
