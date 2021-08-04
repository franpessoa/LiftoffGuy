import discord
import os
import apirequest
import json
import requests
import asyncio
from discord.ext import commands

client = commands.Bot(command_prefix='=', help_command=None)

async def change_status():
  await client.wait_until_ready()
  while not client.is_closed():
    status = "em {} servers".format(len(client.guilds))
    await client.change_presence(activity=discord.Game(name=status))
    await asyncio.sleep(6)


def apod_get():
  nx = requests.get('https://api.nasa.gov/planetary/apod?api_key={}'.format(os.getenv(NASA_API_KEY)))
  data = json.loads(nx.text)
  name = data["title"]
  des = data["explanation"]
  hora = data["date"]
  url = data["url"]
  lista = [url, hora, des, name]
  return lista

@client.command()
async def next(ctx):
  url = apirequest.no_search()
  embedVar = apirequest.request(url)
  if not embedVar:
    await ctx.send("Tivemos um erro :(")
  else:
    embed = discord.Embed(title=embedVar[2], description=embedVar[7], color=0xffdd00)
    embed.add_field(name='Foguete', value=embedVar[0], inline=True)
    embed.add_field(name='Órbita', value=embedVar[4], inline=True)
    embed.add_field(name='Missão', value=embedVar[3], inline=True)
    embed.add_field(name='Tipo', value=embedVar[5], inline=True)
    embed.add_field(name='Status', value=embedVar[6], inline=True)
    embed.add_field(name='Pad', value=embedVar[8], inline=True)
    await ctx.send(embed=embed)

@client.command()
async def company(ctx, argument):
  url = apirequest.company_name(argument)
  embedVar = apirequest.request(url)
  embed = discord.Embed(title=embedVar[2], description=embedVar[7], color=0xffdd00)
  embed.add_field(name='Foguete', value=embedVar[0], inline=True)
  embed.add_field(name='Órbita', value=embedVar[4], inline=True)
  embed.add_field(name='Missão', value=embedVar[3], inline=True)
  embed.add_field(name='Tipo', value=embedVar[5], inline=True)
  embed.add_field(name='Status', value=embedVar[6], inline=True)
  embed.add_field(name='Pad', value=embedVar[8], inline=True)
  await ctx.send(embed=embed)

@client.command()
async def apod(ctx):
  act = apod_get()
  embed = discord.Embed(title='{} // {}'.format(act[3], act[1]), description=act[2], url=act[0], color=0xBDFDFF)
  embed.set_image(url=act[0])
  await ctx.send(embed=embed)

@client.command()
async def help(ctx):
  help_text = '''**LISTA DE COMANDOS**
  =help : Lista de Comandos
  =add : Adicione o bot em seu server
  =github : Github do projeto
  =site : Site do bot
  
  =next : Próximo lançamento
  =company {companhia} : Próximo lançamento de determinada companhia
  =apod : Imagem do dia pela NASA
  =list : Lista de companhias suportadas
  =issnow : Posição atual da ISS'''
  
  await ctx.send(help_text)

@client.command()
async def add(ctx):
  await ctx.send('''Adicione-me em seu server!
  https://discord.com/api/oauth2/authorize?client_id=817438170097385523&permissions=8&scope=bot''')

@client.command()
async def github(ctx):
  await ctx.send('''Github do projeto:
  https://github.com/franpessoa/LOXLoadingComplete''')

@client.command()
async def site(ctx):
  await ctx.send('''Site do bot:
  https://arco.coop.br/~franpessoa/lox-loading-complete.html''')

@client.command()
async def issnow(ctx):
  url = 'http://api.open-notify.org/iss-now.json'
  issnow = requests.get(url)
  issnow_data = json.loads(issnow.text)
  issnow_list = issnow_data["iss_position"]
  latitude = issnow_list["latitude"]
  longitude = issnow_list["longitude"]
  embed = discord.Embed(title="Posição da ISS", description="Clique no título para ver no mapa", color=0x8ceb34, url='https://arco.coop.br/~franpessoa/iss/')
  embed.add_field(name='Latitude', value=latitude, inline=True)
  embed.add_field(name='Longitude', value=longitude, inline=True)
  await ctx.send(embed=embed)

@client.command()
async def list(ctx):
  await ctx.send(file=discord.File('list.txt'))

client.loop.create_task(change_status())
client.run(os.getenv('BOT_TOKEN'))