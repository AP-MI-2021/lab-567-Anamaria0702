from Domain.obiect import to_str
from Logic.crud import add_obiect, edit_obiect, delete_obiect

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

def run_crud_ui(obiecte):
    '''

    :param obiecte: lista de obiecte
    :return:
    '''

    def handle_show_all(obiecte):
        '''
        Afisare lista de obiecte din memorie
        :param obiecte: lista de obiecte
        :return:
        '''
        for obiect in obiecte:
            print(to_str(obiect))

    def handle_add_obiect_ui(obiecte):
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
            obiecte = add_obiect(obiecte, id, nume, descriere, pret_achizitie, locatie)
            print('Obiectul a fost adaugat cu succes')
            return obiecte
        except ValueError as ve:
            print("!!! Au aparut erori")
            print(ve)
        except:
            print('Unknown error')

    def handle_edit_obiect_ui(obiecte):
        '''
        Modificarea un obiect dintr-o lista de obiecte in functie de id
        :param obiecte: lista de obiecte
        :return:
        '''
        id = input('Dati idul obiectului pe care vreti sa il editati ')
        nume = input('Dati numele ')
        descriere = input('Dati descrierea ')
        pret_achizitie = input('Dati pretul achizitiei ')
        locatie = input('Dati locatia ')
        try:
            obiecte = edit_obiect(obiecte, id, nume, descriere, pret_achizitie, locatie)
            print('Obiectul a fost modificat cu succes')
            return obiecte
        except ValueError as ve:
            print("!!! Au aparut erori")
            print(ve)
        except:
            print('Unknown error')

    def handle_delete_obiect_ui(obiecte):
        '''
        Stergerea un obiect dintr-o lista de obiecte in functie de id
        :param obiecte: lista de obiecte
        :return:
        '''
        id = input('Dati idul obiectului pe care vreti sa il stergeti ')
        try:
            obiecte = delete_obiect(obiecte, id)
            print('Obiectul a fost sters cu succes')
            return obiecte
        except ValueError as ve:
            print("!!! Au aparut erori")
            print(ve)
        except:
            print('Unknown error')


    while True:
        print_obiect_meniu()
        cmd = input("Comanda: ")
        if cmd == '1':
            obiecte = handle_add_obiect_ui(obiecte)
        elif cmd == '2':
            obiecte = handle_edit_obiect_ui(obiecte)
        elif cmd == '3':
            obiecte = handle_delete_obiect_ui(obiecte)
        elif cmd == '4':
            handle_show_all(obiecte)
        elif cmd == '5':
            break
        else:
            print("Comanda invalida")

def run_operatiuni_ui(obiecte):
    pass

def run_undo_redo(obiecte):
    pass

def run_console(obiecte):
    '''

    :param obiecte: lista de obiecte
    :return:
    '''
    while True:
        print_meniu()
        cmd = input("Comanda: ")
        if cmd == '1':
            run_crud_ui(obiecte)
        elif cmd == '2':
            run_operatiuni_ui(obiecte)
        elif cmd == '3':
            run_undo_redo(obiecte)
        elif cmd == 'x':
            print("La revedere!")
            break
        else:
            print('Comanda invalida')



