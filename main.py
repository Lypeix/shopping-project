from state import create_state
from utils import user_choice
from cart import add_to_cart, item_removal, checkout
from subscriptions import buy_subscription


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
            checkout(state)
            

        elif answer == '4':
            buy_subscription(state)

        elif answer == '5':
            print('Thank you for shopping!')            
            break

def main():
    state = create_state()
    action_loop(state)
    

if __name__ == "__main__":
    main()
