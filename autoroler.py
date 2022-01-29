import nextcord

class ButtonHelp(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None
        
    @nextcord.ui.button(
        custom_id= "autoroler_help",
        label = "?",
        style = nextcord.ButtonStyle.primary
    )
    async def autorolerhelp(self, button: nextcord.ui.button, interaction:nextcord.Interaction):
        print("help")


    @nextcord.ui.button(
        custom_id= "autoroler_reset",
        label = "RESET",
        style = nextcord.ButtonStyle.red
    )
    async def autorolerreset(self, button: nextcord.ui.button, interaction:nextcord.Interaction):
        print("reset")
