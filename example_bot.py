import discord
import os
from markov import make_random_text

client = discord.Client()

@client.event
async def on_ready():
    print('alive')
    pass

@client.event
async def on_message(message):
    if message.author == client.user:
        print('Message Recieved')
        return
    
    if message.content.startswith('Speak!'):
        print('Message Received')
        await message.channel.send(make_random_text())

TOKEN = os.getenv('DISCORD_TOKEN')

client.run(TOKEN)