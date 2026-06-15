#SHOPPING PROJECT



print(f"Products available:") 
product_names = ['Cola', 'Mango', 'Manga', 'Meat', 'Suit']
for idx, product in enumerate(product_names, start=1):
    print(f"{idx}. {product}")




def user_choice(prompt, valid_choices):

    while True:
        choice = input(prompt).strip().lower()
        if choice in valid_choices:
            return choice
        else:
            print(f"Invalid choice, please choose from: {', ' .join(valid_choices)} ")

product_choice = user_choice("Choose a product by typing in desired number!"
                "\n1. Cola"
                "\n2. Manga"
                "\n3. Suit"
                "\n> ",
                ["1", "2", "3"]
                )

product_map = {
    "1": "Cola",
    "2": "Manga",
    "3": "Suit"
    }

product = product_map[product_choice]

print(f"Your cart currently consists of: {product}")

