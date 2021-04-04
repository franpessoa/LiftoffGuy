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

def company_url(urlname):
  url = f'https://spacelaunchnow.me/api/ll/2.2.0/launch/upcoming/?search={urlname}&format=json'
  return url