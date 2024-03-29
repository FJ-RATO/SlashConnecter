import os

import nextcord
from nextcord.ext import application_checks

import autoroler
import cf
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

    print("SlashConnecter is online \nVersion: 2.2.0 ALPHA")

############
# COMMANDS #
############

@client.slash_command(name="ping",description="Reply pong",guild_ids=GUILD_IDS)
async def _ping(ctx):
    await ctx.send(f"Pong! ({client.latency*1000}ms)")

@client.slash_command(name="version",description="Returns the current version",guild_ids=GUILD_IDS)
async def _version(ctx):
    await ctx.send(f"Slashconnecter v2.2.0 ALPHA [CF UPDATE]")

@client.slash_command(name="tag",description="tags the role specificied in the arguemnt",guild_ids=GUILD_IDS)
async def _tag(ctx, role):
    await utils._tag(ctx,role)

@client.user_command(name = "Send Debug",guild_ids=GUILD_IDS) #right click on user
async def _test(ctx,user):
    await right_click.test(ctx,user)

##################
# COMMANDS ADMIN #
##################

@client.slash_command(name="autoroler",description="Summons the auto roller post",guild_ids=GUILD_IDS)
@application_checks.has_permissions(administrator=True)
async def _autoroler(ctx):
    await ctx.send("Autoroler Menu",view=autoroler.Menu())

@client.user_command(name = "Update to Super",guild_ids=GUILD_IDS)
@application_checks.has_permissions(administrator=True)
@application_checks.has_role("SUPER")
async def _super(ctx,user):
    await right_click.super_add(ctx,user)

@client.user_command(name = "Remove from Super",guild_ids=GUILD_IDS)
@application_checks.has_permissions(administrator=True)
@application_checks.has_role("SUPER")
async def _unsuper(ctx,user):
    await right_click.super_remove(ctx,user)

#####################
# COMMANDS EMPRESAS #
#####################

@client.slash_command(name="autobuilder",description="Creates a role, text channel, voice channel, post channel in Empresas",guild_ids=GUILD_IDS)
@application_checks.has_permissions(administrator=True)
async def _autobuilder(ctx,name):
    await empresas.create(ctx,name)

######
# CF #
######

@client.slash_command(name="caderno",description="ADD & SUB traços from the caderno",guild_ids=GUILD_IDS)
@application_checks.has_role("CF")
async def _caderno(ctx,command,amount):
    await cf.caderno(ctx,command,amount)

@client.user_command(name = "Update to Aluvião",guild_ids=GUILD_IDS) #right click on user
@application_checks.has_role("CF")
async def _add_aluvião(ctx,user):
    await cf.add_aluvião(ctx,user)

@client.user_command(name = "Update to Veterano",guild_ids=GUILD_IDS) #right click on user
@application_checks.has_role("CF")
async def _add_veterano(ctx,user):
    await cf.add_veterano(ctx,user)
##################
# EVENT LISTENER #
##################

@client.event
async def on_member_join(member):
    await member_join.welcome(member)   

client.run(CODE)
