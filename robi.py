import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} olarak giriş yapıldı!")

@bot.command()
async def geri(ctx, *, malzeme):
    cevaplar = {
        "plastik şişe": "Plastik şişeleri geri dönüşüm kutusuna atabilirsin. Ayrıca saksı veya kalemlik olarak yeniden kullanabilirsin! ve sana aferin https://random-d.uk/api/3.gif",
        "cam şişe": "Cam şişeleri cam geri dönüşüm kutusuna atabilirsin. Dekoratif süs eşyası olarak da kullanabilirsin. ve sana aferin https://random-d.uk/api/3.gif",
        "kağıt": "Kağıtları geri dönüşüm kutusuna at veya taslak kağıt olarak kullan. ve sana aferin https://random-d.uk/api/3.gif",
        "muz kabuğu": "Muz kabuğu, kompost için harikadır. Toprak zenginleştirici olarak kullanabilirsin. ve sana aferin https://random-d.uk/api/3.gif"
    }

    malzeme = malzeme.lower()
    if malzeme in cevaplar:
        await ctx.send(cevaplar[malzeme])
    else:
        await ctx.send("Bu malzeme için özel bir bilgi bulunamadı. Ama muhtemelen geri dönüşüm kutusuna girebilir!")

bot.run('')
