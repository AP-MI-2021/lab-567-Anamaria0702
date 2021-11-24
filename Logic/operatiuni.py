from copy import deepcopy
from Domain.obiect import set_locatie, get_pret_achizitie, set_descriere, get_descriere, get_locatie
from Domain.inventar import get_lista_curenta, get_lista_undo, set_lista_curenta, adaugare_lista_undo_and_clear_redo, get_lista_redo, adaugare_lista_undo, adaugare_lista_redo


def mutare_obiecte(inventar, locatie_new):
    '''
    Muta toate obiectele dintr-o locatie in alta
    :param obiecte: lista de obiecte
    :param locatie_new: string
    :return:
    '''
    adaugare_lista_undo_and_clear_redo(inventar)
    if len(locatie_new) != 4:
        raise ValueError('Locatia trebuie sa contina exact 4 caractere')
    obiecte = get_lista_curenta(inventar)
    for obiect in obiecte:
        set_locatie(obiect, locatie_new)

def concatenare_string(inventar, sir, n):
    '''
    Concateneaza un string citit la toate descrierile obiectelor cu prețul mai mare decât o valoare citită.
    :param obiecte: lista de obiecte
    :param sir: string
    :param n: float
    :return:
    '''
    adaugare_lista_undo_and_clear_redo(inventar)
    obiecte = get_lista_curenta(inventar)
    for obiect in obiecte:
        if n < get_pret_achizitie(obiect):
            set_descriere(obiect, get_descriere(obiect) + sir)

def location_list(obiecte):
    '''
    Formeaza o lista ce contine doar locatiile diferite ale obiectelor dintr-o lista
    :param obiecte: lista de obiecte
    :return:
    '''
    result = []
    for obiect in obiecte:
        if get_locatie(obiect) not in result:
            result.append(get_locatie(obiect))
    return result

def pret_max_locatie(obiecte):
    '''
    Creeaza o lista formata din preturile maxime ale locatiilor din lista
    :param obiecte: lista de obiecte
    :return: cel mai mare pret pentru fiecare locatie
    '''
    lista_pret_max = []
    locatii = location_list(obiecte)
    for locatie in locatii:
        pret_max = -1
        for obiect in obiecte:
            if get_locatie(obiect) == locatie:
                if pret_max < get_pret_achizitie(obiect):
                    pret_max = get_pret_achizitie(obiect)
        lista_pret_max.append(pret_max)
    return lista_pret_max


def sort_obiecte(obiecte):
    '''
    Ordoneaza crescator obiectele dupa pretul de achizitie
    :param obiecte: lista de obiecte
    :return:
    '''
    return sorted(obiecte, key = lambda obiect: get_pret_achizitie(obiect))

def compute_sum_prices_per_location(obiecte):
    '''
    Afiseaza sumele preturilor pentru fiecare locatie
    :param obiecte: lista de obiecte
    :return:
    '''
    result = {}
    for obiect in obiecte:
        location = get_locatie(obiect)
        price = get_pret_achizitie(obiect)
        if location in result:
            result[location] += price
        else:
            result[location] = price
    return result

def apply_undo(inventar):
    '''

    :param inventar:
    :return:
    '''
    lista_undo = get_lista_undo(inventar)
    if len(lista_undo) > 1:
        adaugare_lista_redo(inventar)
        prior_lista_curenta = lista_undo.pop()
        set_lista_curenta(inventar, prior_lista_curenta)
    else:
        set_lista_curenta(inventar, [])


def apply_redo(inventar):
    '''

    :param inventar:
    :return:
    '''
    lista_redo = get_lista_redo(inventar)
    if len(lista_redo) > 0:
        adaugare_lista_undo(inventar)
        new_current_list = lista_redo.pop()
        set_lista_curenta(inventar, new_current_list)



