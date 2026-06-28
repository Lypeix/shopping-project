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
    'subscription': None,
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

subscriptions = {
    'vip': {'name': 'VIP', 'price': 500, 'currency': user_account['currency_display'], 'discount': 0.05},
    'mega_vip': {'name': 'MEGA VIP', 'price': 1000, 'currency': user_account['currency_display'], 'discount': 0.10},
    'ultra_vip': {'name': 'ULTRA VIP', 'price': 2000, 'currency': user_account['currency_display'], 'discount': 0.15}
}

cart = {
    'items': {},
    'item_count': 0,
    'total_price': 0
}

TAX_RATE = 0.23

state = {
    'user': user_account,
    'products': products,
    'subscriptions': subscriptions,
    'cart': cart,
    'tax': TAX_RATE
}


# CART FUNCTIONS

def display_catalog(state):
    """Displays catalog"""
    prompt_lines = ['Choose a product by typing in corresponding number: ']

    product_keys = list(state['products'].keys()) # ['cola', 'mango', 'manga', etc.]

    for idx, key in enumerate(product_keys, start=1):
        product = state['products'][key]
        
        prompt_lines.append(f"{idx}. {product['name']} - {product['price']} {product['currency']}"
                            f" - Stock: {product['stock']} units") 
        
    prompt_lines.append("> ")

    return "\n".join(prompt_lines), product_keys


def quantity_get(product_key, state):
    """Let's user choose the amount of product units he wants to get, eg. x8 cola"""
    product = state['products'][product_key]
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



def add_to_cart(state):
    """Lets user pick products"""
   

    prompt, product_keys = display_catalog(state)

    valid_choices = [str(i) for i in range(1, len(product_keys) + 1)]

    choice_num = user_choice(prompt, valid_choices)

    product_key = product_keys[int(choice_num) - 1] # converts choice string to integer and subtracts 1 so that guy's choice reflects index
    chosen_product = state['products'][product_key]
        
    qty = quantity_get(product_key, state)

    state['cart']['items'][product_key] = state['cart']['items'].get(product_key, 0) + qty
    state['cart']['item_count'] += qty
    state['cart']['total_price'] += chosen_product['price'] * qty
    chosen_product['stock'] -= qty
        
    print(f"You have selected {chosen_product['name']} for {chosen_product['price']} {chosen_product['currency']} ")

    cart_update(state)
        

def subscription_display(state):
    
    prompt_lines = ["Which subscription would you like to purchase? (LIFETIME!)"]

    subscription_keys = list(state['subscriptions'].keys())
    
    for idx, key in enumerate(subscription_keys, start=1):
        subscription = state['subscriptions'][key]

        prompt_lines.append(f"{idx}. Subscription: {subscription['name']} - Price: {subscription['price']} {subscription['currency']} - Benefits: {subscription['discount']} discount for all products")
    prompt_lines.append("> ")
    
    return "\n".join(prompt_lines), subscription_keys

def buy_subscription(state):

    answer = user_choice("Would you like to buy a subscription?"
                        "\n1. Yes" 
                        "\n2. No"
                        "\n> ",
                        ["1", "2"]
                        )
    
    if answer == '1':

        prompt, subscription_keys = subscription_display(state)

        valid_choices = [str(i) for i in range(1, len(subscription_keys) + 1)]

        choice_num = user_choice(prompt, valid_choices)

        subscription_key = subscription_keys[int(choice_num) - 1]
       
        selected_subscription = state['subscriptions'][subscription_key]


        if state['user']['balance'] < selected_subscription['price']:
            print(f"Insufficient funds!")
            return 

        else:
            state['user']['balance'] -= selected_subscription['price']
            state['user']['subscription'] = selected_subscription
            
            print(f"You are now a {selected_subscription['name']}!") 
            print(f"Your balance: {state['user']['balance']}")

    elif answer == "2":
        return

    return 



def calculate_tax(state):
    original_price = state['cart']['total_price']
    tax_amount = original_price * state['tax']

    return original_price, tax_amount

def calculate_discount(state):
    original_price = state['cart']['total_price']
    discount = state['user']['subscription']['discount'] 
    discount_amount = original_price * discount

    return discount_amount

def cart_update(state):

    original_price, tax_amount = calculate_tax(state)
    discount_amount = calculate_discount(state)

    total = original_price - discount_amount + tax_amount 
    state['cart']['total_price'] = total
 

    item_display = [f"x{qty} {state['products'][key]['name']}" for key, qty in state['cart']['items'].items()]
        
    print(f'\n-=-!CART STATUS!-=-')
    print(f"Items: {', '.join(item_display)}")
    print(f"Item count: {state['cart']['item_count']}") 

    print('Individual prices:')
    
    for key, qty in state['cart']['items'].items():
        product = state['products'][key]
        item_subtotal = qty * product['price']
        
        print(f"{product['name']} = {item_subtotal} {state['user']['currency_display']}\n============")

    print(f"Subtotal: {round(original_price, 2)} {state['user']['currency_display']}\n============")
    print(f"Discount: {round(discount_amount, 2)} {state['user']['currency_display']}\n============")
    print(f"Tax: {round(tax_amount, 2)} {state['user']['currency_display']}\n============")
    print(f"Total: {round(total, 2)} {state['user']['currency_display']}\n============")


def item_removal(state): 
    """Let's user remove items froms the cart"""

    if not state['cart']['items']:
        print('The cart is empty!')
        return

    cart_items = list(state['cart']['items'].items())
        
    prompt_lines = ['Which product would you like to remove?']
    
    for idx, (key, qty) in enumerate(cart_items, start=1):
        product = state['products'][key]
        prompt_lines.append(f"{idx}. x{qty} {product['name']} - {product['price']} {product['currency']}")
    prompt_lines.append("> ")
    prompt = "\n".join(prompt_lines)

    valid_choices = [str(i) for i in range(1, len(state['cart']['items']) + 1)]

    choice_num = user_choice(prompt, valid_choices)

    product_key, current_qty = cart_items[int(choice_num) - 1]
    product = state['products'][product_key]

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

    state['cart']['items'][product_key] -= remove_qty
    state['cart']['item_count'] -= remove_qty
    state['cart']['total_price'] -= product['price'] * remove_qty
    product['stock'] += remove_qty

    if state['cart']['items'][product_key] == 0:
        del state['cart']['items'][product_key]

    cart_update(state)

def action_loop(state):

    while True:
        answer = user_choice('What would you like to do?'
                            '\n1. Add items to the cart'
                            '\n2. Remove items from the cart'
                            '\n3. Purchase'
                            '\n4. Get a discount' 
                            '\n5. Exit'
                            '\n> ',
                        ['1', '2', '3', '4', '5']
                        )


        if answer == '1':
            add_to_cart(state)

        elif answer == '2':
            item_removal(state)
        
        elif answer == '3':
            total = state['cart']['total_price']
            if state['user']['balance'] < total:
                print("You do not have enough funds to make this purchase")
                return

            state['user']['balance'] -= total
            print('Your purchase has been finalized! Thank you for shopping')
            print(f"Your balance: {state['user']['balance']}")

        elif answer == '4':
            buy_subscription(state)

        elif answer == '5':
            print('Thank you for shopping!')            
            break


def main(state):
    action_loop(state)
    

if __name__ == "__main__":
    main(state)
