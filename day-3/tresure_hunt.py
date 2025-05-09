from arts import *
from endings import *

def main():
    treasure_art()
    print('Bem-vindo a caça ao tesouro!')

    from paths import places_generator
    paths = places_generator()
    while not bad_ending():
        # TODO: Implementar a lógica do jogo
        pass



if __name__ == '__main__':
   main()
