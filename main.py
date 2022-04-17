import os
from pickle import TRUE

import nextcord
from nextcord.ext import commands

import autoroler
# import eggy
import member_join
import empresas
import utils
import market

from secret import code as CODE
from secret import servers as GUILD_IDS

#CODE = os.getenv("TOKEN")
#GUILD_IDS = os.getenv("SERVERS")


client = nextcord.Client()

@client.event
async def on_ready():
    
    #reset the autoroler
    try:
        autoroler_channel = client.get_channel(760811656149598260)
        await autoroler_channel.purge(limit=1)
        await autoroler_channel.send("Autoroler Menu",view=autoroler.Menu())
        print("Autoroler reset: SUCCESS")
    except:
        print("Autoroler reset: FAILED\n(Is the id channel correct?)\n")

    #reset the game
    try:
        market.init()
        print("Game reset: SUCCESS")
    except:
        print("Game reset: FAILED\n(Is the id channel correct?)\n")

    print("SlashConnecter is online \nVersion: 2.0.1 PRE-ALPHA")

############
# COMMANDS #
############

@client.slash_command(name="ping",description="Reply pong",guild_ids=GUILD_IDS)
async def _ping(ctx):
    await ctx.send(content=f"Pong! ({client.latency*1000}ms)",ephemeral=True)

@client.slash_command(name="version",description="Returns the current version",guild_ids=GUILD_IDS)
async def _version(ctx):
    await ctx.send(content=f"Slashconnecter v2.0.1 Nextcord",ephemeral=True)

@client.slash_command(name="tag",description="tags the role specificied in the arguemnt",guild_ids=GUILD_IDS)
async def _tag(ctx, role):
    await utils._tag(ctx,role)

@client.slash_command(name="game",description="Game handler, go to game channel for more ingo",guild_ids=GUILD_IDS)
async def _game(ctx,option,stock,amount):
    market.handler(ctx,option,stock,amount)

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
    await ctx.send(content="All channels are ready",ephemeral=True)

####################
# MESSAGE COMMANDS #
####################
@client.user_command(name="copy pasta",guild_ids=GUILD_IDS)
#@client.message_command(name="copy pasta",guild_ids=GUILD_IDS)
async def _copy_pasta(interaction,message):
    await message.send(f"{interaction.user.name} sent you some pasta <3")
    await interaction.send(content="Pasta away",ephemeral=True)

#####################
# COMMANDS EMPRESAS #
#####################

##################
# EVENT LISTENER #
##################

@client.event()
async def on_member_join(member):
    await member_join.welcome(member)   

client.run(CODE)