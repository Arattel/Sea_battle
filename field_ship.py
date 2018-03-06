from string import ascii_lowercase as alphabet
import random


def part_coordinates(bow, length, horizontal = True):
    ship_parts = []
    if horizontal:
        ship_parts = [(bow[0] - i, bow[1]) for i in range(length)]
    else:
        ship_parts = [(bow[0], bow[1]- i) for i in range(length)]
    return ship_parts

def on_field(coord):
    return coord[0] > -1 and coord[0] < 10 and coord[1] > -1 and coord[1] < 10


def find_around(ship_parts):
    around = []
    for i in ship_parts:
        for j in [-1, 0, 1]:
            for k in [-1, 0, 1]:
                if (i[0] + j, i[1] + k) not in around and (i[0] + j, i[1] + k) not in ship_parts and \
                        on_field((i[0] + j, i[1] + k)):
                    around.append((i[0] + j, i[1] + k))
    return around


def to_abs(s):
    return alphabet.index(s[0]), int(s[1:]) - 1



class Ship:
    def __init__(self, length):
        self._length = length
        self.bow = None
        self.horizontal = None
        self._hit = [False] * length

    def killed(self):
        for i in self._hit:
            if not self._hit[i]:
                return False
        return True


class Field:
    def __init__(self, ships):
        self._ships = ships
        self.canvas = [[{'killed':False, 'ship': False, 'around' : False, 'symbol': 's', 'view' : False}
                        for i in range(10)] for j in range(10)]
        for i, ship in enumerate(self._ships):
            parts, around = self.find_possible(ship)
            for i, j in parts:
                self.canvas[9 - j][i] = {'killed':False, 'ship': True, 'around' : False, 'symbol': '#', 'view' : False}
            for i, j in around:
                if self.canvas[9 - j][i] != '#':
                    self.canvas[9 - j][i] = {'killed': False, 'ship': False, 'around': True, 'symbol': 's', 'view' : False}

    def find_possible(self, ship):
        rand_coord = (random.randint(0, 9), random.randint(0, 9))
        pos = random.choice([True, False])
        ship.bow = rand_coord
        ship.horizontal = pos
        possible = True
        parts = part_coordinates(ship.bow, ship._length, horizontal=pos)
        for i, j in parts:
            if not on_field((9 - j, i)) or self.canvas[9 - j][i]['symbol'] != 's' or self.canvas[9 - j][i]['around']:
                possible = False
        while not possible:
            rand_coord = (random.randint(0, 9), random.randint(0, 9))
            ship.bow = rand_coord
            ship.horizontal = pos
            possible = True
            parts = part_coordinates(ship.bow, ship._length)
            for i, j in parts:
                if not on_field((9 - j, i)) or self.canvas[9 - j][i]['symbol'] != 's' or self.canvas[9 - j][i]['around']:
                    possible = False
        around = find_around(parts)
        ship._hit = {i : False for i in parts}

        return parts, around

    def _display(self):
        for i in self.canvas:
            for j in i:
                print(j['symbol'], end=' ')
            print('\n')

    def display(self):
        for i in self.canvas:
            for j in i:
                if j['view']:
                    print(j['symbol'], end=' ')
                else:
                    print("?", end=' ')
            print('\n')
        print('-----'*5)
class Player:
    def __init__(self, name):
        self._name = name
        self._field = Field(ships)
        self.hits = 0


class Game:
    def __init__(self):
        self.player1 = Player(input("Player 1, enter your name: "))
        self.player2 = Player(input("Player 2, enter your name: "))
        self.turn = self.player1
        self.wait = self.player2
    def read_position(self):
        shoot = input('Input coodinates, {} :'.format(self.turn._name))
        coord = to_abs(shoot)
        if not self.wait._field.canvas[9 - coord[1]][coord[0]]['ship']:
            self.wait._field.canvas[9 - coord[1]][coord[0]]['view'] = True
            self.turn, self.wait = self.wait, self.turn
            self.turn._field.display()
        else:
            self.wait._field.canvas[9 - coord[1]][coord[0]]['symbol'] = '*'
            for i in range(len(self.wait._field._ships)):
                if coord in self.wait._field._ships[i]._hit.keys():
                    self.wait._field._ships[i]._hit[coord] = True
                    if self.wait._field._ships[i].killed():
                        for j in self.wait._field._ships[i]._hit.keys():
                            self.wait._field.canvas[9 - j[1]][j[0]]['symbol'] = '#'
            self.wait._field.canvas[9 - coord[1]][coord[0]]['view'] = True
            self.turn.hits += 1
            self.wait._field.display()
        if self.turn.hits >= 20:
            print('Player {} wins'.format(self.turn._name))
        else:
            self.read_position()
ships = [Ship(4), Ship(3), Ship(3), Ship(2), Ship(2), Ship(2), Ship(1), Ship(1), Ship(1), Ship(1)]


if __name__ == "__main__":
    field0 = Field(ships)
    field0.display()
    game = Game()
    game.read_position()





