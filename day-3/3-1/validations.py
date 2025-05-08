ADD_ONS = {
    'Bacon': 5.00,
    'Calabresa': 2.00,
    'Frango': 2.00,
    'Milho': 1.00,
    'Palmito': 2.50,
    'Queijo': 1.50,
    'Tomate': 1.00,
}


def is_valid_pizza_size(pizza_size=''):
    """
    Validate the pizza size input.
    :param pizza_size: The size of the pizza (P, M, G).
    :return: True if valid, False otherwise.
    """
    valid_sizes = ['P', 'M', 'G']
    return pizza_size in valid_sizes

def pizza_price(pizza_size=''):
    """
    Calculate the price of the pizza based on its size.
    :param pizza_size: The size of the pizza (P, M, G).
    :return: The price of the pizza.
    """
    prices = {
        'P': 20.00,
        'M': 30.00,
        'G': 40.00
    }
    return prices.get(pizza_size, 0)  # Default to 0 if size is invalid

def add_on_price(add_on):
    if add_on in ADD_ONS:
        return ADD_ONS[add_on]
    else:
        print('Nenhum adicional foi selecionado')
        return 0