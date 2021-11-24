import sys

from Domain.obiect import to_str
from Logic.crud import add_obiect, edit_obiect, delete_obiect
from Logic.operatiuni import *
from Domain.inventar import get_lista_curenta

def print_meniu():
    print('''
    MENIU
    1. Obiect
    2. Operatiuni
    3. Undo/Redo
    x. Iesire
    ''')

def print_obiect_meniu():
    print('''
    MENIU Obiect
    1. Adaugare
    2. Modificare
    3. Stergere
    4. Afisare toate obiectele
    5. Inapoi
    ''')

def print_operatiuni_meniu():
    print('''
    MENIU Operatiuni
    1. Mutarea tuturor obiectelor dintr-o locație în alta.
    2. Concatenarea unui string citit la toate descrierile obiectelor cu prețul mai mare decât o valoare citită.
    3. Determinarea celui mai mare preț pentru fiecare locație.
    4. Ordonarea obiectelor crescător după prețul de achiziție.
    5. Afișarea sumelor prețurilor pentru fiecare locație.
    6. Inapoi
    ''')

def print_undo_redo_meniu():
    print('''
    MENIU - Undo/Redo
    1. Undo
    2. Redo
    3. Inapoi
    ''')

def run_crud_ui(inventar):
    '''

    :param inventar: lista de obiecte
    :return:
    '''

    def handle_show_all(inventar):
        '''
        Afisare lista de obiecte din memorie
        :param obiecte: lista de obiecte
        :return:
        '''
        obiecte = get_lista_curenta(inventar)
        for obiect in obiecte:
            print(to_str(obiect))

    def handle_add_obiect_ui(inventar):
        '''
        Adaugam un obiect citit de la tastatura in lista de obiecte
        :param obiecte: lista de obiecte
        :return:
        '''
        id = input('Dati idul obiectului ')
        nume = input('Dati numele ')
        descriere = input('Dati descrierea ')
        pret_achizitie = float(input('Dati pretul achizitiei '))
        locatie = input('Dati locatia ')
        try:
            add_obiect(inventar, id, nume, descriere, pret_achizitie, locatie)
            print('Obiectul a fost adaugat cu succes')
        except ValueError as ve:
            print("!!! Au aparut erori")
            print(ve)
        except:
            print('Unknown error')

    def handle_edit_obiect_ui(inventar):
        '''
        Modificarea un obiect dintr-o lista de obiecte in functie de id
        :param obiecte: lista de obiecte
        :return:
        '''
        id = input('Dati idul obiectului pe care vreti sa il editati ')
        nume = input('Dati numele ')
        descriere = input('Dati descrierea ')
        pret_achizitie = float(input('Dati pretul achizitiei '))
        locatie = input('Dati locatia ')
        try:
            edit_obiect(inventar, id, nume, descriere, pret_achizitie, locatie)
            print('Obiectul a fost modificat cu succes')
        except ValueError as ve:
            print("!!! Au aparut erori")
            print(ve)
        except:
            print('Unknown error')

    def handle_delete_obiect_ui(inventar):
        '''
        Stergerea un obiect dintr-o lista de obiecte in functie de id
        :param obiecte: lista de obiecte
        :return:
        '''
        id = input('Dati idul obiectului pe care vreti sa il stergeti ')
        try:
            delete_obiect(inventar, id)
            print('Obiectul a fost sters cu succes')
        except ValueError as ve:
            print("!!! Au aparut erori")
            print(ve)
        except:
            print('Unknown error')

    while True:
        print_obiect_meniu()
        cmd = input("Comanda: ")
        if cmd == '1':
            handle_add_obiect_ui(inventar)
        elif cmd == '2':
            handle_edit_obiect_ui(inventar)
        elif cmd == '3':
            handle_delete_obiect_ui(inventar)
        elif cmd == '4':
            handle_show_all(inventar)
        elif cmd == '5':
            run_console(inventar)
        else:
            print("Comanda invalida")

