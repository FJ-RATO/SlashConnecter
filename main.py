import nextcord
from nextcord.ext import commands

import autoroler
# import eggy
# import member_join
# import empresas

from secret import code as CODE
from secret import servers as GUILD_IDS

client = nextcord.Client()

@client.event
async def on_ready():
    print("SlashConnecter is online \nVersion: 2.0 PRE-ALPHA")

############
# COMMANDS #
############

@client.slash_command(name="ping",description="Reply pong",guild_ids=GUILD_IDS)
async def _ping(ctx):
    await ctx.send(f"Pong! ({client.latency*1000}ms)")

@client.slash_command(name="tag",description="tags the role specificied in the arguemnt",guild_ids=GUILD_IDS)
async def _tag(ctx, role):
    r = nextcord.utils.get(ctx.guild.roles, name = role)
    if r in ctx.user.roles:
        await ctx.send(r.mention)
    else:
       await ctx.user.send(f"You do not have the role {role}")

@client.slash_command(name="autoroler",description="Summons the auto roller post",guild_ids=GUILD_IDS)
@commands.has_permissions(administrator=True)
async def _autoroler(ctx):
#    await ctx.send("AUTOROLER", components=[nextcord.actionrow(autoroler.matriculas_create()),nextcord.actionrow(autoroler.atividades_create()),nextcord.actionrow(autoroler.button_create_help(),autoroler.button_create_reset())])
   # await ctx.send("list",view=autoroler.Anos())
    await ctx.send("Autoroler Menu",view=autoroler.Menu())


client.run(CODE)