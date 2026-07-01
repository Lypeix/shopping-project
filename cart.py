from state import create_state
from utils import user_choice


def display_catalog(state):
    """Displays catalog"""
    prompt_lines = ['Choose a product by typing in corresponding number: ']

    product_keys = list(state['products'].keys())

    for idx, key in enumerate(product_keys, start=1):
        product = state['products'][key] 
        
        prompt_lines.append(f"{idx}. {product['name']} - {product['price']} {state["user"]["currency_display"]}"
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
        
    print(f"You have selected {chosen_product['name']} for {chosen_product['price']} {state["user"]["currency_display"]} ")

    cart_update(state)

def calculate_tax(state):
    original_price = state['cart']['total_price']
    tax_amount = original_price * state['tax']

    return original_price, tax_amount

def calculate_discount(state):
    if state['user']['subscription'] is None:
        return 0

    original_price = state['cart']['total_price']
    discount = state['user']['subscription']['discount'] 
    

    return original_price * discount

def cart_update(state):

    original_price, tax_amount = calculate_tax(state)
    discount_amount = calculate_discount(state)

    total = original_price - discount_amount + tax_amount 

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
        prompt_lines.append(f"{idx}. x{qty} {product['name']} - {product['price']} {state["user"]["currency_display"]}")
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

def checkout(state):
        total = state['cart']['total_price']
        if state['cart']['item_count'] == 0:
            print("You have no products in your inventory!")
            return
        
        elif state['user']['balance'] < total:
            print("You do not have enough funds to make this purchase")
            return

        state['user']['balance'] -= total
        print('Your purchase has been finalized! Thank you for shopping')
        print(f"Your balance: {state['user']['balance']} {state['user']['currency_display']}")    


