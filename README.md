# LiftoffGuy
Bot para o discord feito com a biblioteca discord.py.
Além dá própria discord.py não precisa de nenhuma outra biblioteca para funcionar

Se um comando falhar, é por que um dos parâmetros que o bot mostra está **nulo** na resposta da API. 
Isso significa que aquele parâmetro ainda não foi definido, e provavelmente o lançamento ainda está longe de acontecer. 
Quando a data de lançamento estiver próximo, com quase total certeza ele vai aparecer

Para que ele funcione no seu computador, altere as linhas 9 e 10 do ```main.py```, colocando sua key da API da NASA (https://api.nasa.gov/), e o token do seu bot (https://discord.com/developers/)

Remova o texto e coloque seus tokens

Para adicionar o bot, https://discord.com/api/oauth2/authorize?client_id=817438170097385523&permissions=8&scope=bot

Site: https://arco.coop.br/~franpessoa/lox-loading-complete.html

## O mapa da ISS
O script para o mapa de onde a ISS está cria uma página HTML em um diretó
rio, que pode ser alterado na linha **31**, o padrão é ```./www/index.html```.
Esse código é complementar ao bot, e não precisa ser rodado junto. Ele é feito com a lib ```folium``` que precisa ser instalada.\
O resultado: https://arco.coop.br/~franpessoa/iss/

## Instalações
Para o bot só, é só usar:

```
pip install discord
```

O mapa da ISS precisa da folium, uma biblioteca que eu usei para fazer o mapa:

```
pip install folium
```

As outras bibliotecas são built-in no Python

## Rodando o mapa [Linux]
Para rodar o script do mapa, coloque o shell script e o script Python na mesma pasta, e utilize
```
source ~/diretorio/iss-map.sh
```

Lembrando que o ~ é sua /home/user/

## Compatibilidade
Tanto o bot quanto o script do mapa rodam em um servidor com Python v3.5
