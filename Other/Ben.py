import discord
from discord.ext import commands
from discord import FFmpegPCMAudio


client = commands.Bot(command_prefix="")


@client.event
async def on_ready():
    print('Logged on as {0.user}!'.format(client))


@client.command(pass_context=True)
async def callben(ctx):
    if (ctx.author.voice):
        channel = ctx.author.voice.channel
        try:
            voice = await channel.connect()
            source = FFmpegPCMAudio('')
        except:
            await ctx.send("yes")
    else:
        await ctx.send("ho ho ho...")


@client.command(pass_context=True)
async def killben(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send("no")


client.run('OTYxNDgzOTkwMTgxNzQ4NzM2.Yk5pvg.1fULrREGXTmV-yq-eZDEdmzWbV8')
