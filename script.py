import discord
import re

# Initialise le client Discord avec toutes les intentions activées
intents = discord.Intents().all()
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.id == 603616390020202529: # Remplacez CHANNEL_ID par l'ID du channel sur lequel vous souhaitez que le bot fonctionne
        twitter_url_pattern = r'https?://(www\.)?twitter\.com/.+?/status/\d+'
        twitter_url_regex = re.compile(twitter_url_pattern)

        if twitter_url_regex.search(message.content):
            tweet_url = twitter_url_regex.search(message.content).group(0)
            fx_tweet_url = tweet_url.replace('https://twitter.com/', 'https://fxtwitter.com/')
            reply_message = f"@silent Voici le lien FX pour le tweet : {fx_tweet_url}"
            await message.reply(reply_message, mention_author=False)
            await message.edit(suppress=True)

client.run('MTA4MDA1MjAyNjcyNzIwNjk2Mg.Ge-kQ3.rpU2LObnVGexn0kT137X9HlaBjNjxQJr3advEI') # Remplacez BOT_TOKEN par le jeton de votre bot Discord
