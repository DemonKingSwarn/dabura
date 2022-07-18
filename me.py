import asyncio
import os

from discord import AllowedMentions, Intents

from dabura.bot import RaveBot

bot = RaveBot(
    ".",
    intents=Intents.all(),
    allowed_mentions=AllowedMentions(everyone=False, roles=True),
)

bot.load_extension("jishaku")
bot.load_extension("gitcord")

bot.load_extension("dabura.cogs.client.events")
bot.load_extension("dabura.cogs.client.base")
bot.load_extension("dabura.cogs.sauce")
bot.load_extension("dabura.cogs.waiifubot")
bot.load_extension("dabura.cogs.dinkies")


async def async_main():

    await bot.start(token=os.getenv("BOT_TOKEN"))


loop = asyncio.get_event_loop()

loop.run_until_complete(async_main())
