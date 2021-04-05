def company_name(nome):
  cnome = ' '
  if nome.lower() == 'ula': cnome = 'United'
  if nome.lower() == 'india': cnome = 'india'
  if nome.lower() == 'isro': cnome = 'india'
  if nome.lower() == 'china': cnome = 'china'
  if nome.lower() == 'rocket_lab': cnome = 'lab'
  if nome.lower() == 'lab': cnome = 'lab'
  if nome.lower() == 'spacex': cnome = 'spacex'
  if nome.lower() == 'astra': cnome = 'astra'
  if nome.lower() == 'nasa': cnome = 'nasa'
  if nome.lower() == 'usa': cnome = 'nasa'
  if nome.lower() == 'arianespace': cnome = 'arianespace'
  if nome.lower() == 'ariane': cnome = 'arianespace'
  if nome.lower() == 'russia': cnome = 'roscosmos'
  if nome.lower() == 'roscosmos': cnome = 'roscosmos'
  url = company_url(cnome)
  return url

def no_search():
  url = 'https://spacelaunchnow.me/api/ll/2.2.0/launch/upcoming/?format=json'
  return

def company_url(urlname):
  url = f'https://spacelaunchnow.me/api/ll/2.2.0/launch/upcoming/?search={urlname}&format=json'
  return url

def request(url):
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