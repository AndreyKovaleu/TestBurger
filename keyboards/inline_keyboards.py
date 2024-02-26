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
forward_beef_burgers_button = InlineKeyboardButton(text=LEXICON_INLINE_BUTTON_RU["forward"], callback_data="forward_beef_burgers")
back_beef_burgers_button = InlineKeyboardButton(text=LEXICON_INLINE_BUTTON_RU["back"], callback_data="back_beef_burgers")
forward_chicken_and_fish_burgers_button = InlineKeyboardButton(text=LEXICON_INLINE_BUTTON_RU["forward"], callback_data="forward_chicken_and_fish_burgers")
back_chicken_and_fish_burgers_button = InlineKeyboardButton(text=LEXICON_INLINE_BUTTON_RU["back"], callback_data="back_chicken_and_fish_burgers")
forward_rolls_button = InlineKeyboardButton(text=LEXICON_INLINE_BUTTON_RU["forward"], callback_data="forward_rolls")
back_rolls_button = InlineKeyboardButton(text=LEXICON_INLINE_BUTTON_RU["back"], callback_data="back_rolls")
forward_snacks_button = InlineKeyboardButton(text=LEXICON_INLINE_BUTTON_RU["forward"], callback_data="forward_snacks")
back_snacks_button = InlineKeyboardButton(text=LEXICON_INLINE_BUTTON_RU["back"], callback_data="back_snacks")
forward_shrimps_button = InlineKeyboardButton(text=LEXICON_INLINE_BUTTON_RU["forward"], callback_data="forward_shrimps")
back_shrimps_button = InlineKeyboardButton(text=LEXICON_INLINE_BUTTON_RU["back"], callback_data="back_shrimps")
forward_cold_drinks_button = InlineKeyboardButton(text=LEXICON_INLINE_BUTTON_RU["forward"], callback_data="forward_cold_drinks")
back_cold_drinks_button = InlineKeyboardButton(text=LEXICON_INLINE_BUTTON_RU["back"], callback_data="back_cold_drinks")
forward_hot_drinks_button = InlineKeyboardButton(text=LEXICON_INLINE_BUTTON_RU["forward"], callback_data="forward_hot_drinks")
back_hot_drinks_button = InlineKeyboardButton(text=LEXICON_INLINE_BUTTON_RU["back"], callback_data="back_hot_drinks")
forward_dessert_button = InlineKeyboardButton(text=LEXICON_INLINE_BUTTON_RU["forward"], callback_data="forward_dessert")
back_dessert_button = InlineKeyboardButton(text=LEXICON_INLINE_BUTTON_RU["back"], callback_data="back_dessert")
forward_sauces_button = InlineKeyboardButton(text=LEXICON_INLINE_BUTTON_RU["forward"], callback_data="forward_sauces")
back_sauces_button = InlineKeyboardButton(text=LEXICON_INLINE_BUTTON_RU["back"], callback_data="back_sauces")
forward_other_button = InlineKeyboardButton(text=LEXICON_INLINE_BUTTON_RU["forward"], callback_data="forward_other")
back_other_button = InlineKeyboardButton(text=LEXICON_INLINE_BUTTON_RU["back"], callback_data="back_other")

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

beef_burgers_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [back_beef_burgers_button, forward_beef_burgers_button]
    ]
)

chicken_and_fish_burgers_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [back_chicken_and_fish_burgers_button, forward_chicken_and_fish_burgers_button]
    ]
)

rolls_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [back_rolls_button, forward_rolls_button]
    ]
)

snacks_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [back_snacks_button, forward_snacks_button]
    ]
)

shrimps_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [back_shrimps_button, forward_shrimps_button]
    ]
)

cold_drinks_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [back_cold_drinks_button, forward_cold_drinks_button]
    ]
)

hot_drinks_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [back_hot_drinks_button, forward_hot_drinks_button]
    ]
)

dessert_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [back_dessert_button, forward_dessert_button]
    ]
)

sauces_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [back_sauces_button, forward_sauces_button]
    ]
)

other_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [back_other_button, forward_other_button]
    ]
)
