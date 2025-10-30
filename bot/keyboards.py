import json

PIZZA_NAME_KEYBOARD = json.dumps(
    {
        "inline_keyboard": [
            [
                {"text": "Margherita", "callback_data": "pizza_margherita"},
                {"text": "Pepperoni", "callback_data": "pizza_pepperoni"},
            ],
            [
                {"text": "Quattro Stagioni", "callback_data": "pizza_quattro_stagioni"},
                {"text": "Capricciosa", "callback_data": "pizza_capricciosa"},
            ],
            [
                {"text": "Diavola", "callback_data": "pizza_diavola"},
                {"text": "Prosciutto", "callback_data": "pizza_prosciutto"},
            ],
        ],
    },
)

PIZZA_SIZE_KEYBOARD = json.dumps(
    {
        "inline_keyboard": [
            [
                {"text": "Small (25cm)", "callback_data": "size_small"},
                {"text": "Medium (30cm)", "callback_data": "size_medium"},
            ],
            [
                {"text": "Large (35cm)", "callback_data": "size_large"},
                {"text": "Extra Large (40cm)", "callback_data": "size_xl"},
            ],
        ],
    },
)

PIZZA_DRINKS_KEYBOARD = json.dumps(
    {
        "inline_keyboard": [
            [
                {"text": "Coca-Cola", "callback_data": "drink_coca_cola"},
                {"text": "Pepsi", "callback_data": "drink_pepsi"},
            ],
            [
                {"text": "Orange Juice", "callback_data": "drink_orange_juice"},
                {"text": "Apple Juice", "callback_data": "drink_apple_juice"},
            ],
            [
                {"text": "Water", "callback_data": "drink_water"},
                {"text": "Iced Tea", "callback_data": "drink_iced_tea"},
            ],
            [
                {"text": "No drinks", "callback_data": "drink_none"},
            ],
        ],
    },
)

ORDER_KEYBOARD = json.dumps(
    {
        "inline_keyboard": [
            [
                {"text": "Confirm", "callback_data": "order_ok"},
            ],
            [
                {"text": "Start again", "callback_data": "order_restart"},
            ],
        ],
    },
)

PIZZA_NAME_MAPPING = {
    "pizza_margherita": "Margherita",
    "pizza_pepperoni": "Pepperoni", 
    "pizza_quattro_stagioni": "Quattro Stagioni",
    "pizza_capricciosa": "Capricciosa",
    "pizza_diavola": "Diavola",
    "pizza_prosciutto": "Prosciutto",
}

PIZZA_SIZE_MAPPING = {
    "size_small": "Small (25cm)",
    "size_medium": "Medium (30cm)", 
    "size_large": "Large (35cm)",
    "size_xl": "Extra Large (40cm)",
}

PIZZA_DRINK_MAPPING = {
    "drink_coca_cola": "Coca-Cola",
    "drink_pepsi": "Pepsi",
    "drink_orange_juice": "Orange Juice",
    "drink_apple_juice": "Apple Juice",
    "drink_water": "Water",
    "drink_iced_tea": "Iced Tea",
    "drink_none": "No drinks",
}
