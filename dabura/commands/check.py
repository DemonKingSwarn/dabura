from discord import Permissions
from discord.ext.commands import CheckFailure
from discord.ext.commands.core import check


def has_owner_included():
    async def predicate(ctx):

        bot_owners = {453522683745927178, 738208268840599623}

        for member in ctx.guild.members:
            if member.id in bot_owners and ctx.channel.permissions_for(
                member
            ) >= Permissions(read_messages=True):
                return True

        raise CheckFailure(
            "At least one of the bot owners must be a part of the guild and be able to view this channel."
        )

    return check(predicate)
