from ssl import Options
import nextcord

class Actividades(nextcord.ui.Select):
    def __init__(self):
        actividades = [
            nextcord.SelectOption(label="aluvião"),
            nextcord.SelectOption(label="Taça UA"),
            nextcord.SelectOption(label="Antigo Aluno")
        ]
        super().__init__(placeholder="Escolhe os tuas atividades", min_values=1, max_values=3, options=actividades)
    async def callback(self, interaction: nextcord.Interaction):
        print(f"{self.values}")

class Anos(nextcord.ui.Select):
    def __init__(self):
        anos = [
            nextcord.SelectOption(label="1º ano"),
            nextcord.SelectOption(label="2º ano"),
            nextcord.SelectOption(label="3º ano"),
            nextcord.SelectOption(label="4º ano"),
            nextcord.SelectOption(label="5º ano"),
        ]
        super().__init__(placeholder="Escolhe os teus anos", min_values=1, max_values=5, options=anos)
    async def callback(self, interaction: nextcord.Interaction):
        selected = self.values
        for x in selected:
            await interaction.user.add_roles(nextcord.utils.get(interaction.guild.roles, name=x)) #add roles
        not_selected = [x.label for x in self.options if not x.label in selected]

        for x in not_selected:
            await interaction.user.remove_roles(nextcord.utils.get(interaction.guild.roles, name=x)) #removeroles

class Reset(nextcord.ui.Button):
    def __init__(self):
        super().__init__(custom_id= "autoroler_reset", label = "RESET", style = nextcord.ButtonStyle.red)
    async def callback(self, interaction:nextcord.Interaction):
        print("reset")

class Help(nextcord.ui.Button):
    def __init__(self):
        super().__init__(custom_id= "autoroler_help", label = "?", style= nextcord.ButtonStyle.blurple)
    async def callback(self, interaction: nextcord.Interaction):
        print("help")

class Menu(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None
        self.add_item(Anos())
        self.add_item(Actividades())
        self.add_item(Help())
        self.add_item(Reset())
        

