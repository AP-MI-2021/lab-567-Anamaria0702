from Domain.obiect import *
from Logic.operatiuni import *
from Logic.crud import find_obiect, add_obiect, delete_obiect, edit_obiect
from Domain.inventar import create_inventar, get_lista_curenta

def test_mutare_obiecte():
    inventar = create_inventar()
    o1 = create_obiect('11a', 'carte', 'roz', 10.2, 'abc1')
    o2 = create_obiect('116', 'carte2', 'mov', 8.5, 'abc2')
    add_obiect(inventar, '11a', 'carte', 'roz', 10.2, 'abc1')
    add_obiect(inventar, '116', 'carte2', 'mov', 8.5, 'abc2')
    obiecte = get_lista_curenta(inventar)
    assert len(obiecte) == 2
    mutare_obiecte(inventar, 'abc2')
    assert len(obiecte) == 2
    o1_new = find_obiect(obiecte, '11a')
    assert get_id(o1_new) == '11a'
    assert get_nume(o1_new) == 'carte'
    assert get_descriere(o1_new) == 'roz'
    assert get_pret_achizitie(o1_new) == 10.2
    assert get_locatie(o1_new) == 'abc2'
    o2_new = find_obiect(obiecte, '116')
    assert get_id(o2_new) == '116'
    assert get_nume(o2_new) == 'carte2'
    assert get_descriere(o2_new) == 'mov'
    assert get_pret_achizitie(o2_new) == 8.5
    assert get_locatie(o2_new) == 'abc2'

def test_concatenare_string():
    inventar = create_inventar()
    o1 = create_obiect('11a', 'carte', 'roz', 8.5, 'abc1')
    o2 = create_obiect('116', 'carte2', 'mov', 10.2, 'abc2')
    add_obiect(inventar, '11a', 'carte', 'roz', 8.5, 'abc1')
    add_obiect(inventar, '116', 'carte2', 'mov', 10.2, 'abc2')
    obiecte = get_lista_curenta(inventar)
    assert len(obiecte) == 2
    concatenare_string(inventar, 'bcd', 10.0)
    assert len(obiecte) == 2
    o1_new = find_obiect(obiecte, '11a')
    assert get_id(o1_new) == '11a'
    assert get_nume(o1_new) == 'carte'
    assert get_descriere(o1_new) == 'roz'
    assert get_pret_achizitie(o1_new) == 8.5
    assert get_locatie(o1_new) == 'abc1'
    o2_new = find_obiect(obiecte, '116')
    assert get_id(o2_new) == '116'
    assert get_nume(o2_new) == 'carte2'
    assert get_descriere(o2_new) == 'movbcd'
    assert get_pret_achizitie(o2_new) == 10.2
    assert get_locatie(o2_new) == 'abc2'

def test_pret_max_per_locatie():
    inventar = create_inventar()
    add_obiect(inventar, '11a', 'carte', 'roz', 8.5, 'abc1')
    add_obiect(inventar, '116', 'carte2', 'mov', 11.5, 'abc2')
    add_obiect(inventar, '11b', 'carte3', 'verde', 20.1, 'abc2')
    add_obiect(inventar, '117', 'carte4', 'maro', 10.2, 'abc1')
    obiecte = get_lista_curenta(inventar)
    locationlist = location_list(obiecte)

    assert get_locatie(obiecte[0]) in locationlist
    assert get_locatie(obiecte[1]) in locationlist
    assert len(locationlist) == 2

    lista_preturi = pret_max_locatie(obiecte)

    assert get_pret_achizitie(obiecte[3]) in lista_preturi
    assert get_pret_achizitie(obiecte[2]) in lista_preturi
    assert len(lista_preturi) == len(locationlist)

def test_ordonare_obiecte():
    o1 = create_obiect('116', 'carte2', 'mov', 11.5, 'abc2')
    o2 = create_obiect('11b', 'carte3', 'verde', 20.1, 'abc2')
    o3 = create_obiect('117', 'carte4', 'maro', 10.2, 'abc1')

    sorted_list = sort_obiecte([o1,o2,o3])
    assert sorted_list[0] == o3
    assert sorted_list[1] == o1
    assert sorted_list[2] == o2

def test_suma_preturi_per_locatie():
    inventar = create_inventar()
    add_obiect(inventar, '11a', 'carte', 'roz', 8.5, 'abc1')
    add_obiect(inventar, '116', 'carte2', 'mov', 11.5, 'abc2')
    add_obiect(inventar, '11b', 'carte3', 'verde', 20.1, 'abc2')
    add_obiect(inventar, '117', 'carte4', 'maro', 10.2, 'abc1')
    obiecte = get_lista_curenta(inventar)
    suma_preturi_per_locatie = compute_sum_prices_per_location(obiecte)
    assert round(suma_preturi_per_locatie['abc1'], 1) == 18.7
    assert round(suma_preturi_per_locatie['abc2'], 1) == 31.6

