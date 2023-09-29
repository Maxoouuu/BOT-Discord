import discord
import re
from dotenv import load_dotenv
import os

load_dotenv()  # Charge les variables d'environnement à partir du fichier .env

# Initialise le client Discord avec toutes les intentions activées
intents = discord.Intents().all()
client = discord.Client(intents=intents)

channel_id = os.getenv("CHANNEL_ID")  # l'ID du channel sur lequel vous souhaitez que le bot fonctionne
bot_token = os.getenv("BOT_TOKEN")

print(f"Channel ID: {channel_id}")
print(f"Bot Token: {bot_token}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.id == int(channel_id):
        url_pattern = r'https?://(www\.)?(twitter\.com|x\.com)/.+?/status/\d+'
        url_regex = re.compile(url_pattern)

        match = url_regex.search(message.content)
        if match:
            url = match.group(0)
            fx_url = url.replace('https://twitter.com/', 'https://fxtwitter.com/')
            fx_url = fx_url.replace('https://x.com/', 'https://fxtwitter.com/')
            reply_message = f"@silent Voici le lien FX pour le tweet : {fx_url}"
            await message.reply(reply_message, mention_author=False)
            await message.edit(suppress=True)

client.run(bot_token)