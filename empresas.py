import discord
from discord import message
from discord.ext import commands

async def create(ctx,name):

    GUILD = ctx.guild
    ROLE = await GUILD.create_role(name=name)
    CT = discord.utils.get(ctx.guild.roles, name="ct")
    NEECT = discord.utils.get(ctx.guild.roles, name="NEECT")

    overwrites = {
    GUILD.default_role: discord.PermissionOverwrite(read_messages=False),
    ROLE: discord.PermissionOverwrite(read_messages=True),
    CT: discord.PermissionOverwrite(read_messages=True)
    }

    overwrites_private= {
    GUILD.default_role: discord.PermissionOverwrite(read_messages=False),
    ROLE: discord.PermissionOverwrite(read_messages=True),
    NEECT: discord.PermissionOverwrite(read_messages=True)
    }
    
    category = await GUILD.create_category_channel(name)
    await GUILD.create_text_channel(name + "-forum",category = category,overwrites= overwrites)
    await GUILD.create_voice_channel(name + "-video",category = category,overwrites= overwrites)
    await GUILD.create_voice_channel(name + "-admin",category = category,overwrites= overwrites_private)
    await ctx.send("all done")

    