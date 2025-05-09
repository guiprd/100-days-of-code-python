class Coordinates:
  def __init__(self, x, y):
    self.x, self.y = x, y

  def __str__(self):
    return "{}, {}".format(self.x, self.y)

  def __neg__(self):
    return Coordinates(-self.x, -self.y)

  def __add__(self, point):
    return Coordinates(self.x + point.x, self.y + point.y)

  def __sub__(self, point):
    return self + -point

# TODO: VALIDAR A IGUALDADE DE COORDENADAS!
  def __eq__(self, point):
    return self.x == point.x and self.y == point.y

class Place(Coordinates):
    def __init__(self, name, coordinates):
        super().__init__(coordinates.x, coordinates.y)
        self.name = name
        self.coordinates = coordinates

    def __str__(self):
        return f"{self.name} ({self.coordinates})"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.name == other.name and self.coordinates == other.coordinates

    def __hash__(self):
        return hash((self.name, self.coordinates))

DIRECTIONS = {
    'U': Coordinates(0, 1),
    'D': Coordinates(0, -1),
    'L': Coordinates(-1, 0),
    'R': Coordinates(1, 0),
    'UR': Coordinates(1, 1),
    'UL': Coordinates(-1, 1),
    'DR': Coordinates(1, -1),
    'DL': Coordinates(-1, -1)
}

PLACES = [
    'Lago',
    'Bosque',
    'Precipício',
    'Cachoeira',
    'Caverna',
    'Montanha',
    'Praia',
    'Campo',
]

def places_generator():
    import random
    path = []
    num_paths = 0
    # Inicializa o caminho com a primeira coordenada
    init_coordinates = Coordinates(0, 0)
    choice_place = random.choice(PLACES)
    init_place = Place(choice_place, init_coordinates)
    path.append(init_place)
    # TODO: VALIDAR O NUMERO DE CAMINHOS!
    while bool(len(PLACES) - num_paths):
        coordinate = Coordinates(random.randint(-1, 1), random.randint(-1, 1))
        if coordinate == Coordinates(0, 0):
            continue
        for p in path:
            if path[-1].coordinates + coordinate == p.coordinates:
                continue
        choice_place = random.choice(PLACES)
        random_place = Place(choice_place, coordinate)
        path.append(random_place)
        num_paths += 1

    return path

def tracking(*track):
    #TODO: Implementar função de tracking
    return