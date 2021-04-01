import discord
import os
import requests
import json
from discord.ext import commands
from hosting import host_bot

client = commands.Bot(command_prefix='=', help_command=None)

def indnextl():
  or_abbrev = 'Sem Info'
  nx = requests.get('https://spacelaunchnow.me/api/ll/2.2.0/launch/upcoming/?search=india&format=json')
  nx_json = json.loads(nx.text)
  data = nx_json["results"]
  next = data[0]
  nome = next['name']
  lsp = next['launch_service_provider']
  mission = next['mission']
  descricao = mission['description']
  if descricao == None:
    descricao = "Sem descrição"
  mission_name = mission['name']
  tipo = mission['type']
  orbit = mission['orbit']
  print(orbit)
  print(type(orbit))
  if orbit == None:
    or_abbrev = 'Sem Info'
  else:
    or_abrev = orbit['abbrev']
  provider = lsp['name']
  rocket = next['rocket']
  config = rocket['configuration']
  rocket_ = config['name']
  provider = lsp['name']
  status = next['status']
  status_ = status['abbrev']
  lista = [rocket_, provider, nome, mission_name, or_abbrev, tipo, status_, descricao]
  return lista


def apod_get():
  nx = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={os.getenv('NASA_API_KEY')}')
  data = json.loads(nx.text)
  name = data["title"]
  des = data["explanation"]
  hora = data["date"]
  url = data["url"]
  lista = [url, hora, des, name]
  return lista

def rlnextl():
  or_abbrev = 'Sem Info'
  nx = requests.get('https://spacelaunchnow.me/api/ll/2.2.0/launch/upcoming/?search=lab&format=json')
  nx_json = json.loads(nx.text)
  data = nx_json["results"]
  next = data[0]
  nome = next['name']
  lsp = next['launch_service_provider']
  mission = next['mission']
  descricao = mission['description']
  if descricao == None:
    descricao = "Sem descrição"
  mission_name = mission['name']
  tipo = mission['type']
  orbit = mission['orbit']
  print(orbit)
  print(type(orbit))
  if orbit == None:
    or_abbrev = 'Sem Info'
  else:
    or_abrev = orbit['abbrev']
  provider = lsp['name']
  rocket = next['rocket']
  config = rocket['configuration']
  rocket_ = config['name']
  provider = lsp['name']
  status = next['status']
  status_ = status['abbrev']
  lista = [rocket_, provider, nome, mission_name, or_abbrev, tipo, status_, descricao]
  return lista

def rcnextl():
  or_abbrev = 'Sem Info'
  nx = requests.get('https://spacelaunchnow.me/api/ll/2.2.0/launch/upcoming/?search=roscosmos&format=json')
  nx_json = json.loads(nx.text)
  data = nx_json["results"]
  next = data[0]
  nome = next['name']
  lsp = next['launch_service_provider']
  mission = next['mission']
  descricao = mission['description']
  if descricao == None:
    descricao = "Sem descrição"
  mission_name = mission['name']
  tipo = mission['type']
  orbit = mission['orbit']
  print(orbit)
  print(type(orbit))
  if orbit == None:
    or_abbrev = 'Sem Info'
  else:
    or_abrev = orbit['abbrev']
  provider = lsp['name']
  rocket = next['rocket']
  config = rocket['configuration']
  rocket_ = config['name']
  provider = lsp['name']
  status = next['status']
  status_ = status['abbrev']
  lista = [rocket_, provider, nome, mission_name, or_abbrev, tipo, status_, descricao]
  return lista

def sxnextl():
  or_abbrev = 'Sem Info'
  nx = requests.get('https://spacelaunchnow.me/api/ll/2.2.0/launch/upcoming/?search=spacex&format=json')
  nx_json = json.loads(nx.text)
  data = nx_json["results"]
  next = data[0]
  nome = next['name']
  lsp = next['launch_service_provider']
  mission = next['mission']
  descricao = mission['description']
  if descricao == None:
    descricao = "Sem descrição"
  mission_name = mission['name']
  tipo = mission['type']
  orbit = mission['orbit']
  print(orbit)
  print(type(orbit))
  if orbit == None:
    or_abbrev = 'Sem Info'
  else:
    or_abrev = orbit['abbrev']
  provider = lsp['name']
  rocket = next['rocket']
  config = rocket['configuration']
  rocket_ = config['name']
  provider = lsp['name']
  status = next['status']
  status_ = status['abbrev']
  lista = [rocket_, provider, nome, mission_name, or_abbrev, tipo, status_, descricao]
  return lista

