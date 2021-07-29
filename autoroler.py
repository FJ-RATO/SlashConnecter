import discord
from discord_slash.model import ButtonStyle
from discord_slash.utils.manage_components import create_select, create_select_option, create_actionrow,create_button

def button_create(): 
    button = create_button(
                style=ButtonStyle.red,
                label="Useless Button",
                custom_id="Exit all roles",
                disabled= True
            )
    return button

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
            create_select_option("faina", value="faina"),
        ],
        placeholder="Escolhe as tuas atividades",  # the placeholder text to show when no options have been chosen
        min_values=1,  # the minimum number of options a user must select
        max_values=2,  # the maximum number of options a user can select
        custom_id= "atividades"
    )
    return select

async def handler(ctx,options):
    for x in ctx.selected_options:
        await ctx.author.add_roles(discord.utils.get(ctx.author.guild.roles, name = x))
    aux = [x for x in options if x not in ctx.selected_options]
    for x in aux:
        await ctx.author.remove_roles(discord.utils.get(ctx.author.guild.roles, name = x))
    await ctx.edit_origin(content="Roles updated!")
