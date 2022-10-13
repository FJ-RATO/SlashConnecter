from calendar import different_locale
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
        selected = self.values
        dif_add = []
        dif_remove = [] 
        for x in selected:
            await interaction.user.add_roles(nextcord.utils.get(interaction.guild.roles, name=x)) #add roles
            dif_add.append(x)

        not_selected = [x.label for x in self.options if not x.label in selected]

        for x in not_selected:
            await interaction.user.remove_roles(nextcord.utils.get(interaction.guild.roles, name=x)) #removeroles
            dif_remove.append(x)

        await interaction.send(content=f"Roles added {dif_add}, roles removed {dif_remove}",ephemeral= True,delete_after=5)

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
        dif_add = []
        dif_remove = [] 
        for x in selected:
            await interaction.user.add_roles(nextcord.utils.get(interaction.guild.roles, name=x)) #add roles
            dif_add.append(x)
        not_selected = [x.label for x in self.options if not x.label in selected]

        for x in not_selected:
            await interaction.user.remove_roles(nextcord.utils.get(interaction.guild.roles, name=x)) #removeroles
            dif_remove.append(x)
        
        await interaction.send(content=f"Roles added {dif_add}, roles removed {dif_remove}",ephemeral= True,delete_after=5)

class Reset(nextcord.ui.Button):
    def __init__(self):
        super().__init__(custom_id= "autoroler_reset", label = "RESET", style = nextcord.ButtonStyle.red)
    async def callback(self, interaction:nextcord.Interaction):
        aux = ["1º ano","2º ano","3º ano","4º ano","5º ano","Taça UA","aluvião","Antigo Aluno"]
        for x in aux:
            await interaction.user.remove_roles(nextcord.utils.get(interaction.guild.roles, name=x))

class Help(nextcord.ui.Button):
    def __init__(self):
        super().__init__(custom_id= "autoroler_help", label = "?", style= nextcord.ButtonStyle.blurple)
    async def callback(self, interaction: nextcord.Interaction):
        embed=nextcord.Embed(title="Auto Roler Help", description="Aqui tens a descrição em detalhe de todas as secções", color=0xffff00)
        embed.add_field(name="Ano", value="Escolhe quais os anos dos quais queres receber notificações", inline=False)
        embed.add_field(name="Empresas", value="Recebe acesso à longa lista de parceiros que o NEECT tem para ti", inline=False)
        embed.add_field(name="Aluvião", value="Se estás interessado em integrar a praxe este é um role obrigatório", inline=False)
        embed.add_field(name="TaçaUa", value="Se queres saber tudo dos nossos atletas ou te queres tornar em um tens aqui a oportunidade", inline=False)
        embed.set_footer(text="Todos os aluviões devem ter o role aluvião sobre pena de represalias graves")
        await interaction.user.send(embed=embed)

class Menu(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.value = None
        self.add_item(Anos())
        self.add_item(Actividades())
        self.add_item(Help())
        self.add_item(Reset())