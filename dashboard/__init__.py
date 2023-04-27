from redbot.core.bot import Red

from .dashboard import Dashboard


async def setup(bot: Red):
    await bot.add_cog(Dashboard(bot))
