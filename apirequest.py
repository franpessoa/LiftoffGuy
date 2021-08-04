import requests
import json

def company_name(nome):
  cnome = ' '
  if nome.lower() == 'ula': cnome = 'United'
  elif nome.lower() == 'india': cnome = 'india'
  elif nome.lower() == 'isro': cnome = 'india'
  elif nome.lower() == 'china': cnome = 'china'
  elif nome.lower() == 'rocket_lab': cnome = 'lab'
  elif nome.lower() == 'lab': cnome = 'lab'
  elif nome.lower() == 'spacex': cnome = 'spacex'
  elif nome.lower() == 'astra': cnome = 'astra'
  elif nome.lower() == 'nasa': cnome = 'nasa'
  elif nome.lower() == 'usa': cnome = 'nasa'
  elif nome.lower() == 'arianespace': cnome = 'arianespace'
  elif nome.lower() == 'ariane': cnome = 'arianespace'
  elif nome.lower() == 'russia': cnome = 'roscosmos'
  elif nome.lower() == 'roscosmos': cnome = 'roscosmos'
  url = company_url(cnome)
  return url

def no_search():
  url = 'https://spacelaunchnow.me/api/ll/2.2.0/launch/upcoming/?format=json'
  return url

def company_url(urlname):
  url = 'https://spacelaunchnow.me/api/ll/2.2.0/launch/upcoming/?search={}&format=json'.format(urlname)
  return url

def request(url):
  try:
    nx = requests.get(url)
    nx_json = json.loads(nx.text)
    data = nx_json["results"]
    nextc = data[0]
    pad = nextc['pad']
    pad_name = pad['name']
    nome = nextc['name']
    lsp = nextc['launch_service_provider']
    mission = nextc['mission']
    descricao = mission['description']
    mission_name = mission['name']
    tipo = mission['type']
    orbit = mission['orbit']
    or_abbrev = orbit['abbrev']
    provider = lsp['name']
    rocket = nextc['rocket']
    config = rocket['configuration']
    rocket_ = config['name']
    provider = lsp['name']
    status = next['status']
    status_ = status['abbrev']
    lista = [rocket_, provider, nome, mission_name, or_abbrev, tipo, status_, descricao, pad_name]
    return lista
  except:
    return False