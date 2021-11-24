from Tests.test_crud import test_add_obiect, test_edit_obiect, test_delete_obiect
from Tests.test_domain import test_obiect
from Tests.test_operatiuni import *

def run_all_tests():
    test_add_obiect()
    test_edit_obiect()
    test_delete_obiect()
    test_obiect()
    test_mutare_obiecte()
    test_concatenare_string()
    test_pret_max_per_locatie()
    test_ordonare_obiecte()
    test_suma_preturi_per_locatie()
    test_undo()
    test_undo_redo()