def nextl():
  or_abbrev = 'Sem Info'
  nx = requests.get('https://spacelaunchnow.me/api/ll/2.2.0/launch/upcoming/?format=json')
  nx_json = json.loads(nx.text)
  data = nx_json["results"]
  next = data[0]
  nome = next['name']
  lsp = next['launch_service_provider']
  mission = next['mission']
  descricao = mission['description']
  if descricao == None:
    descricao = "Sem descrição"
  mission_name = mission['name']
  tipo = mission['type']
  orbit = mission['orbit']
  print(orbit)
  print(type(orbit))
  if orbit == None:
    or_abbrev = 'Sem Info'
  else:
    or_abrev = orbit['abbrev']
  provider = lsp['name']
  rocket = next['rocket']
  config = rocket['configuration']
  rocket_ = config['name']
  provider = lsp['name']
  status = next['status']
  status_ = status['abbrev']
  lista = [rocket_, provider, nome, mission_name, or_abbrev, tipo, status_, descricao]
  return lista

def nasanextl():
  or_abbrev = 'Sem Info'
  nx = requests.get('https://spacelaunchnow.me/api/ll/2.2.0/launch/upcoming/?search=nasa&format=json')
  nx_json = json.loads(nx.text)
  data = nx_json["results"]
  next = data[0]
  nome = next['name']
  lsp = next['launch_service_provider']
  mission = next['mission']
  descricao = mission['description']
  if descricao == None:
    descricao = "Sem descrição"
  mission_name = mission['name']
  tipo = mission['type']
  orbit = mission['orbit']
  print(orbit)
  print(type(orbit))
  if orbit == None:
    or_abbrev = 'Sem Info'
  else:
    or_abrev = orbit['abbrev']
  provider = lsp['name']
  rocket = next['rocket']
  config = rocket['configuration']
  rocket_ = config['name']
  provider = lsp['name']
  status = next['status']
  status_ = status['abbrev']
  lista = [rocket_, provider, nome, mission_name, or_abbrev, tipo, status_, descricao]
  return lista

def chnextl():
  or_abbrev = 'Sem Info'
  nx = requests.get('https://spacelaunchnow.me/api/ll/2.2.0/launch/upcoming/?search=china&format=json')
  nx_json = json.loads(nx.text)
  data = nx_json["results"]
  next = data[0]
  nome = next['name']
  lsp = next['launch_service_provider']
  mission = next['mission']
  descricao = mission['description']
  if descricao == None:
    descricao = "Sem descrição"
  mission_name = mission['name']
  tipo = mission['type']
  orbit = mission['orbit']
  print(orbit)
  print(type(orbit))
  if orbit == None:
    or_abbrev = 'Sem Info'
  else:
    or_abrev = orbit['abbrev']
  provider = lsp['name']
  rocket = next['rocket']
  config = rocket['configuration']
  rocket_ = config['name']
  provider = lsp['name']
  status = next['status']
  status_ = status['abbrev']
  lista = [rocket_, provider, nome, mission_name, or_abbrev, tipo, status_, descricao]
  return lista

def arnextl():
  or_abbrev = 'Sem Info'
  nx = requests.get('https://spacelaunchnow.me/api/ll/2.2.0/launch/upcoming/?search=arianespace&format=json')
  nx_json = json.loads(nx.text)
  data = nx_json["results"]
  next = data[0]
  nome = next['name']
  lsp = next['launch_service_provider']
  mission = next['mission']
  descricao = mission['description']
  if descricao == None:
    descricao = "Sem descrição"
  mission_name = mission['name']
  tipo = mission['type']
  orbit = mission['orbit']
  print(orbit)
  print(type(orbit))
  if orbit == None:
    or_abbrev = 'Sem Info'
  else:
    or_abrev = orbit['abbrev']
  provider = lsp['name']
  rocket = next['rocket']
  config = rocket['configuration']
  rocket_ = config['name']
  provider = lsp['name']
  status = next['status']
  status_ = status['abbrev']
  lista = [rocket_, provider, nome, mission_name, or_abbrev, tipo, status_, descricao]
  return lista

def ulanextl():
  or_abbrev = 'Sem Info'
  nx = requests.get('https://spacelaunchnow.me/api/ll/2.2.0/launch/upcoming/?search=united&format=json')
  nx_json = json.loads(nx.text)
  data = nx_json["results"]
  next = data[0]
  nome = next['name']
  lsp = next['launch_service_provider']
  mission = next['mission']
  descricao = mission['description']
  if descricao == None:
    descricao = "Sem descrição"
  mission_name = mission['name']
  tipo = mission['type']
  orbit = mission['orbit']
  print(orbit)
  print(type(orbit))
  if orbit == None:
    or_abbrev = 'Sem Info'
  else:
    or_abrev = orbit['abbrev']
  provider = lsp['name']
  rocket = next['rocket']
  config = rocket['configuration']
  rocket_ = config['name']
  provider = lsp['name']
  status = next['status']
  status_ = status['abbrev']
  lista = [rocket_, provider, nome, mission_name, or_abbrev, tipo, status_, descricao]
  return lista

