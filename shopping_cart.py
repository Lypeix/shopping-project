#SHOPPING PROJECT

# INITIALIZATION

def user_choice(prompt, valid_choices):
    """Loops until user selects a valid choice"""
    while True:
        choice = input(prompt).strip().lower()
        if choice in valid_choices:
            return choice
        else:
            print(f"Invalid choice, please choose from: {', ' .join(valid_choices)} ")

def initialization():
    
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
    'currency_display': user_currency.upper()
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
    'items': [],
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

def add_to_cart():
    """Lets user pick products"""

    while True:    

        prompt, product_keys = display_cart()

        valid_choices = [str(i) for i in range(1, len(product_keys) + 1)]

        choice_num = user_choice(prompt, valid_choices)

        product_key = product_keys[int(choice_num) - 1] # converts choice string to integer and subtracts 1 so that guy's choice reflects index
        chosen_product = products[product_key]
        

        cart['items'].append(product_key)
        cart['item_count'] += 1
        cart['total_price'] += chosen_product['price']


        item_names = [products[key]['name'] for key in cart['items']]
        print(f"You have selected {chosen_product['name']} for {chosen_product['price']} {chosen_product['currency']} ")
        print(f'-=-!CART STATUS!-=-')
        print(f"Items: {', '.join(item_names)}")
        print(f"Item count: {cart['item_count']}") 
        print(f"Total price: {cart['total_price']} {user_account['currency_display']}")


        answer = user_choice('Would you like to choose another item? (Yes/No) \n> ',
                        ['yes', 'no']
                        )


        if answer == 'yes':
            continue
        else:
            print('Thank you for shopping!')            

            return True

        
def main():

    display_cart()
    add_to_cart()

if __name__ == "__main__":
    main()
