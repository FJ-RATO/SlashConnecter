import nextcord

async def _tag(ctx, role):
    r = nextcord.utils.get(ctx.guild.roles, name = role)
    if r in ctx.user.roles:
        await ctx.send(r.mention)
    else:
       await ctx.user.send(f"You do not have the role {role}")