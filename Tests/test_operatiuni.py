from Domain.obiect import *
from Logic.operatiuni import mutare_obiecte, concatenare_string
from Logic.crud import find_obiect

def test_mutare_obiecte():
    o1 = create_obiect('11a', 'carte', 'roz', 8.5, 'abc1')
    o2 = create_obiect('116', 'carte2', 'mov', 10.2, 'abc1')
    obiecte = [o1, o2]
    assert len(obiecte) == 2
    obiecte = mutare_obiecte(obiecte, 'abc2')
    assert len(obiecte) == 2
    o1_new = find_obiect(obiecte, '11a')
    assert get_id(o1_new) == '11a'
    assert get_nume(o1_new) == 'carte'
    assert get_descriere(o1_new) == 'roz'
    assert get_pret_achizitie(o1_new) == 8.5
    assert get_locatie(o1_new) == 'abc2'
    o2_new = find_obiect(obiecte, '116')
    assert get_id(o2_new) == '116'
    assert get_nume(o2_new) == 'carte2'
    assert get_descriere(o2_new) == 'mov'
    assert get_pret_achizitie(o2_new) == 10.2
    assert get_locatie(o2_new) == 'abc2'

def test_concatenare_string():
    o1 = create_obiect('11a', 'carte', 'roz', 8.5, 'abc1')
    o2 = create_obiect('116', 'carte2', 'mov', 10.2, 'abc1')
    obiecte = [o1, o2]
    assert len(obiecte) == 2
    obiecte = concatenare_string(obiecte, 'bcd', 10.0)
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
    assert get_locatie(o2_new) == 'abc1'


