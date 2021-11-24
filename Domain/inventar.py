from copy import deepcopy

def create_inventar():
    return {
        'listaCurenta': [],
        'listaUndo': [[]],
        'listaRedo': []
    }

def get_lista_curenta(inventar):
    return inventar['listaCurenta']

def get_lista_undo(inventar):
    return inventar['listaUndo']

def get_lista_redo(inventar):
    return inventar['listaRedo']

def set_lista_curenta(inventar, newCurrentList):
    inventar['listaCurenta'] = newCurrentList

def adaugare_lista_undo(inventar):
    listaCurenta = get_lista_curenta(inventar)
    get_lista_undo(inventar).append(deepcopy(listaCurenta))

def adaugare_lista_redo(inventar):
    listaCurenta = get_lista_curenta(inventar)
    get_lista_redo(inventar).append(deepcopy(listaCurenta))

def adaugare_lista_undo_and_clear_redo(inventar):
    adaugare_lista_undo(inventar)
    clear_redo(inventar)

def clear_redo(inventar):
    get_lista_redo(inventar).clear()
