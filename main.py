import discord
import os
import apirequest
from discord.ext import commands
from hosting import host_bot

client = commands.Bot(command_prefix='=', help_command=None)

def apod_get():
  nx = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={os.getenv(NASA_API_KEY)}')
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
  embedVar = apirequest.next(url)
  embed = discord.Embed(title=embedVar[2], description=embedVar[7], color=0x00ff95)
  embed.add_field(name='Foguete', value=embedVar[0], inline=True)
  embed.add_field(name='Órbita', value=embedVar[4], inline=True)
  embed.add_field(name='Missão', value=embedVar[3], inline=True)
  embed.add_field(name='Tipo', value=embedVar[5], inline=True)
  embed.add_field(name='Status', value=embedVar[6], inline=True)
  await ctx.send(embed=embed)

@client.command()
async def company(ctx, argument):
  url = apirequest.company_name(argument)
  embedVar = apirequest.next(url)
  embed = discord.Embed(title=embedVar[2], description=embedVar[7], color=0x00ff95)
  embed.add_field(name='Foguete', value=embedVar[0], inline=True)
  embed.add_field(name='Órbita', value=embedVar[4], inline=True)
  embed.add_field(name='Missão', value=embedVar[3], inline=True)
  embed.add_field(name='Tipo', value=embedVar[5], inline=True)
  embed.add_field(name='Status', value=embedVar[6], inline=True)
  await ctx.send(embed=embed)

@client.command()
async def apod(ctx):
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
  
  =next : Próximo lançamento
  =company {compania} : Próximo lançamento de determinada companhia
  =apod : Imagem do dia pela NASA
  =list : Lista de companhias suportadas
  
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

@client.command()
async def list(ctx):
  await ctx.send_file('list.txt')

host_bot()
client.run(os.getenv('BOT_TOKEN'))
