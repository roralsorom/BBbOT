import discord
from discord.ext import commands
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
import json
import os
from py_currency_converter import convert
import locale
locale.setlocale(locale.LC_ALL, 'de_DE.utf-8')

token = "OTc4NTU3ODM0MTY3OTk2NDY2.G7MUav.GAl28_NtIZoeRpv_3DmmKe6gqGa3LmxFd45foA"
prefix = "$"

intentss = discord.Intents().all()

bot = commands.Bot(command_prefix=prefix, intents=intentss)


@bot.event
async def on_ready():
    print("Bot is ready")


def reddText(textt):
    return f"""```ansi
    [9;31m[1;40m{textt}```"""

def greennText(textt):
    return f"""```ansi
    [32;1m{textt}```"""
class Int(int):
    def __repr__(self):
        return "{:,}".format(self)



@bot.command()
async def crypto(ctx):
    bitcoinReq = requests.get("https://coinmarketcap.com/currencies/bitcoin").text
    bitcoinPrice = bitcoinReq.split("<div class=\"priceValue \"><span>")[1].split("</span></div>")[0]
    ethReq = requests.get("https://coinmarketcap.com/currencies/ethereum").text
    ethPrice = ethReq.split("<div class=\"priceValue \"><span>")[1].split("</span></div>")[0]
    bnbReq = requests.get("https://coinmarketcap.com/currencies/bnb").text
    bnbPrice = bnbReq.split("<div class=\"priceValue \"><span>")[1].split("</span></div>")[0]
    solonaReq = requests.get("https://coinmarketcap.com/currencies/solana").text
    solonaPrice = solonaReq.split("<div class=\"priceValue \"><span>")[1].split("</span></div>")[0]
    avalancheReq = requests.get("https://coinmarketcap.com/currencies/avalanche").text
    avalanchePrice = avalancheReq.split("<div class=\"priceValue \"><span>")[1].split("</span></div>")[0]
    dripReq = requests.get("https://coinmarketcap.com/currencies/drip-network").text
    dripPrice = dripReq.split("<div class=\"priceValue \"><span>")[1].split("</span></div>")[0]
    embed = discord.Embed(title="Crypto Prices $USD",description=":chart_with_upwards_trend: :chart_with_upwards_trend:", color=0x00ff00)
    embed.add_field(name="Bitcoin", value=bitcoinPrice, inline=True)
    embed.add_field(name="Ethereum", value=ethPrice, inline=True)
    embed.add_field(name="Binance Coin", value=bnbPrice, inline=True)
    embed.add_field(name="Solana", value=solonaPrice, inline=True)
    embed.add_field(name="Avalanche", value=avalanchePrice, inline=True)
    embed.add_field(name="Drip Network", value=dripPrice, inline=True)
    await ctx.send(embed=embed)
    embed = discord.Embed(title="Crypto Prices $AUD", description=":chart_with_upwards_trend: :chart_with_upwards_trend:", color=0x00ff00)
    #Split bitcoinPrice and remove , and .
    bitcoinPrice = bitcoinPrice.replace(",", "")
    bitcoinPrice = bitcoinPrice.replace(".", "")
    bitcoinPrice = bitcoinPrice.replace("$", "")

    bitcoinJsonn = json.dumps(convert(amount=int(bitcoinPrice), to=['AUD']))
    bitcoinJsonn = json.loads(bitcoinJsonn)
    bitcoinPrice = Int(bitcoinJsonn["AUD"])
    embed.add_field(name="Bitcoin", value="$" + str(bitcoinPrice), inline=True)
    #Split ethPrice and remove , and .
    ethPrice = ethPrice.replace(",", "")
    ethPrice = ethPrice.replace(".", "")
    ethPrice = ethPrice.replace("$", "")
    ethJsonn = json.dumps(convert(amount=int(ethPrice), to=['AUD']))
    ethJsonn = json.loads(ethJsonn)
    ethPrice = Int(ethJsonn["AUD"])
    embed.add_field(name="Ethereum", value="$" + str(ethPrice), inline=True)
    #Split bnbPrice and remove , and .
    bnbPrice = bnbPrice.replace(",", "")
    bnbPrice = bnbPrice.replace(".", "")
    bnbPrice = bnbPrice.replace("$", "")
    bnbJsonn = json.dumps(convert(amount=int(bnbPrice), to=['AUD']))
    bnbJsonn = json.loads(bnbJsonn)
    bnbPrice = Int(bnbJsonn["AUD"])
    embed.add_field(name="Binance Coin", value="$" + str(bnbPrice), inline=True)
    #Split solonaPrice and remove , and .
    solonaPrice = solonaPrice.replace(",", "")
    solonaPrice = solonaPrice.replace(".", "")
    solonaPrice = solonaPrice.replace("$", "")
    solonaJsonn = json.dumps(convert(amount=int(solonaPrice), to=['AUD']))
    solonaJsonn = json.loads(solonaJsonn)
    solonaPrice = Int(solonaJsonn["AUD"])
    embed.add_field(name="Solana", value="$" + str(solonaPrice), inline=True)
    #Split avalanchePrice and remove , and .
    avalanchePrice = avalanchePrice.replace(",", "")
    avalanchePrice = avalanchePrice.replace(".", "")
    avalanchePrice = avalanchePrice.replace("$", "")
    avalancheJsonn = json.dumps(convert(amount=int(avalanchePrice), to=['AUD']))
    avalancheJsonn = json.loads(avalancheJsonn)
    avalanchePrice = Int(avalancheJsonn["AUD"])
    embed.add_field(name="Avalanche", value="$" + str(avalanchePrice), inline=True)
    #Split dripPrice and remove , and .
    dripPrice = dripPrice.replace(",", "")
    dripPrice = dripPrice.replace(".", "")
    dripPrice = dripPrice.replace("$", "")
    dripJsonn = json.dumps(convert(amount=int(dripPrice), to=['AUD']))
    dripJsonn = json.loads(dripJsonn)
    dripPrice = dripJsonn['AUD']
    embed.add_field(name="Drip Network", value="$" + str(dripPrice)[:2] + "," + str(dripPrice)[2:], inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def nuke(ctx):
    #Save channel permission and delete channel and create new channel with same name and permission in the same category
    channel = ctx.channel
    category = channel.category
    overwrites = channel.overwrites
    await channel.delete()
    newChannel = await category.create_text_channel(channel.name, overwrites=overwrites)
    await newChannel.send(f"{ctx.author.mention} has nuked this channel")   



bot.run(token)