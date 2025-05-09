from arts import *
def good_ending():
    alive_art()
    print('Você encontrou o tesouro!')
    return True

def bad_ending():
    death_art()
    print('Você morreu... Tente novamente!')
    return False