import discord

from config import *

bot = discord.Bot()

@bot.event
async def on_ready():
    print("Ready")

@bot.slash_command(guild_ids=GUILD_IDS)
async def test(ctx):
    await ctx.respond('hi')

bot.run(BOT_TOKEN)