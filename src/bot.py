import discord
from discord.ext import commands
from credentials import DISCORD_BOT_TOKEN
from llm import TexasJack

from utils import fetch_bad_words

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='!tj ', intents=intents)

llm = TexasJack()

BAD_WORDS = fetch_bad_words()


@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')


@bot.listen('on_message')
async def chat(message):

    # Chat command
    if message.content.startswith('tj '):
        response = llm.chat(message.content[3:])
        await message.channel.send(response)

    # If it's vulgar
    for word in BAD_WORDS:
        if word in message.content.lower().split(' '):
            response = llm.warn_vulgar(message.content)
            await message.channel.send(response)

        
@bot.command()
async def reset(ctx):
    await ctx.send(llm.flush_memory())


@bot.command()
async def memory(ctx):

    if len(llm.get_memory()) == 0:
        await ctx.send(f'```No memory found.```')
    else:
        await ctx.send(f'```{llm.get_memory()}```')


def start_server():
    bot.run(DISCORD_BOT_TOKEN)


def main():
    start_server()


if __name__ == "__main__":
    main()
