import random

# Definir las constantes de los símbolos utilizados en el laberinto
WALL = '#'
PATH = ' '
ENTRY = 'E'
EXIT = 'X'


def create_maze(width, height):
    # Inicializar el laberinto con todas las paredes
    maze = [[WALL for x in range(width)] for y in range(height)]

    # Crear una lista de paredes, cada una representada por una tupla (x, y, dirección)
    # donde la dirección es una de las cadenas "N", "S", "E" o "W".
    walls = []
    for x in range(width):
        for y in range(height):
            if x > 0:
                walls.append((x, y, 'W'))
            if y > 0:
                walls.append((x, y, 'N'))

    # Barajar aleatoriamente la lista de paredes
    random.shuffle(walls)

    # Crear un conjunto de conjuntos (disjoint sets) para realizar la unión
    sets = [{(x, y)} for x in range(width) for y in range(height)]

    # Recorrer la lista de paredes, uniendo los conjuntos que separan
    for wall in walls:
        x, y, direction = wall
        if direction == 'W':
            set1 = find_set(x, y, sets)
            set2 = find_set(x-1, y, sets)
        else:
            set1 = find_set(x, y, sets)
            set2 = find_set(x, y-1, sets)
        if set1 != set2:
            maze[y][x] = PATH
            sets.remove(set1)
            sets.remove(set2)
            sets.append(set1.union(set2))

    # Escoger aleatoriamente una entrada y una salida
    entry_x = random.randint(0, width-1)
    exit_x = random.randint(0, width-1)
    entry_y = 0
    exit_y = height-1
    maze[entry_y][entry_x] = ENTRY
    maze[exit_y][exit_x] = EXIT

    # Convertir la matriz de caracteres en una cadena única
    maze_str = ''
    for row in maze:
        maze_str += ''.join(row) + '\n'

    return maze_str


def find_set(x, y, sets):
    # Encontrar el conjunto (set) que contiene la celda (x, y)
    for s in sets:
        if (x, y) in s:
            return s


# Ejemplo de uso:
print(create_maze(10, 10))
