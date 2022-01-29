import nextcord

class ButtonHelp(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        
    @nextcord.ui.button(
        label = "?",
        style = nextcord.ButtonStyle.link
    )
    async def autorolerhelp(self, button: nextcord.ui.button, interaction:nextcord.Interaction):
        print("button pressed")