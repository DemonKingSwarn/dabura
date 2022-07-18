from .sneakies import SneakyCatcher


def setup(bot):
    bot.add_cog(
        SneakyCatcher(
            bot, guild_id=947394369198116864, disposal_channel=947561997262794752
        )
    )
