def make_pizza(size, *toppings):
    print(f"make a {size}-size pizza with toppings:")
    for topping in toppings:
        print(f"-{topping}")