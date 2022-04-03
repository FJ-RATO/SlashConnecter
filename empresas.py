import nextcord

async def create(ctx,name):

    GUILD = ctx.guild
    ROLE = await GUILD.create_role(name=name)
    CT = nextcord.utils.get(ctx.guild.roles, name="ct")
    NEECT = nextcord.utils.get(ctx.guild.roles, name="NEECT")

    overwrites = {
    GUILD.default_role: nextcord.PermissionOverwrite(read_messages=False),
    ROLE: nextcord.PermissionOverwrite(read_messages=True),
    CT: nextcord.PermissionOverwrite(read_messages=True)
    }

    overwrites_private= {
    GUILD.default_role: nextcord.PermissionOverwrite(read_messages=False),
    ROLE: nextcord.PermissionOverwrite(read_messages=True),
    NEECT: nextcord.PermissionOverwrite(read_messages=True)
    }
    
    category = await GUILD.create_category_channel(name)
    await GUILD.create_text_channel(name + "-forum",category = category,overwrites= overwrites)
    await GUILD.create_voice_channel(name + "-video",category = category,overwrites= overwrites)
    await GUILD.create_voice_channel(name + "-admin",category = category,overwrites= overwrites_private)
    await ctx.send("all done")

    