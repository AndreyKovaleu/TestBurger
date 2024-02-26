from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

from lexicon.lexicon_ru import LEXICON_RU, LEXICON_BUTTON_RU
from keyboards.keyboards import (main_keyboard, news_keyboard,
                                 settings_keyboard, help_keyboard)
from keyboards.inline_keyboards import (menu_inline_keyboard, about_inline_keyboard,
                                        beef_burgers_keyboard, chicken_and_fish_burgers_keyboard,
                                        rolls_keyboard, snacks_keyboard,
                                        shrimps_keyboard, cold_drinks_keyboard,
                                        hot_drinks_keyboard, dessert_keyboard,
                                        sauces_keyboard, other_keyboard)

router = Router()


# Обработка нажатия на кнопки меню и обычные кнопки
@router.message(CommandStart())
@router.message(F.text == LEXICON_BUTTON_RU["home"])
async def command_start_handler(message: Message):
    await message.answer(text=LEXICON_RU["/start"],
                         reply_markup=main_keyboard)


@router.message(Command("menu"))
@router.message(F.text == LEXICON_BUTTON_RU["menu"])
async def command_catalog_handler(message: Message):
    await message.answer(text=LEXICON_RU["/menu"],
                         reply_markup=menu_inline_keyboard)


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
    await message.answer(text=LEXICON_RU["/about"],
                         reply_markup=about_inline_keyboard)


# Обработка нажатия на инлайн-кнопки меню
@router.callback_query(F.data == "beef_burgers")
async def beef_burgers_callback_handler(call: CallbackQuery):
    await call.message.answer(text=LEXICON_RU["beef_burgers"],
                              reply_markup=beef_burgers_keyboard)
    await call.answer()


@router.callback_query(F.data == "chicken_and_fish_burgers")
async def chicken_and_fish_burgers_callback_handler(call: CallbackQuery):
    await call.message.answer(text=LEXICON_RU["chicken_and_fish_burgers"],
                              reply_markup=chicken_and_fish_burgers_keyboard)
    await call.answer()


@router.callback_query(F.data == "rolls")
async def rolls_callback_handler(call: CallbackQuery):
    await call.message.answer(text=LEXICON_RU["rolls"],
                              reply_markup=rolls_keyboard)
    await call.answer()


@router.callback_query(F.data == "snacks")
async def snacks_callback_handler(call: CallbackQuery):
    await call.message.answer(text=LEXICON_RU["snacks"],
                              reply_markup=snacks_keyboard)
    await call.answer()


@router.callback_query(F.data == "shrimps")
async def shrimps_callback_handler(call: CallbackQuery):
    await call.message.answer(text=LEXICON_RU["shrimps"],
                              reply_markup=shrimps_keyboard)
    await call.answer()


@router.callback_query(F.data == "cold_drinks")
async def cold_drinks_callback_handler(call: CallbackQuery):
    await call.message.answer(text=LEXICON_RU["cold_drinks"],
                              reply_markup=cold_drinks_keyboard)
    await call.answer()


@router.callback_query(F.data == "hot_drinks")
async def hot_drinks_callback_handler(call: CallbackQuery):
    await call.message.answer(text=LEXICON_RU["hot_drinks"],
                              reply_markup=hot_drinks_keyboard)
    await call.answer()


@router.callback_query(F.data == "dessert")
async def dessert_callback_handler(call: CallbackQuery):
    await call.message.answer(text=LEXICON_RU["dessert"],
                              reply_markup=dessert_keyboard)
    await call.answer()


@router.callback_query(F.data == "sauces")
async def sauces_callback_handler(call: CallbackQuery):
    await call.message.answer(text=LEXICON_RU["sauces"],
                              reply_markup=sauces_keyboard)
    await call.answer()


@router.callback_query(F.data == "other")
async def other_callback_handler(call: CallbackQuery):
    await call.message.answer(text=LEXICON_RU["other"],
                              reply_markup=other_keyboard)
    await call.answer()
