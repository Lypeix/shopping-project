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
            print(f"Your balance: {state['user']['balance']} {state['user']['currency_display']}")

    elif answer == "2":
        return

    return 
