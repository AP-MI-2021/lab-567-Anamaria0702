from Domain.inventar import create_inventar
from UI.consola import run_console
from Tests.run_all_tests import run_all_tests

def main():
    inventar = create_inventar()
    run_console(inventar)

run_all_tests()
main()