import discord
from discord_slash.model import ButtonStyle
from discord_slash.utils.manage_components import create_select, create_select_option, create_actionrow,create_button

def button_create_help(): 
    button = create_button(
                style=ButtonStyle.blue,
                label="?",
                custom_id="info_roles",
                disabled= False
            )
    return button

def button_create_reset(): 
    button = create_button(
                style=ButtonStyle.red,
                label="RESET",
                custom_id="reset",
                disabled= False
            )
    return button

def info(ctx):
    embed=discord.Embed(title="Auto Roler Help", description="Aqui tens a descrição em detalhe de todas as secções", color=0xffff00)
    embed.add_field(name="Ano", value="Escolhe quais os anos dos quais queres receber notificações", inline=False)
    embed.add_field(name="Empresas", value="Recebe acesso à longa lista de parceiros que o NEECT tem para ti", inline=False)
    embed.add_field(name="Aluvião", value="Se estás interessado em integrar a praxe este é um role obrigatório", inline=False)
    embed.add_field(name="TaçaUa", value="Se queres saber tudo dos nossos atletas ou te queres tornar em um tens aqui a oportunidade", inline=False)
    embed.set_footer(text="Todos os aluviões devem ter o role aluvião sobre pena de represalias graves")
    return embed

def matriculas_create():
    select = create_select(
        options=[# the options in your dropdown
            create_select_option("1º ano", value="1º ano"),
            create_select_option("2º ano", value="2º ano"),
            create_select_option("3º ano", value="3º ano"),
            create_select_option("4º ano", value="4º ano"),
            create_select_option("5º ano", value="5º ano"),
        ],
        placeholder="Escolhe os teus anos",  # the placeholder text to show when no options have been chosen
        min_values=1,  # the minimum number of options a user must select
        max_values=5,  # the maximum number of options a user can select
        custom_id= "matriculas"
    )
    return select

def atividades_create():
    select = create_select(
        options=[# the options in your dropdown
            create_select_option("empresas", value="empresas"),
            create_select_option("aluvião", value="aluvião"),
            create_select_option("TaçaUa", value="TaçaUa"),
            create_select_option("Antigo Aluno", value="Antigo Aluno"),
        ],
        placeholder="Outros Roles",  # the placeholder text to show when no options have been chosen
        min_values=1,  # the minimum number of options a user must select
        max_values=4,  # the maximum number of options a user can select
        custom_id= "atividades"
    )
    return select

async def handler(ctx,options):
    
    #add role
    for x in ctx.selected_options:
        await ctx.author.add_roles(discord.utils.get(ctx.author.guild.roles, name = x))
    
    #remove role 
    aux = [x for x in options if x not in ctx.selected_options]
    for x in aux:
        await ctx.author.remove_roles(discord.utils.get(ctx.author.guild.roles, name = x))
    
    await ctx.edit_origin(content="Roles updated!")

async def reset(ctx):
    aux = ["1º ano","2º ano","3º ano","4º ano","5º ano","empresas","TaçaUa","aluvião","Antigo Aluno"]
    for x in aux:
        await ctx.author.remove_roles(discord.utils.get(ctx.author.guild.roles, name = x))
