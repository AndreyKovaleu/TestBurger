from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from lexicon.lexicon_ru import LEXICON_BUTTON_RU

menu_button = KeyboardButton(text=LEXICON_BUTTON_RU["menu"])
cart_button = KeyboardButton(text=LEXICON_BUTTON_RU["cart"])
history_button = KeyboardButton(text=LEXICON_BUTTON_RU["history"])
news_button = KeyboardButton(text=LEXICON_BUTTON_RU["news"])
settings_button = KeyboardButton(text=LEXICON_BUTTON_RU["settings"])
help_button = KeyboardButton(text=LEXICON_BUTTON_RU["help"])
home_button = KeyboardButton(text=LEXICON_BUTTON_RU["home"])
again_button = KeyboardButton(text=LEXICON_BUTTON_RU["again"])
name_button = KeyboardButton(text=LEXICON_BUTTON_RU["name"])
phone_button = KeyboardButton(text=LEXICON_BUTTON_RU["phone"])
address_button = KeyboardButton(text=LEXICON_BUTTON_RU["address"])
city_button = KeyboardButton(text=LEXICON_BUTTON_RU["city"])
notification_button = KeyboardButton(text=LEXICON_BUTTON_RU["notification"])
back_button = KeyboardButton(text=LEXICON_BUTTON_RU["back"])
message_button = KeyboardButton(text=LEXICON_BUTTON_RU["message"])
reference_button = KeyboardButton(text=LEXICON_BUTTON_RU["reference"])

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [menu_button, cart_button],
        [history_button, news_button],
        [settings_button, help_button]
    ],
    resize_keyboard=True,
    is_persistent=False,
    one_time_keyboard=False,
    input_field_placeholder="Выберите кнопку ↓",
    selective=True
)

news_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [home_button, again_button]
    ],
    resize_keyboard=True,
    is_persistent=False,
    one_time_keyboard=False,
    input_field_placeholder="Выберите кнопку ↓",
    selective=True
)

settings_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [name_button, phone_button],
        [address_button, city_button],
        [notification_button],
        [back_button]
    ],
    resize_keyboard=True,
    is_persistent=False,
    one_time_keyboard=False,
    input_field_placeholder="Выберите кнопку ↓",
    selective=True
)

help_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [message_button, reference_button],
        [home_button]
    ],
    resize_keyboard=True,
    is_persistent=False,
    one_time_keyboard=False,
    input_field_placeholder="Выберите кнопку ↓",
    selective=True
)
