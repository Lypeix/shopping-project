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

def display_catalog():
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

        prompt, product_keys = display_catalog()

        valid_choices = [str(i) for i in range(1, len(product_keys) + 1)]

        choice_num = user_choice(prompt, valid_choices)

        product_key = product_keys[int(choice_num) - 1] # converts choice string to integer and subtracts 1 so that guy's choice reflects index
        chosen_product = products[product_key]
        
        qty = quantity_get(product_key)

        cart['items'][product_key] = cart['items'].get(product_key, 0) + qty
        cart['item_count'] += qty
        cart['total_price'] += chosen_product['price'] * qty
        chosen_product['stock'] -= qty
        
        print(f"You have selected {chosen_product['name']} for {chosen_product['price']} {chosen_product['currency']} ")

        cart_update()
        action_loop()
        

def cart_update():

    item_display = [f"x{qty} {products[key]['name']}" for key, qty in cart['items'].items()]
        
    print(f'\n-=-!CART STATUS!-=-')
    print(f"Items: {', '.join(item_display)}")
    print(f"Item count: {cart['item_count']}") 

    print('Individual prices:')
    subtotal_sum = 0
    for key, qty in cart['items'].items():
        product = products[key]
        subtotal = qty * product['price']
        subtotal_sum += subtotal
        print(f'{product['name']} = {subtotal} {user_account['currency_display']}')
     
    print(f"Total price: {cart['total_price']} {user_account['currency_display']}")


def action_loop():

    while True:
        answer = user_choice('What would you like to do now?'
                            '\n1. Add another item to the cart'
                            '\n2. Remove items from the cart'
                            '\n3. Purchase options'
                            '\n4. Exit'
                            '\n> ',
                        ['1', '2', '3', '4']
                        )


        if answer == '1':
            add_to_cart()
            return

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

    if not cart['items']:
        print('The cart is empty!')
        return

    cart_items = list(cart['items'].items())
        
    prompt_lines = ['Which product would you like to remove?']
    
    for idx, (key, qty) in enumerate(cart_items, start=1):
        product = products[key]
        prompt_lines.append(f"{idx}. x{qty} {product['name']} - {product['price']} {product['currency']}")
    prompt_lines.append("> ")
    prompt = "\n".join(prompt_lines)

    valid_choices = [str(i) for i in range(1, len(cart['items']) + 1)]

    choice_num = user_choice(prompt, valid_choices)

    product_key, current_qty = cart_items[int(choice_num) - 1]
    product = products[product_key]

    while True:
        try:
            remove_qty = int(input(f"How many {product['name']} units would you like to remove?\nUnits in cart: {current_qty} \n> "))
            
            if remove_qty < 1:
                print('You must select at least one unit!')
            elif remove_qty > current_qty:
                print('The provided number exceeds amount of units in the cart.')
            else:
                print(f'Successfuly removed {remove_qty} units from the cart!')
                break

        except ValueError:
            print(f'Please enter a valid number')

    cart['items'][product_key] = current_qty - remove_qty
    cart['item_count'] -= remove_qty
    cart['total_price'] -= product['price'] * remove_qty

    if cart['items'][product_key] == 0:
        del cart['items'][product_key]

    cart_update()

def main():
    add_to_cart()

if __name__ == "__main__":
    main()
