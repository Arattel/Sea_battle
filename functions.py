from string import ascii_lowercase as alphabet


def read_field(path):
    """
    (str) -> (list)
    Reads a field from file and outputs a list
    """
    field = []
    with open(path, 'r') as file:
        for i in file.readlines():
            field.append(list(i.strip()))
    return field


def has_ship(field, coord):
    """
    (list, tuple) -> (bool)
    Defines if there is a ship in given cell
    """
    if field[9 - coord[1]][alphabet.index(coord[0])] == ' ':
        return False
    return True

def is_ship(s):
    """
    (str) -> (bool)
    Returns True is str can represent a ship
    """
    for i in s:
        if i not in ['*', "X"]:
            return False
    return True


def is_valid(field):
    """
    (list) -> (bool)
    Defines if field is valid
    """
    ship_cells = 0
    for i in field:
        for j in i:
            if j in ['*', 'X']:
                ship_cells += 1
    has_number_cells = (ship_cells == 20)
    one_cell = 0
    for i in range(len(field)):
        for j in range(len(i)):
            if field[i][j] in ['*', 'X']:
                if field[i-1][j] not in  ['*', 'X'] and field[i][j - 1] not in  ['*', 'X'] and field[i][j + 1] not in  \
                        ['*', 'X'] and field[i + 1][j] not in  ['*', 'X']:
                    one_cell += 1
    has_number_one_cells = one_cell == 4
    four = 0
    for i in field:
        for j in range(6):
            if is_ship(''.join(i[j: j + 4])):
                four += 1
    for i in range(len(field)):
        pass


def field_to_str(field):
    """
    (list) -> (str)
    Makes str from list
    """
    represent = ""
    for i in field:
        represent += ''.join(i) + '\n'
    return represent






