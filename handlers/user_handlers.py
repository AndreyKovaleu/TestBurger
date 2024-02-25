from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from lexicon.lexicon_ru import LEXICON_RU, LEXICON_BUTTON_RU
from keyboards.keyboards import (main_keyboard, news_keyboard,
                                 settings_keyboard, help_keyboard)

router = Router()


@router.message(CommandStart())
@router.message(F.text == LEXICON_BUTTON_RU["home"])
async def command_start_handler(message: Message):
    await message.answer(text=LEXICON_RU["/start"],
                         reply_markup=main_keyboard)


@router.message(Command("menu"))
@router.message(F.text == LEXICON_BUTTON_RU["menu"])
async def command_catalog_handler(message: Message):
    await message.answer(text=LEXICON_RU["/menu"])


@router.message(Command("cart"))
@router.message(F.text == LEXICON_BUTTON_RU["cart"])
async def command_cart_handler(message: Message):
    await message.answer(text=LEXICON_RU["/cart"])


@router.message(Command("history"))
@router.message(F.text == LEXICON_BUTTON_RU["history"])
async def command_history_handler(message: Message):
    await message.answer(text=LEXICON_RU["/history"])


@router.message(Command("news"))
@router.message(F.text == LEXICON_BUTTON_RU["news"])
async def command_news_handler(message: Message):
    await message.answer(text=LEXICON_RU["/news"],
                         reply_markup=news_keyboard)


@router.message(Command("settings"))
@router.message(F.text == LEXICON_BUTTON_RU["settings"])
async def command_settings_handler(message: Message):
    await message.answer(text=LEXICON_RU["/settings"],
                         reply_markup=settings_keyboard)


@router.message(Command("help"))
@router.message(F.text == LEXICON_BUTTON_RU["help"])
async def command_help_handler(message: Message):
    await message.answer(text=LEXICON_RU["/help"],
                         reply_markup=help_keyboard)


@router.message(Command("about"))
async def command_about_handler(message: Message):
    await message.answer(text=LEXICON_RU["/about"])
