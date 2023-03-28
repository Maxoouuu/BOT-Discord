import discord
import re
import os

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    channel_id = os.getenv("CHANNEL_ID") # l'ID du channel sur lequel vous souhaitez que le bot fonctionne
    bot_token = os.getenv("BOT_TOKEN")
    if message.channel.id == int(channel_id):
        twitter_url_pattern = r'https?://(www\.)?twitter\.com/.+?/status/\d+'
        twitter_url_regex = re.compile(twitter_url_pattern)

        if twitter_url_regex.search(message.content):
            tweet_url = twitter_url_regex.search(message.content).group(0)
            fx_tweet_url = tweet_url.replace('https://twitter.com/', 'https://fxtwitter.com/')
            reply_message = f"@silent Voici le lien FX pour le tweet : {fx_tweet_url}"
            await message.reply(reply_message, mention_author=False)
            await message.edit(suppress=True)

client.run(bot_token) # le jeton de votre bot Discord
