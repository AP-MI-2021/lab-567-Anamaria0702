from copy import deepcopy
from Domain.obiect import set_locatie, get_pret_achizitie, set_descriere, get_descriere


def mutare_obiecte(obiecte, locatie_new):
    '''
    Muta toate obiectele dintr-o locatie in alta
    :param obiecte: lista de obiecte
    :param locatie_new: string
    :return:
    '''
    if len(locatie_new) != 4:
        raise ValueError('Locatia trebuie sa contina exact 4 caractere')
    result_list = deepcopy(obiecte)
    for obiect in result_list:
        set_locatie(obiect, locatie_new)
    return result_list

def concatenare_string(obiecte, sir, n):
    '''
    Concateneaza un string citit la toate descrierile obiectelor cu prețul mai mare decât o valoare citită.
    :param obiecte: lista de obiecte
    :param sir: string
    :param n: float
    :return:
    '''
    result_list = deepcopy(obiecte)
    for obiect in result_list:
        if n < get_pret_achizitie(obiect):
            set_descriere(obiect, get_descriere(obiect) + sir)
    return result_list

def pret_max_locatie(obiecte):
    '''
    Determina cel mai mare pret pentru fiecare locatie
    :param obiecte: lista de obiecte
    :return: cel mai mare pret pentru fiecare locatie
    '''
    pass