def asnextl():
  or_abbrev = 'Sem Info'
  nx = requests.get('https://spacelaunchnow.me/api/ll/2.2.0/launch/upcoming/?search=astra&format=json')
  nx_json = json.loads(nx.text)
  data = nx_json["results"]
  next = data[0]
  nome = next['name']
  lsp = next['launch_service_provider']
  mission = next['mission']
  descricao = mission['description']
  if descricao == None:
    descricao = "Sem descrição"
  mission_name = mission['name']
  tipo = mission['type']
  orbit = mission['orbit']
  print(orbit)
  print(type(orbit))
  if orbit == None:
    or_abbrev = 'Sem Info'
  else:
    or_abrev = orbit['abbrev']
  provider = lsp['name']
  rocket = next['rocket']
  config = rocket['configuration']
  rocket_ = config['name']
  provider = lsp['name']
  status = next['status']
  status_ = status['abbrev']
  lista = [rocket_, provider, nome, mission_name, or_abbrev, tipo, status_, descricao]
  return lista

@client.command()
async def indnext(ctx):
  embedVar = indnextl()
  embed = discord.Embed(title=embedVar[2], description=embedVar[7], color=0x00ff95)
  embed.add_field(name='Foguete', value=embedVar[0], inline=True)
  embed.add_field(name='Órbita', value=embedVar[4], inline=True)
  embed.add_field(name='Missão', value=embedVar[3], inline=True)
  embed.add_field(name='Tipo', value=embedVar[5], inline=True)
  embed.add_field(name='Status', value=embedVar[6], inline=True)
  await ctx.send(embed=embed)

@client.command()
async def chnext(ctx):
  embedVar = chnextl()
  embed = discord.Embed(title=embedVar[2], description=embedVar[7], color=0xfbff00)
  embed.add_field(name='Foguete', value=embedVar[0], inline=True)
  embed.add_field(name='Órbita', value=embedVar[4], inline=True)
  embed.add_field(name='Missão', value=embedVar[3], inline=True)
  embed.add_field(name='Tipo', value=embedVar[5], inline=True)
  embed.add_field(name='Status', value=embedVar[6], inline=True)
  await ctx.send(embed=embed)

@client.command()
async def nasanext(ctx):
  embedVar = nasanextl()
  embed = discord.Embed(title=embedVar[2], description=embedVar[7], color=0xff0040)
  embed.add_field(name='Foguete', value=embedVar[0], inline=True)
  embed.add_field(name='Órbita', value=embedVar[4], inline=True)
  embed.add_field(name='Missão', value=embedVar[3], inline=True)
  embed.add_field(name='Tipo', value=embedVar[5], inline=True)
  embed.add_field(name='Status', value=embedVar[6], inline=True)
  await ctx.send(embed=embed)

@client.command()
async def next(ctx):
  embedVar = nextl()
  embed = discord.Embed(title=embedVar[2], description=embedVar[7], color=0xffa82e)
  embed.add_field(name='Foguete', value=embedVar[0], inline=True)
  embed.add_field(name='Órbita', value=embedVar[4], inline=True)
  embed.add_field(name='Missão', value=embedVar[3], inline=True)
  embed.add_field(name='Tipo', value=embedVar[5], inline=True)
  embed.add_field(name='Status', value=embedVar[6], inline=True)
  await ctx.send(embed=embed)

@client.command()
async def sxnext(ctx):
  embedVar = sxnextl()
  embed = discord.Embed(title=embedVar[2], description=embedVar[7], color=0x12e6c6)
  embed.add_field(name='Foguete', value=embedVar[0], inline=True)
  embed.add_field(name='Órbita', value=embedVar[4], inline=True)
  embed.add_field(name='Missão', value=embedVar[3], inline=True)
  embed.add_field(name='Tipo', value=embedVar[5], inline=True)
  embed.add_field(name='Status', value=embedVar[6], inline=True)
  await ctx.send(embed=embed)

@client.command()
async def rlnext(ctx):
  embedVar = rlnextl()
  embed = discord.Embed(title=embedVar[2], description=embedVar[7], color=0xab2045)
  embed.add_field(name='Foguete', value=embedVar[0], inline=True)
  embed.add_field(name='Órbita', value=embedVar[4], inline=True)
  embed.add_field(name='Missão', value=embedVar[3], inline=True)
  embed.add_field(name='Tipo', value=embedVar[5], inline=True)
  embed.add_field(name='Status', value=embedVar[6], inline=True)
  await ctx.send(embed=embed)

