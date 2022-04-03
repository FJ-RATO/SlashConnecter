import nextcord

class Wait(nextcord.ui.Button):
    def __init__(self):
            super().__init__(custom_id= "dummy_button",label="Prioruty request", style = nextcord.ButtonStyle.red)
    async def callback(self, interaction:nextcord.Interaction):
        await interaction.user.send("Request sent")

class Button(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None
        self.add_item(Wait())

async def welcome(member):
    await member.send("Se bem-vindo ao servidor do NEECT\nEste é o SlashConnecter a nossa ferramenta para automatizar muitos processos dentro do servidor\nEnquanto esperas que um membro do NEECT te contacte certifica-te que sabes qual é o teu numero mecanográfico que te vai ser pedido\n")
    await member.send("Este Bot tambem é para ti quando tiveres acesso ao servidor usa '/' para descobrires todos os comandos a usar")
    await member.send("Se estas impaciente podes sempre carregar aqui (1/1000 vezes funciona)", view=Button())