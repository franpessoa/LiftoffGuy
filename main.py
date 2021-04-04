import discord
import os
import requests
import json
import company
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


@client.command()
async def indnext(ctx, arg):
  embedVar = nextl()
  embed = discord.Embed(title=embedVar[2], description=embedVar[7], color=0x00ff95)
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
  =add : Adicione o bot em seu server
  =github : Github do projeto
  
  =indnext : Próximo lançamento da ISRO
  =chnext : Próximo lançamento da China
  =nasanext : Próximo lançamento da NASA
  =sxnext : Próximo lançamento da SpaceX
  =rlnext : Próximo lançamento da Rocket Lab
  =rcnext : Próximo lançamento da Roscosmos
  =ulanext : Próximo lançamento da ULA
  =asnext : Próximo lançamento da Astra (Comando Falho)
  =arnext : Próximo lançamento do Arianespace Group
  
  =next : Próximo lançamento
  =apod : Imagem do dia pela NASA
  
  Se um comando falhar, é por que um dos parâmetros que o bot mostra está **nulo** na resposta da API. Isso significa que aquele parâmetro ainda não foi definido, e provavelmente o lançamento ainda está longe de acontecer.
  
  Criado por .Francisco Pessoa#8327'''
  await ctx.send(help_text)

@client.command()
async def add(ctx):
  await ctx.send('''Adicione-me em seu server!
  https://discord.com/api/oauth2/authorize?client_id=817438170097385523&permissions=8&scope=bot''')

@client.command()
async def github(ctx):
  await ctx.send('''Github do projeto:
  https://github.com/franpessoa/LOXLoadingComplete''')

keep_alive()
client.run(os.getenv('BOT_TOKEN'))
