import discord
from discord.ext import commands

client = commands.Bot(command_prefix= "?")
client.remove_command("help")

@client.event
async def on_ready():
    print("Bot jest online")
    await client.change_presence(activity=discord.Game(name="?help"))


@client.command()
async def help(ctx):
    await ctx.channel.send('pomoc')

client.run("OTY5OTg0OTI5NDk4ODA0MjQ1.Ym1W3A.053kGg9-xfHAkVo8a_tXTITkBxo")