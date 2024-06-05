import settings
import discord
import requests
from discord.ext import commands

def run():
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix = "!", intents = intents)

    @bot.event
    async def on_ready():
        print(bot.user)
        print(bot.user.id)
        print("__________________")

    @bot.command()
    async def live(ctx, channelName = "Which channel?"):
        contents = requests.get('https://www.twitch.tv/' +channelName).content.decode('utf-8')

        if 'isLiveBroadcast' in contents: 
            await ctx.send(channelName + ' is live')
        elif channelName == "Which channel?":
            await ctx.send(channelName)
        else:
            await ctx.send(channelName + ' is not live')

    bot.run(settings.TOKEN)

if __name__ == "__main__":
    run()
