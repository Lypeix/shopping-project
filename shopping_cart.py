#SHOPPING PROJECT

# DICTIONARIES

products = {
    'cola': {'name': 'Cola', 'price': 4, 'currency': 'PLN'}, 
    'mango': {'name': 'Mango', 'price': 8, 'currency': 'PLN'},
    'manga': {'name': 'Manga', 'price': 70, 'currency': 'PLN'},
    'meat':{'name': 'Meat', 'price': 40, 'currency': 'PLN'},
    'suit':{'name': 'Suit', 'price': 500, 'currency': 'PLN'}
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

    prompt_lines = ['Choose product by typing corresponding number']

    product_keys = list(products.keys())

    for idx, key in enumerate(product_keys, start=1):
        product = products[key]
        prompt_lines.append(f"{idx}. {product['name']} - {product['price']} {product['currency']}") 
    
    prompt_lines.append(f"> ")
    prompt =  "\n".join(prompt_lines)

    valid_choices = [str(i) for i in range(1, len(product_keys) + 1)]

    choice_num = user_choice(prompt, valid_choices)

    product_key = product_keys[int(choice_num) - 1]
    chosen_product = product[product_key]

    print(f'You have selected {chosen_product['name']}!')

if __name__ == "__main__":
    main()
