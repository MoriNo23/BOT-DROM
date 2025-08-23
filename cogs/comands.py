import discord 
from discord.ext import commands

class Comand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(ctx, *args):
        respuestas = " ".join(args)
        await ctx.send(respuestas)

    @commands.command()
    async def clear(ctx):
        await ctx.channel.purge()
        await ctx.send("Todo limpio", delete_after=3)