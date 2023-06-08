import discord
import os
from dotenv import load_dotenv
import time
import random

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

#bot = commands.Bot(command_prefix = ".") #Command prefix, needs adding

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    print(message.author)
    print(message.content)
    print()
    if message.author == client.user:
        return

    # On command .f Hello
    if message.content.startswith('.f hello'):
        await message.channel.send('Hi.')

    # On command .f help
    if message.content.startswith('.f help'):
        await message.channel.send('.f [command] | lore | help | hello')

    # On command .f quote
    if message.content.startswith('.f quote'):
        with open("quotes.txt", "r") as quotes:           
            quote = random.choice(quotes.read().splitlines()) 
            await message.channel.send(quote)



TOKEN = os.getenv('TOKEN')
client.run(TOKEN)