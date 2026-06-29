import json
from pathlib import Path
from utils import user_choice

TAX_RATE = 0.23
BASE_DIR = Path(__file__).parent

def load_json(filename):
    path = BASE_DIR / filename

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)

def initialization():
    user_name = input("Welcome! How would you like to name your account?\n> ")

    user_currency = user_choice(
        f"Hello {user_name}! Please pick your currency:"
        "\nPLN"
        "\nUSD"
        "\nEUR"
        "\nYEN"
        "\n> ",
        ["pln", "usd", "eur", "yen"]
    )

    return {
        "name": user_name,
        "currency": user_currency,
        "currency_display": user_currency.upper(),
        "subscription": None,
        "balance": 10000
    }

def create_cart():
    return {
        "items": {},
        "item_count": 0,
        "total_price": 0
    }

def create_state():
    user_account = initialization()
    products = load_json("products.json")
    subscriptions = load_json("subscriptions.json")
    cart = create_cart()

    return {
        "user": user_account,
        "products": products,
        "subscriptions": subscriptions,
        "cart": cart,
        "tax": TAX_RATE
    }
