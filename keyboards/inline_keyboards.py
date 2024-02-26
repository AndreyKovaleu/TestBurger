from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from lexicon.lexicon_ru import LEXICON_INLINE_BUTTON_RU

beef_burgers_button = InlineKeyboardButton(text=LEXICON_INLINE_BUTTON_RU["beef_burgers"], callback_data="beef_burgers")
chicken_and_fish_burgers_button = InlineKeyboardButton(text=LEXICON_INLINE_BUTTON_RU["chicken_and_fish_burgers"], callback_data="chicken_and_fish_burgers")
rolls_button = InlineKeyboardButton(text=LEXICON_INLINE_BUTTON_RU["rolls"], callback_data="rolls")
snacks_button = InlineKeyboardButton(text=LEXICON_INLINE_BUTTON_RU["snacks"], callback_data="snacks")
shrimps_button = InlineKeyboardButton(text=LEXICON_INLINE_BUTTON_RU["shrimps"], callback_data="shrimps")
cold_drinks_button = InlineKeyboardButton(text=LEXICON_INLINE_BUTTON_RU["cold_drinks"], callback_data="cold_drinks")
hot_drinks_button = InlineKeyboardButton(text=LEXICON_INLINE_BUTTON_RU["hot_drinks"], callback_data="hot_drinks")
dessert_button = InlineKeyboardButton(text=LEXICON_INLINE_BUTTON_RU["dessert"], callback_data="dessert")
sauces_button = InlineKeyboardButton(text=LEXICON_INLINE_BUTTON_RU["sauces"], callback_data="sauces")
other_button = InlineKeyboardButton(text=LEXICON_INLINE_BUTTON_RU["other"], callback_data="other")
website_button = InlineKeyboardButton(text=LEXICON_INLINE_BUTTON_RU["website"], url="https://www.linkedin.com/in/andrey-kovaleu/")
author_button = InlineKeyboardButton(text=LEXICON_INLINE_BUTTON_RU["author"], url="https://t.me/AndreyDevs")

menu_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [beef_burgers_button],
        [chicken_and_fish_burgers_button],
        [snacks_button, sauces_button],
        [rolls_button, shrimps_button],
        [cold_drinks_button],
        [hot_drinks_button],
        [dessert_button, other_button],
        [author_button]
    ]
)

about_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [website_button],
        [author_button]
    ]
)

# order_inline_keyboard