import discord 
from discord.ext import commands
import requests
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("TOKEN")
try:
    ID_ROL = int(os.getenv("ID_ROL"))  # Convertir a entero
except (ValueError, TypeError):
    print("Error: ID_ROL no es un número válido o no está configurado")
    ID_ROL = None


intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix = "!", intents=intents)

@bot.command()
async def poked(ctx, args):
    try:
        pokemon = args.split(" ",1)[0].lower()
        result = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
        
        if result.text == "Not Found":
            await ctx.send("Pokemon no Encontrado")
        else:
            image_url = result.json()["sprites"]["front_default"]
            print(image_url)
            await ctx.send(image_url)

    except Exception as e:
        print("Error: ", e)

@poked.error
async def error_type(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send("tienes q pasar un pokemon")

@bot.command()
async def test(ctx, *args):
    respuestas = " ".join(args)
    await ctx.send(respuestas)

@bot.command()
async def clear(ctx):
    await ctx.channel.purge()
    await ctx.send("Todo limpio", delete_after=3)

@bot.event
async def on_ready():
    print(f"running {bot.user}")

@bot.event
async def on_member_join(member):
    # Obtiene el rol por ID
    role = member.guild.get_role(ID_ROL)
    if role:
        try:
            await member.add_roles(role)
            print(f'Se ha asignado el rol {role.name} a {member.name}')
        except Exception as e:
            print(f'Error asignando rol: {e}')
    else:
        print(f'Rol no encontrado (ID: {ID_ROL})')
        # Imprimir todos los roles del servidor para diagnóstico
        print("Roles disponibles:", [f"{r.name} (ID: {r.id})" for r in member.guild.roles])

bot.run(token)