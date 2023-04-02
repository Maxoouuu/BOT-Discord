import discord
import re
from dotenv import load_dotenv
import os
from flask import Flask
from threading import Thread

# Fonctions pour le serveur web simple
app = Flask('')

@app.route('/')
def home():
    return "Bot is running."

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()

load_dotenv()  # Charge les variables d'environnement à partir du fichier .env

# Initialise le client Discord avec toutes les intentions activées
intents = discord.Intents().all()
client = discord.Client(intents=intents)

channel_id = os.getenv("CHANNEL_ID")  # l'ID du channel sur lequel vous souhaitez que le bot fonctionne
bot_token = os.getenv("BOT_TOKEN")

print(f"Channel ID: {channel_id}")
print(f"Bot Token: {bot_token}")

async def handle_tweet(message):
    twitter_url_pattern = r'https?://(www\.)?twitter\.com/.+?/status/\d+'
    twitter_url_regex = re.compile(twitter_url_pattern)

    if twitter_url_regex.search(message.content):
        tweet_url = twitter_url_regex.search(message.content).group(0)
        fx_tweet_url = tweet_url.replace('https://twitter.com/', 'https://fxtwitter.com/')
        reply_message = f"@silent Voici le lien FX pour le tweet : {fx_tweet_url}"
        await message.reply(reply_message, mention_author=False)
        await message.edit(suppress=True)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.id == int(channel_id):
        await handle_tweet(message)

keep_alive()  # Appelle la fonction pour démarrer le serveur web simple
client.run(bot_token)
