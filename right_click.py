import nextcord

async def test(ctx,user):
    await user.send("test target")
    await ctx.send(delete_after=3,content="test sent")

async def super_add(ctx,user):
    super_role = nextcord.utils.get(ctx.guild.roles, name="SUPER")
    await user.add_roles(super_role)
    await ctx.send(f"{user.display_name} is now a super user",ephemeral= True)

async def super_remove(ctx,user):
    super_role = nextcord.utils.get(ctx.guild.roles, name="SUPER")
    await user.remove_roles(super_role)
    await ctx.send(f"{user.display_name} is no longer a super user",ephemeral= True)