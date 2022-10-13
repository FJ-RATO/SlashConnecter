import os

import nextcord
from nextcord.ext import commands

import autoroler
# import eggy
import member_join
import empresas
import utils
import right_click

from secret import code as CODE
from secret import servers as GUILD_IDS

#CODE = os.getenv("TOKEN")
#GUILD_IDS = os.getenv("SERVERS")


client = nextcord.Client()

@client.event
async def on_ready():
    
    #reset the autoroler
    autoroler_channel = client.get_channel(760811656149598260)
    await autoroler_channel.purge(limit=1)
    await autoroler_channel.send("Autoroler Menu",view=autoroler.Menu()) 

    print("SlashConnecter is online \nVersion: 2.0.1 PRE-ALPHA")

############
# COMMANDS #
############

@client.slash_command(name="ping",description="Reply pong",guild_ids=GUILD_IDS)
async def _ping(ctx):
    await ctx.send(f"Pong! ({client.latency*1000}ms)")

@client.slash_command(name="version",description="Returns the current version",guild_ids=GUILD_IDS)
async def _version(ctx):
    await ctx.send(f"Slashconnecter v2.0 Nextcord")

@client.slash_command(name="tag",description="tags the role specificied in the arguemnt",guild_ids=GUILD_IDS)
async def _tag(ctx, role):
    await utils._tag(ctx,role)

##################
# COMMANDS ADMIN #
##################

@client.slash_command(name="autoroler",description="Summons the auto roller post",guild_ids=GUILD_IDS)
@commands.has_permissions(administrator=True)
async def _autoroler(ctx):
    await ctx.send("Autoroler Menu",view=autoroler.Menu())

@client.slash_command(name="autobuilder",description="Creates a role, text channel, voice channel, post channel in Empresas",guild_ids=GUILD_IDS)
@commands.has_permissions(administrator=True)
async def _autobuilder(ctx,name):
    await empresas.create(ctx,name)


#####################
# COMMANDS EMPRESAS #
#####################

###############
# RIGHT CLICK #
###############

@client.user_command(name = "Send test",guild_ids=GUILD_IDS)
@commands.has_role("cf") #does this even work ?
async def _test(ctx,user):
    await right_click.test(ctx,user)

##################
# EVENT LISTENER #
##################

@client.event
async def on_member_join(member):
    await member_join.welcome(member)   

client.run(CODE)