def test_undo():
    inventar = create_inventar()
    add_obiect(inventar, '11a', 'carte', 'roz', 8.5, 'abc1')
    add_obiect(inventar, '116', 'carte2', 'mov', 11.5, 'abc2')
    assert len(get_lista_curenta(inventar)) == 2
    apply_undo(inventar)
    assert len(get_lista_curenta(inventar)) == 1
    apply_undo(inventar)
    assert len(get_lista_curenta(inventar)) == 0
    apply_undo(inventar)
    assert len(get_lista_curenta(inventar)) == 0

    add_obiect(inventar, '11a', 'carte', 'roz', 8.5, 'abc1')
    add_obiect(inventar, '116', 'carte2', 'mov', 11.5, 'abc2')
    delete_obiect(inventar, '11a')
    assert len(get_lista_curenta(inventar)) == 1
    apply_undo(inventar)
    assert len(get_lista_curenta(inventar)) == 2

    edit_obiect(inventar, '116', 'carte2new', 'mov new', 19.3, 'abc2')
    assert len(get_lista_curenta(inventar)) == 2
    assert find_obiect(get_lista_curenta(inventar), '116') == create_obiect('116', 'carte2new', 'mov new', 19.3, 'abc2')
    apply_undo(inventar)
    assert len(get_lista_curenta(inventar)) == 2
    assert find_obiect(get_lista_curenta(inventar), '116') == create_obiect('116', 'carte2', 'mov', 11.5, 'abc2')

def test_undo_redo():
    inventar = create_inventar()

    add_obiect(inventar, '11a', 'carte', 'roz', 8.5, 'abc1')
    add_obiect(inventar, '116', 'carte2', 'mov', 11.5, 'abc2')
    add_obiect(inventar, '11b', 'carte3', 'verde', 20.1, 'abc3')
    assert len(get_lista_curenta(inventar)) == 3

    apply_undo(inventar)
    assert len(get_lista_curenta(inventar)) == 2

    apply_undo(inventar)
    assert len(get_lista_curenta(inventar)) == 1

    apply_undo(inventar)
    assert len(get_lista_curenta(inventar)) == 0

    apply_undo(inventar)
    assert len(get_lista_curenta(inventar)) == 0

    add_obiect(inventar, '11c', 'carte4', 'roz', 8.5, 'abc1')
    add_obiect(inventar, '117', 'carte5', 'mov', 11.5, 'abc2')
    add_obiect(inventar, '11d', 'carte6', 'verde', 20.1, 'abc3')
    assert len(get_lista_curenta(inventar)) == 3

    apply_redo(inventar)
    assert len(get_lista_curenta(inventar)) == 3

    apply_undo(inventar)
    assert len(get_lista_curenta(inventar)) == 2

    apply_undo(inventar)
    assert len(get_lista_curenta(inventar)) == 1

    apply_redo(inventar)
    assert len(get_lista_curenta(inventar)) == 2

    apply_redo(inventar)
    assert len(get_lista_curenta(inventar)) == 3

    apply_undo(inventar)
    assert len(get_lista_curenta(inventar)) == 2
    apply_undo(inventar)
    assert len(get_lista_curenta(inventar)) == 1

    add_obiect(inventar, '11e', 'carte6', 'verde', 20.1, 'abc3')
    assert len(get_lista_curenta(inventar)) == 2
    apply_redo(inventar)
    assert len(get_lista_curenta(inventar)) == 2

    apply_undo(inventar)
    assert len(get_lista_curenta(inventar)) == 1

    apply_undo(inventar)
    assert len(get_lista_curenta(inventar)) == 0
    apply_redo(inventar)
    assert len(get_lista_curenta(inventar)) == 1
    apply_redo(inventar)
    assert len(get_lista_curenta(inventar)) == 2
    apply_redo(inventar)
    assert len(get_lista_curenta(inventar)) == 2

    delete_obiect(inventar, '11e')
    assert len(get_lista_curenta(inventar)) == 1
    apply_undo(inventar)
    assert len(get_lista_curenta(inventar)) == 2
    apply_redo(inventar)
    assert len(get_lista_curenta(inventar)) == 1
    apply_redo(inventar)
    assert len(get_lista_curenta(inventar)) == 1
    apply_undo(inventar)
    assert len(get_lista_curenta(inventar)) == 2

    edit_obiect(inventar, '11c', 'nume','descriere', 15, '1234')
    assert len(get_lista_curenta(inventar)) == 2
    assert find_obiect(get_lista_curenta(inventar), '11c') == create_obiect('11c', 'nume','descriere', 15, '1234')
    apply_undo(inventar)
    assert len(get_lista_curenta(inventar)) == 2
    assert find_obiect(get_lista_curenta(inventar), '11c') == create_obiect('11c', 'carte4', 'roz', 8.5, 'abc1')
    apply_redo(inventar)
    assert len(get_lista_curenta(inventar)) == 2
    assert find_obiect(get_lista_curenta(inventar), '11c') == create_obiect('11c', 'nume', 'descriere', 15, '1234')


















