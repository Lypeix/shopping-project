#SHOPPING PROJECT

# INITIALIZATION PHASE

def user_choice(prompt, valid_choices):
    """Loops until user selects a valid choice"""
    while True:
        choice = input(prompt).strip().lower()
        if choice in valid_choices:
            return choice
        else:
            print(f"Invalid choice, please choose from: {', ' .join(valid_choices)} ")

def initialization():
    """Creates user's account data including username and currency"""


    user_name = input("Welcome! How would you like to name your account?\n> ")

    user_currency = user_choice(f"Hello {user_name}! Please pick your currency: "
                "\nPLN"
                "\nUSD"
                "\nEUR"
                "\nYEN"
                "\n> ",
                ["pln", "usd", "eur", "yen"]
                )

    user_account = {
    'name': user_name,
    'currency': user_currency,
    'currency_display': user_currency.upper(),
    'balance': 10000
    }


    return user_account

# DICTIONARIES

user_account = initialization()


products = {
    'cola': {'name': 'Cola', 'price': 4, 'currency': user_account['currency_display'], 'stock': 84}, 
    'mango': {'name': 'Mango', 'price': 8, 'currency': user_account['currency_display'], 'stock': 12},
    'manga': {'name': 'Manga', 'price': 70, 'currency': user_account['currency_display'], 'stock': 41},
    'meat':{'name': 'Meat', 'price': 40, 'currency': user_account['currency_display'], 'stock': 321},
    'suit':{'name': 'Suit', 'price': 500, 'currency': user_account['currency_display'], 'stock': 3}
    }

cart = {
    'items': {},
    'item_count': 0,
    'total_price': 0
}


# CART FUNCTIONS

def display_cart():
    """Displays catalog"""
    prompt_lines = ['Choose a product by typing in corresponding number: ']

    product_keys = list(products.keys()) # ['cola', 'mango', 'manga', etc.]

    for idx, key in enumerate(product_keys, start=1):
        product = products[key]
        
        prompt_lines.append(f"{idx}. {product['name']} - {product['price']} {product['currency']}"
                            f" - Stock: {product['stock']} units") 
        
    prompt_lines.append("> ")

    return '\n'.join(prompt_lines), product_keys

def quantity_get(product_key):
    """Let's user choose the amount of product units he wants to get, eg. x8 cola"""
    product = products[product_key]
    max_qty = product['stock']

    while True:
        try:
            qty = int(input(f"How many units would you like to purchase?\nIn Stock: {max_qty}\n> "))
                        
            if qty < 1:
                print("You must select at least one unit!")

            elif qty > max_qty:
                print(f"There are only {max_qty} units in stock!") 
            
            else:
                return qty

        except ValueError: 
            print("Invalid number! Please enter a valid value.")



def add_to_cart():
    """Lets user pick products"""

    while True:    

        prompt, product_keys = display_cart()

        valid_choices = [str(i) for i in range(1, len(product_keys) + 1)]

        choice_num = user_choice(prompt, valid_choices)

        product_key = product_keys[int(choice_num) - 1] # converts choice string to integer and subtracts 1 so that guy's choice reflects index
        chosen_product = products[product_key]
        
        qty = quantity_get(product_key)

        cart['items'][product_key] = cart['items'].get(product_key, 0) + qty
        cart['item_count'] += qty
        cart['total_price'] += chosen_product['price'] * qty
        chosen_product['stock'] -= qty


        # Stock update

        item_display = [f"x{qty} {products[key]['name']}" for key, qty in cart['items'].items()]
        print(f"You have selected {chosen_product['name']} for {chosen_product['price']} {chosen_product['currency']} ")
        print(f'-=-!CART STATUS!-=-')
        print(f"Items: {', '.join(item_display)}")
        print(f"Item count: {cart['item_count']}") 
        print(f"Total price: {cart['total_price']} {user_account['currency_display']}")


        answer = user_choice('What would you like to do now?'
                            '\n1. Add another item to the cart'
                            '\n2. Remove items from the cart'
                            '\n3. Purchase options'
                            '\n4. Exit'
                            '\n> ',
                        ['1', '2', '3', '4']
                        )


        if answer == '1':
            continue
        
        elif answer == '2':
            item_removal()
        
        elif answer == '3':
            user_account['balance'] -= cart['total_price']
            print('Your purchase has been finalized! Thank you for shopping')

        else:
            print('Thank you for shopping!')            

            return True

        
def item_removal():
    """Let's user remove items froms the cart"""


def main():

    display_cart()
    add_to_cart()

if __name__ == "__main__":
    main()