def run_operatiuni_ui(inventar):
    '''

    :param obiecte:lista de obiecte
    :return:
    '''

    def handle_mutare_obiecte(inventar):
        '''
        mutarea tuturor obiectelor dintr-o locatie in alta
        :param obiecte:lista de obiecte
        :return:
        '''
        locatie_new = input('Dati noua locatie ')
        try:
            mutare_obiecte(inventar, locatie_new)
            print('Obiectele au fost mutate cu succes')
        except ValueError as ve:
            print("!!! Au aparut erori")
            print(ve)
        except:
            print("Unknown error")

    def handle_concatenare_string(inventar):
        '''
        Concateneaza un string citit la toate descrierile obiectelor cu prețul mai mare decât o valoare citită.
        :param obiecte: lista de obiecte
        :return:
        '''
        sir = input('Introduceti sirul ')
        n = float(input('Introduceti valoarea '))
        try:
            concatenare_string(inventar, sir, n)
            print('Sirul a fost concatenat cu succes')
        except ValueError as ve:
            print("!!! Au aparut erori")
            print(ve)
        except:
            print("Unknown error")

    def handle_pret_max_locatie(obiecte):
        '''
        Determina pretul maxim pentru fiecare locatie
        :param obiecte: lista de obiecte
        :return:
        '''
        try:
            lista_locatii = location_list(obiecte)
            pret_max_list = pret_max_locatie(obiecte)
            for pozitie in range(len(lista_locatii)):
                print(f'Cel mai mare pret din locatia {lista_locatii[pozitie]} este {pret_max_list[pozitie]}')
        except ValueError as ve:
            print("!!! Au aparut erori")
            print(ve)
        except:
            print("Unknown error")

    def handle_sort_obiecte(obiecte):
        '''
        Ordoneaza crescator obiectele dupa pretul de achizitie
        :param obiecte: lista de obiecte
        :return:
        '''
        try:
            obiecte = sort_obiecte(obiecte)
            print('Obiectele au fost ordonate cu succes')
            for obiect in obiecte:
                print(to_str(obiect))
            return obiecte
        except ValueError as ve:
            print("!!! Au aparut erori")
            print(ve)
        except:
            print("Unknown error")

    def handle_compute_sum_prices_per_location(obiecte):
        '''
        Afiseaza sumele preturilor pentru fiecare locatie
        :param obiecte: lista de obiecte
        :return:
        '''
        try:
            result = compute_sum_prices_per_location(obiecte)
            for locatie in result:
                print('Locatia {} are suma preturilor: {}'.format(locatie, result[locatie]))
        except ValueError as ve:
            print("!!! Au aparut erori")
            print(ve)
        except:
            print("Unknown error")


    while True:
        print_operatiuni_meniu()
        cmd = input("Comanda: ")
        if cmd == '1':
            handle_mutare_obiecte(inventar)
        elif cmd == '2':
            handle_concatenare_string(inventar)
        elif cmd == '3':
            obiecte = get_lista_curenta(inventar)
            handle_pret_max_locatie(obiecte)
        elif cmd == '4':
            obiecte = get_lista_curenta(inventar)
            handle_sort_obiecte(obiecte)
        elif cmd == '5':
            obiecte = get_lista_curenta(inventar)
            handle_compute_sum_prices_per_location(obiecte)
        elif cmd == '6':
            run_console(inventar)
        else:
            print("Comanda invalida")


def run_undo_redo(inventar):
    def handle_undo(inventar):
        apply_undo(inventar)
        print('Undo facut cu succes')

    def handle_redo(inventar):
        apply_redo(inventar)
        print('Redo facut cu succes')

    while True:
        print_undo_redo_meniu()
        cmd = input("Comanda: ")
        if cmd == '1':
            handle_undo(inventar)
        elif cmd == '2':
            handle_redo(inventar)
        elif cmd == '3':
            run_console(inventar)
        else:
            print("Comanda invalida")

def run_console(inventar):
    '''

    :param inventar: lista de obiecte
    :return:
    '''
    while True:
        print_meniu()
        cmd = input("Comanda: ")
        if cmd == '1':
            run_crud_ui(inventar)
        elif cmd == '2':
            run_operatiuni_ui(inventar)
        elif cmd == '3':
            run_undo_redo(inventar)
        elif cmd == 'x':
            print("La revedere!")
            sys.exit(0)
        else:
            print('Comanda invalida')



