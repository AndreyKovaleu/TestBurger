import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from config_data.config import Config, load_config
from keyboards.set_menu import set_main_menu
from handlers import router as main_handlers_router


async def main() -> None:
    config: Config = load_config(".env")

    bot = Bot(token=config.tg_bot.token, parse_mode=ParseMode.HTML)
    dp = Dispatcher()

    dp.workflow_data.update({"admin_id": config.tg_bot.admin_ids[0]})
    dp.include_router(main_handlers_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await set_main_menu(bot)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - [%(levelname)s] - %(name)s - "
                                                   "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
    asyncio.run(main())
