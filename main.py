import discord
from PIL import Image, ImageDraw
from io import BytesIO
import requests

from config import *

bot = discord.Bot()

@bot.event
async def on_ready():
    print("Ready")

@bot.slash_command(guild_ids=GUILD_IDS, description='h')
async def test(ctx, url: discord.Option(str, "url")):
    try:
        response = requests.get(url)
    except:
        response = requests.get(str(ctx.author.display_avatar))
        print(str(ctx.author.display_avatar))

    img = Image.new('RGB', (1570,942), color='grey')

    
    img2 = Image.open(BytesIO(response.content))

    mask_img = Image.new("L", img2.size, 0)
    draw = ImageDraw.Draw(mask_img)
    draw.ellipse((140,50,260,170), fill=255)

    img2.reduce


    img.paste(img2, (157,157), mask_img)


    img.save('test.png')
    await ctx.respond(file=discord.File('test.png'))

bot.run(BOT_TOKEN)