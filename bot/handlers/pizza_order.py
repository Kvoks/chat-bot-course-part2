import bot.telegram_client
import bot.database_client
from bot.handlers.handler import Handler, HandlerStatus

class PizzaOrderHandler(Handler):
    def can_handle(self, update: dict, state: str, order_json: dict) -> bool:
        if "callback_query" not in update:
            return False
        
        if state != "WAIT_FOR_ORDER_APPROVE":
            return False
        
        callback_data = update["callback_query"]["data"]
        return callback_data.startswith("order_")
    
    def handle(self, update: dict, state: str, order_json: dict) -> HandlerStatus:
        telegram_id = update["callback_query"]["from"]["id"]
        callback_data = update["callback_query"]["data"]

        bot.database_client.update_user_state(telegram_id, "ORDER_FINISHED")

        bot.telegram_client.answerCallbackQuery(update["callback_query"]["id"])

        """depending on the response, it was possible to accept different states for further processing
        then this handler returns CONTINUE, and add handlers to those different states
        which will be after him in the __init__"""
        if callback_data == "order_ok":
            order_summary = (
                "Order accepted!\n"
                f"- Pizza: {order_json.get('pizza_name', 'Not selected')}\n"
                f"- Size: {order_json.get('pizza_size', 'Not selected')}\n"
                f"- Drink: {order_json.get('drink', 'Not selected')}\n\n"
                "To re-order, press /start"
            )
        else:
            order_summary = (
                "The order was not accepted!\n\n"
                "To re-order, press /start"
            )

        bot.telegram_client.deleteMessage(
            chat_id=update["callback_query"]["message"]["chat"]["id"],
            message_id=update["callback_query"]["message"]["message_id"],
        )
        bot.telegram_client.sendMessage(
            chat_id=update["callback_query"]["message"]["chat"]["id"],
            text=order_summary,
        )
        return HandlerStatus.STOP