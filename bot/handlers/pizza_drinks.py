from bot.keyboards import PIZZA_DRINK_MAPPING, ORDER_KEYBOARD
import bot.telegram_client
import bot.database_client
from bot.handlers.handler import Handler, HandlerStatus

class PizzaDrinksHandler(Handler):
    def can_handle(self, update: dict, state: str, order_json: dict) -> bool:
        if "callback_query" not in update:
            return False
        
        if state != "WAIT_FOR_DRINKS":
            return False
        
        callback_data = update["callback_query"]["data"]
        return callback_data.startswith("drink_")
    
    def handle(self, update: dict, state: str, order_json: dict) -> HandlerStatus:
        telegram_id = update["callback_query"]["from"]["id"]
        callback_data = update["callback_query"]["data"]

        drink = PIZZA_DRINK_MAPPING.get(callback_data)
        order_json["drink"] = drink
        bot.database_client.update_user_order_json(telegram_id, order_json)
        bot.database_client.update_user_state(telegram_id, "WAIT_FOR_ORDER_APPROVE")

        bot.telegram_client.answerCallbackQuery(update["callback_query"]["id"])

        order_summary = (
            "Your order:\n"
            f"- Pizza: {order_json.get('pizza_name', 'Not selected')}\n"
            f"- Size: {order_json.get('pizza_size', 'Not selected')}\n"
            f"- Drink: {order_json.get('drink', 'Not selected')}\n\n"
            "Сonfirm the order?"
        )

        bot.telegram_client.deleteMessage(
            chat_id=update["callback_query"]["message"]["chat"]["id"],
            message_id=update["callback_query"]["message"]["message_id"],
        )
        bot.telegram_client.sendMessage(
            chat_id=update["callback_query"]["message"]["chat"]["id"],
            text=order_summary,
            reply_markup=ORDER_KEYBOARD,
        )
        return HandlerStatus.STOP