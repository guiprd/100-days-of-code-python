from validations import *

def main():
    # Initialize pizza size variable
    pizza_size = ''

    # Loop until a valid size is entered
    while not is_valid_pizza_size(pizza_size):
        pizza_size = input("Por favor, escolha uma opção de tamanho: P, M ou G?\n").upper()

        if not is_valid_pizza_size(pizza_size):
            print("Tamanho inválido. Por favor, escolha P, M ou G.")

    # Calculate the price of the pizza
    price = pizza_price(pizza_size)

    concat_add_ons = ''
    for n, k in enumerate(ADD_ONS.keys()):
        concat_add_ons += f'{n+1}. ' + k + '\n'

    add_on = ''
    while True:
        add_on = input(f'Gostaria de colocar algum adicional? {concat_add_ons}\nAperte enter se não quiser adicionar nada ou digite "sair" para sair.\n')
        if add_on == 'sair' or add_on == '':
            break
        # TODO: TRATAR AQUI O ERRO DE DIGITAR UM NÚMERO QUE NÃO EXISTE NA LISTA
        break
    if add_on == 'sair' or add_on == '':
        print(f"O preço da pizza de tamanho {pizza_size} é R$ {price:.2f}")
        exit(0)

    add_on_name = list(ADD_ONS.keys())[int(add_on) - 1]
    print(f"O preço da pizza de tamanho {pizza_size} com adicional de {add_on_name} é R$ {price+ADD_ONS[add_on_name]:.2f}")


if __name__ == '__main__':
    main()