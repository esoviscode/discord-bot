from nextcord import User

from dnd_bot.dc.ui.messager import Messager


async def get_user_name_by_id(user_id: int) -> str:
    bot = Messager.bot

    user: User = await bot.fetch_user(user_id)

    return user.name
