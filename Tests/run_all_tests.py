from Tests.test_crud import test_add_obiect, test_edit_obiect, test_delete_obiect
from Tests.test_domain import test_obiect

def run_all_tests():
    test_add_obiect()
    test_edit_obiect()
    test_delete_obiect()
    test_obiect()