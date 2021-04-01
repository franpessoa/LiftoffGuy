from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "LOXLoadingComplete#3954 https://discord.com/api/oauth2/authorize?client_id=817438170097385523&permissions=8&scope=bot"

def run():
  app.run(host='0.0.0.0',port=8080)

def host_bot():
    t = Thread(target=run)
    t.start()
