import json

import bot.database_client
from bot.keyboards import PIZZA_NAME_KEYBOARD
import bot.telegram_client
from bot.handlers.handler import Handler, HandlerStatus


class MessageStart(Handler):
    def can_handle(self, update: dict, state: str, order_json: dict) -> bool:
        return (
            "message" in update
            and "text" in update["message"]
            and update["message"]["text"] == "/start"
        )
    
    def handle(self, update: dict, state: str, data: dict) -> HandlerStatus:
        telegram_id = update["message"]["from"]["id"]

        bot.database_client.clear_user_state_and_order(telegram_id)
        bot.database_client.update_user_state(telegram_id, "WAIT_FOR_PIZZA_NAME")

        bot.telegram_client.sendMessage(
            chat_id=update["message"]["chat"]["id"],
            text="Welcom to Pizza shop!",
            reply_markup=json.dumps({"remove_keyboard": True}),
        )

        bot.telegram_client.sendMessage(
            chat_id=update["message"]["chat"]["id"],
            text="Please choose pizza name",
            reply_markup=PIZZA_NAME_KEYBOARD,
        )
        return HandlerStatus.STOP
