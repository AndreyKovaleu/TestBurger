from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

from lexicon.lexicon_ru import LEXICON_COMMANDS_RU


async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(
            command=command,
            description=description
        ) for command, description in LEXICON_COMMANDS_RU.items()
    ]

    await bot.set_my_commands(commands=main_menu_commands,
                              scope=BotCommandScopeDefault())
