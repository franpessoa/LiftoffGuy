import discord
import apirequest
import json
import requests
import asyncio
from discord.ext import commands
from dotenv import load_dotenv

# CHANGE THIS #
nasa_api_key = load_dotenv("NASA_API_KEY")
bot_token = load_dotenv("BOT_TOKEN")

client = commands.Bot(command_prefix='=', help_command=None)

async def change_status():
  await client.wait_until_ready()
  while not client.is_closed():
    status = "em {} servers".format(len(client.guilds))
    await client.change_presence(activity=discord.Game(name=status))
    await asyncio.sleep(6)


def apod_get():
  nx = requests.get('https://api.nasa.gov/planetary/apod?api_key={}'.format(nasa_api_key))
  data = json.loads(nx.text)
  name = data["title"]
  des = data["explanation"]
  hora = data["date"]
  url = data["url"]
  lista = [url, hora, des, name]
  return lista

@client.command()
async def nl(ctx):
  url = apirequest.no_search()
  embedVar = apirequest.request(url)
  if not embedVar:
    await ctx.send("{} Tivemos um erro :(".format(ctx.author.mention))
  else:
    des = '''{}\n
    Foguete: {}
    Órbita: {}
    Missão: {}
    Tipo: {}
    Status: {}
    Pad: {}'''.format(embedVar[7], embedVar[0], embedVar[4], embedVar[3], embedVar[5], embedVar[6], embedVar[8])
    embed = discord.Embed(title=embedVar[2], description=des, color=0xFFDD91)
    await ctx.send(ctx.author.mention, embed=embed)

@client.command()
async def c(ctx, argument):
  url = apirequest.company_name(argument)
  embedVar = apirequest.request(url)
  if not embedVar:
    await ctx.send("{} Tivemos um erro :(".format(ctx.author.mention))
  else:
    des = '''{}\n
    Foguete: {}
    Órbita: {}
    Missão: {}
    Tipo: {}
    Status: {}
    Pad: {}'''.format(embedVar[7], embedVar[0], embedVar[4], embedVar[3], embedVar[5], embedVar[6], embedVar[8])
    embed = discord.Embed(title=embedVar[2], description=des, color=0xFFDD91)
    await ctx.send(ctx.author.mention, embed=embed)

@client.command()
async def apod(ctx):
  act = apod_get()
  embed = discord.Embed(title='{} // {}'.format(act[3], act[1]), description=act[2], url=act[0], color=0xBDFDFF)
  embed.set_image(url=act[0])
  await ctx.send(embed=embed)

@client.command()
async def help(ctx):
  help_text = '''**COMANDOS:**
  =help : Lista de Comandos
  =add : Adicione o bot em seu server
  =github : Github do projeto
  =site : Site do bot

  =nl : Próximo lançamento
  =c {companhia} : Próximo lançamento de determinada companhia
  =apod : Imagem do dia pela NASA
  =ls : Lista de companhias suportadas
  =iss : Posição atual da ISS'''
  embed = discord.Embed(title='Comando de ajuda', description=help_text, color=0xCC0000)
  await ctx.send(ctx.author.mention, embed=embed)

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
async def iss(ctx):
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
async def ls(ctx):
  await ctx.send(file=discord.File('list.txt'))

client.loop.create_task(change_status())
client.run(bot_token)