import json
import requests

def next(url):
  or_abbrev = 'Sem Info'
  nx = requests.get(url)
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