def create_obiect(id, nume, descriere, pret_achizitie, locatie):
    '''

    :param id: string
    :param nume: string
    :param descriere: string
    :param pret_achizitie: float
    :param locatie: string
    :return: Dict
    '''
    return{
        "id": id,
        "nume": nume,
        "descriere": descriere,
        "pret_achizitie": pret_achizitie,
        "locatie": locatie
    }

def get_id(obiect):
    '''

    :param obiect: Dict
    :return: id - string
    '''
    return obiect['id']

def set_id(obiect, id):
    '''
    Setarea id la obiect
    :param obiect: Dict
    :param id: string
    :return:
    '''
    obiect['id'] = id

def get_nume(obiect):
    '''

    :param obiect: Dict
    :return: nume - string
    '''
    return obiect['nume']

def set_nume(obiect, nume):
    '''
    Setarea nume la obiect
    :param obiect: Dict
    :param nume: string
    :return:
    '''
    obiect['nume'] = nume

def get_descriere(obiect):
    '''

    :param obiect: Dict
    :return: descriere - string
    '''
    return obiect['descriere']

def set_descriere(obiect, descriere):
    '''
    Setarea descriere la obiect
    :param obiect: Dict
    :param descriere: string
    :return:
    '''
    obiect['descriere'] = descriere

def get_pret_achizitie(obiect):
    '''

    :param obiect: Dict
    :return: pret_achizitie - float
    '''
    return obiect['pret_achizitie']

def set_pret_achizitie(obiect, pret_achizitie):
    '''
    Setarea pret de achizitie la obiect
    :param obiect: Dict
    :param pret_achizitie: float
    :return:
    '''
    obiect['pret_achizitie'] = pret_achizitie

def get_locatie(obiect):
    '''

    :param obiect: Dict
    :return: locatie - string
    '''
    return obiect['locatie']

def set_locatie(obiect, locatie):
    '''
    Setarea locatie la obiect
    :param obiect: Dict
    :param locatie: string
    :return:
    '''
    obiect['locatie'] = locatie

def to_str(obiect):
    return f'ID={get_id(obiect)}, nume={get_nume(obiect)}, descriere={get_descriere(obiect)}, pret_achizitie={get_pret_achizitie(obiect)}, locatie={get_locatie(obiect)}'