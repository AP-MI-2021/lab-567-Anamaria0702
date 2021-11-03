from copy import deepcopy
from Domain.obiect import *
from Logic.validator import validate_obiect

def add_obiect(obiecte, id, nume, descriere, pret_achizitie, locatie):
    '''

    Adaugam in memorie, in lista de obiecte un obiect format
    din fieldurile: id, nume, descriere, pret_achizitie, locatie
    :param obiecte: lista de obiecte
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret_achizitie: string
    :param locatie: string
    :return:
    '''
    id, nume, descriere, pret_achizitie, locatie = validate_obiect(id, nume, descriere, pret_achizitie, locatie)
    obiect = create_obiect(id,nume, descriere, pret_achizitie, locatie)
    return obiecte + [obiect]

def find_obiect(obiecte, id):
    '''
    Find obiect in obiecte with id
    If not found, we return None
    :param obiecte:
    :param id:
    :return:
    '''
    for obiect in obiecte:
        if get_id(obiect) == id:
            return obiect
    return None

def edit_obiect(obiecte, id, nume_new, descriere_new, pret_achizitie_new, locatie_new):
    '''
    Editarea unui obiect cu idul id si aruncarea unei erori ValueError in cazurile in care fieldurile nu sunt
    corecte
    :param obiecte:
    :param id:
    :param nume_new:
    :param descriere_new:
    :param pret_achizitie_new:
    :param locatie_new:
    :return:
    '''
    id, nume_new, descriere_new, pret_achizitie_new, locatie_new = validate_obiect(id, nume_new, descriere_new, pret_achizitie_new, locatie_new)
    updated_list = deepcopy(obiecte)
    for obiect in updated_list:
        if get_id(obiect) == id:
            set_nume(obiect, nume_new)
            set_descriere(obiect,descriere_new)
            set_pret_achizitie(obiect, pret_achizitie_new)
            set_locatie(obiect, locatie_new)

    return updated_list

def delete_obiect(obiecte, id):
    '''
    Scoatem din lista un obiect cu idul id
    :param obiecte:
    :param id:
    :return:
    '''
    result_list = [obiect for obiect in obiecte if get_id(obiect) != id]
    return result_list
