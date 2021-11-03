from Logic.crud import add_obiect, find_obiect, edit_obiect, delete_obiect
from Domain.obiect import create_obiect, get_id, get_nume, get_descriere, get_pret_achizitie, get_locatie

def test_add_obiect():
    obiecte = []
    obiect_adaugat = create_obiect('11a', 'carte', 'roz', 10.2, 'abc1')
    obiecte = add_obiect(obiecte, '11a', 'carte', 'roz', 10.2, 'abc1')
    assert len(obiecte) == 1
    assert obiecte[0] == obiect_adaugat
    assert get_id(obiecte[0]) == '11a'
    assert get_nume(obiecte[0]) == 'carte'
    assert get_descriere(obiecte[0]) == 'roz'
    assert get_pret_achizitie(obiecte[0]) == 10.2
    assert get_locatie(obiecte[0]) == 'abc1'

    obiecte = add_obiect(obiecte, '11b', 'masa' , 'maro', 50.4, 'abc7')
    obiect_adaugat_2 = create_obiect('11b', 'masa' , 'maro', 50.4, 'abc7')
    assert len(obiecte) == 2
    assert obiecte[0] == obiect_adaugat
    assert obiecte[1] == obiect_adaugat_2

def test_edit_obiect():
    o1 = create_obiect('11a', 'carte', 'roz', 10.2, 'abc1')
    o2 = create_obiect('116', 'carte2', 'mov', 10.2, 'abc1')
    obiecte = [o1, o2]
    assert len(obiecte) == 2
    obiecte = edit_obiect(obiecte, '11a', 'carte new', 'verde' , 8.5, 'abc2')
    assert len(obiecte) == 2
    o1_new = find_obiect(obiecte, '11a')
    assert get_id(o1_new) == '11a'
    assert get_nume(o1_new) == 'carte new'
    assert get_descriere(o1_new) == 'verde'
    assert get_pret_achizitie(o1_new) == 8.5
    assert get_locatie(o1_new) == 'abc2'

    try:
        obiecte = edit_obiect(obiecte, '11a', '', 'verde', -34, 'abc2')
        assert False
    except ValueError:
        assert True

def test_delete_obiect():
    o1 = create_obiect('11a', 'carte', 'roz', 10.2, 'abc1')
    o2 = create_obiect('116', 'carte2', 'mov', 10.2, 'abc1')
    obiecte = [o1, o2]
    assert len(obiecte) == 2
    obiecte = delete_obiect(obiecte, '11a')
    assert len(obiecte) == 1
    obiecte = delete_obiect(obiecte, '11ajv')
    assert len(obiecte) == 1



