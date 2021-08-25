import discord
from discord_slash.model import ButtonStyle
from discord_slash.utils.manage_components import create_select, create_select_option, create_actionrow,create_button

async def welcome(member):
    await member.send("Se bem-vindo ao servidor do NEECT\n Este é o SlashConnecter a nossa ferramenta para automatizar muitos processos dentro do servidor\n Enquanto esperas que um membro do NEECT te contacte certifica-te que sabes qual é o teu numero mecanográfico que te vai ser pedido\n")
    await member.send("Este Bot tambem é para ti quando tiveres acesso ao servidor usa '/' para descobrires todos os comandos a usar\n Se estas impaciente podes sempre carregar aqui")
    button_faster = create_button(
                style=ButtonStyle.red,
                label="priority request",
                disabled= False
            )
    await member.send(components=[create_actionrow(button_faster)])