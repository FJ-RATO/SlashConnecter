import nextcord

async def _test(ctx,user):
    await user.send("test target")
    await ctx.send(delete_after=3,content="test sent")