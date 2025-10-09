from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from game_share_bot.core.callbacks import MenuCallback


def get_game_detail_kb(game_id: int, is_available: bool = True) -> InlineKeyboardMarkup:
    """Клавиатура для страницы конкретной игры"""
    buttons = []

    if is_available:
        buttons.append([
            InlineKeyboardButton(
                text="🎮 Взять игру",
                callback_data=f"take_game_{game_id}"
            )
        ])

    return InlineKeyboardMarkup(inline_keyboard=buttons)