@client.command()
async def rcnext(ctx):
  embedVar = rcnextl()
  embed = discord.Embed(title=embedVar[2], description=embedVar[7], color=0x6f00ff)
  embed.add_field(name='Foguete', value=embedVar[0], inline=True)
  embed.add_field(name='Órbita', value=embedVar[4], inline=True)
  embed.add_field(name='Missão', value=embedVar[3], inline=True)
  embed.add_field(name='Tipo', value=embedVar[5], inline=True)
  embed.add_field(name='Status', value=embedVar[6], inline=True)
  await ctx.send(embed=embed)

@client.command()
async def ulanext(ctx):
  embedVar = ulanextl()
  embed = discord.Embed(title=embedVar[2], description=embedVar[7], color=0x6f00ff)
  embed.add_field(name='Foguete', value=embedVar[0], inline=True)
  embed.add_field(name='Órbita', value=embedVar[4], inline=True)
  embed.add_field(name='Missão', value=embedVar[3], inline=True)
  embed.add_field(name='Tipo', value=embedVar[5], inline=True)
  embed.add_field(name='Status', value=embedVar[6], inline=True)
  await ctx.send(embed=embed)

@client.command()
async def asnext(ctx):
  embedVar = asnextl()
  embed = discord.Embed(title=embedVar[2], description=embedVar[7], color=0x6f00ff)
  embed.add_field(name='Foguete', value=embedVar[0], inline=True)
  embed.add_field(name='Órbita', value=embedVar[4], inline=True)
  embed.add_field(name='Missão', value=embedVar[3], inline=True)
  embed.add_field(name='Tipo', value=embedVar[5], inline=True)
  embed.add_field(name='Status', value=embedVar[6], inline=True)
  await ctx.send(embed=embed)

@client.command()
async def arnext(ctx):
  embedVar = arnextl()
  embed = discord.Embed(title=embedVar[2], description=embedVar[7], color=0x6f00ff)
  embed.add_field(name='Foguete', value=embedVar[0], inline=True)
  embed.add_field(name='Órbita', value=embedVar[4], inline=True)
  embed.add_field(name='Missão', value=embedVar[3], inline=True)
  embed.add_field(name='Tipo', value=embedVar[5], inline=True)
  embed.add_field(name='Status', value=embedVar[6], inline=True)
  await ctx.send(embed=embed)

@client.command()
async def esanext(ctx):
  embedVar = esanextl()
  embed = discord.Embed(title=embedVar[2], description=embedVar[7], color=0x6f00ff)
  embed.add_field(name='Foguete', value=embedVar[0], inline=True)
  embed.add_field(name='Órbita', value=embedVar[4], inline=True)
  embed.add_field(name='Missão', value=embedVar[3], inline=True)
  embed.add_field(name='Tipo', value=embedVar[5], inline=True)
  embed.add_field(name='Status', value=embedVar[6], inline=True)
  await ctx.send(embed=embed)

@client.command()
async def apod(ctx):
  # lista = [url, hora, des, name]
  act = apod_get()
  embed = discord.Embed(title=f'{act[3]} // {act[1]}', description=act[2], url=act[0], color=0xBDFDFF)
  embed.set_image(url=act[0])
  await ctx.send(embed=embed)

@client.command()
async def help(ctx):
  help_text = '''**LISTA DE COMANDOS**
  =help : Lista de Comandos
  =indnext : Próximo lançamento da ISRO
  =chnext : Próximo lançamento da China
  =nasanext : Próximo lançamento da NASA
  =sxnext : Próximo lançamento da SpaceX
  =rlnext : Próximo lançamento da Rocket Lab
  =rcnext : Próximo lançamento da Roscosmos
  =ulanext : Próximo lançamento da ULA
  =asnext : Próximo lançamento da Astra
  =arnext : Próximo lançamento do Arianespace Group
  
  =next : Próximo lançamento
  =apod : Imagem do dia pela NASA
  
  Se um comando falhar, é por que um dos parâmetros que o bot mostra está **nulo** na resposta da API. Isso significa que aquele parâmetro ainda não foi definido, e provavelmente o lançamento ainda está longe de acontecer. Quando a data de lançamento estiver próximo, com quase total certeza ele vai aparecer
  
  Criado por .Francisco Pessoa#8327'''
  await ctx.send(help_text)
keep_alive()
client.run(os.getenv('BOT_TOKEN'))
