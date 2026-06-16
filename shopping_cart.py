#SHOPPING PROJECT

# DICTIONARIES

products = {
    'cola': {'name': 'Cola', 'price': 4, 'currency': 'PLN', 'stock': 84}, 
    'mango': {'name': 'Mango', 'price': 8, 'currency': 'PLN', 'stock': 12},
    'manga': {'name': 'Manga', 'price': 70, 'currency': 'PLN', 'stock': 41},
    'meat':{'name': 'Meat', 'price': 40, 'currency': 'PLN', 'stock': 321},
    'suit':{'name': 'Suit', 'price': 500, 'currency': 'PLN', 'stock': 3}
    }


# FUNCTIONS

def user_choice(prompt, valid_choices):

    while True:
        choice = input(prompt).strip().lower()
        if choice in valid_choices:
            return choice
        else:
            print(f"Invalid choice, please choose from: {', ' .join(valid_choices)} ")


def main():
    while True:
        prompt_lines = ['Choose product by typing corresponding number']

        product_keys = list(products.keys()) # ['cola', 'mango', 'manga', etc.]

        for idx, key in enumerate(product_keys, start=1):
            product = products[key]
            prompt_lines.append(f"{idx}. {product['name']} - {product['price']} {product['currency']} - Stock: {product['stock']} units ") 
        
        prompt_lines.append("> ")
        prompt =  "\n".join(prompt_lines)

        valid_choices = [str(i) for i in range(1, len(product_keys) + 1)]

        choice_num = user_choice(prompt, valid_choices)

        product_key = product_keys[int(choice_num) - 1] # converts choice string to integer and subtracts 1 so that guy's choice reflects index
        chosen_product = products[product_key]

        answer = user_choice(f'You have selected {chosen_product['name']} for {chosen_product['price']} {chosen_product['currency']} \nWould you like to choose another item? (Yes/No) \n> ',
                    ['yes', 'no']
                    )
        if answer == 'yes':
            continue
        else:
            return True

if __name__ == "__main__":
    main()
