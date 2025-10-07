from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from core.callbacks import CatalogCallback
from core.callbacks.game import GameCallback
from core.callbacks.user import UserCallback
from game_share_bot.core.callbacks import MenuCallback
from infrastructure.models import Game


def main_menu_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🎮 Каталог", callback_data=CatalogCallback().pack())],
            [InlineKeyboardButton(text="📦 Подписки", callback_data=MenuCallback(section="subs").pack())],
            [InlineKeyboardButton(text="👤 Регистрация", callback_data=UserCallback(action="register").pack())],
            [InlineKeyboardButton(text="🆘 Поддержка", callback_data="help")],
        ]
    )


def catalog_kb(games: list[Game]) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    for idx, game in enumerate(games, start=1):
        builder.button(
            text=f"{idx}",
            callback_data=GameCallback(
                action="open",
                game_id=game.id,
            ).pack()
        )

    builder.adjust(5)
    builder.row(
        InlineKeyboardButton(text="⬅️ Меню", callback_data=MenuCallback(section="main").pack())
    )

    return builder.as_markup()
