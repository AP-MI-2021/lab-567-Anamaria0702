from Domain.obiect import *

def test_obiect():
    obiect = create_obiect('id', 'nume', 'descriere', 4.6, 'locatie')
    assert get_id(obiect) == 'id'
    assert get_nume(obiect) == 'nume'
    assert get_descriere(obiect) == 'descriere'
    assert get_pret_achizitie(obiect) == 4.6
    assert get_locatie(obiect) == 'locatie'

    set_id(obiect, 'id2')
    set_nume(obiect, 'nume2')
    set_descriere(obiect, 'descriere2')
    set_pret_achizitie(obiect, 7.6)
    set_locatie(obiect, 'locatie2')

    assert get_id(obiect) == 'id2'
    assert get_nume(obiect) == 'nume2'
    assert get_descriere(obiect) == 'descriere2'
    assert get_pret_achizitie(obiect) == 7.6
    assert get_locatie(obiect) == 'locatie2'