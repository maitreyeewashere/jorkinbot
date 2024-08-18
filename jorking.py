import re
import discord
from dotenv import load_dotenv

from discord.ext import *

# Replace with your regenerated bot token
load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def transform(sentence):
    pattern = r"(?:^|\s)(I| Im | I am|i am|im|i'm)\s+(\w+)\s+(.+?)(?:\.|\s|$)"
    match = re.search(pattern, sentence, re.IGNORECASE)

    

    if match:
        verb = match.group(2)
        action = match.group(3)

        #print(verb, action)

        # Verb modification improvements
        if verb.endswith('e'):
            verb = verb[:-1] + 'in\''
        else:
            verb = verb + 'in\''

        return f"you're at da club, straight up {verb} it, and by 'it', well let's just say, your '{action}'."
    else:
        return sentence


@client.event
async def on_message(message):
    # Avoid responding to the bot's own messages
    if message.author == client.user:
        return

    # Attempt to transform the sentence
    transformed = transform(message.content)
    
    if transformed != message.content:
        await message.channel.send(transformed)

# Run the bot
client.run(TOKEN)
