import random

# Definimos una clase para representar cada celda del laberinto


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.walls = {"top": True, "right": True, "bottom": True, "left": True}
        self.visited = False

    def remove_wall(self, direction):
        self.walls[direction] = False

    def get_neighbors(self, grid):
        neighbors = []
        if self.x > 0:
            neighbors.append(grid[self.x - 1][self.y])
        if self.y > 0:
            neighbors.append(grid[self.x][self.y - 1])
        if self.x < len(grid) - 1:
            neighbors.append(grid[self.x + 1][self.y])
        if self.y < len(grid[0]) - 1:
            neighbors.append(grid[self.x][self.y + 1])
        return [neighbor for neighbor in neighbors if not neighbor.visited]

# Función para construir el laberinto


def build_maze(width, height):
    # Creamos una matriz de celdas
    grid = [[Cell(x, y) for y in range(height)] for x in range(width)]

    # Escogemos una celda de entrada y otra de salida aleatorias
    entrance = random.choice(grid[0])
    entrance.remove_wall("left")
    exit = random.choice(grid[-1])
    exit.remove_wall("right")

    # Función para encontrar el conjunto al que pertenece una celda
    def find_set(cell, sets):
        for s in sets:
            if cell in s:
                return s
        return None

    # Creamos un conjunto para cada celda
    sets = [{cell} for row in grid for cell in row]

    # Lista para almacenar las aristas del grafo
    edges = []

    # Agregamos todas las aristas del grafo al azar
    for row in grid:
        for cell in row:
            if cell.x > 0:
                edges.append((cell, grid[cell.x - 1][cell.y]))
            if cell.y > 0:
                edges.append((cell, grid[cell.x][cell.y - 1]))

    # Mezclamos las aristas al azar
    random.shuffle(edges)

    # Recorremos las aristas del grafo en orden aleatorio
    for edge in edges:
        cell1, cell2 = edge

        # Si las dos celdas están en conjuntos diferentes, las unimos quitando una pared
        set1 = find_set(cell1, sets)
        set2 = find_set(cell2, sets)
        if set1 != set2:
            cell1.remove_wall("right" if cell1.x < cell2.x else "left")
            cell2.remove_wall("left" if cell1.x < cell2.x else "right")
            set1.update(set2)
            sets.remove(set2)

        # Si todas las celdas ya han sido visitadas, terminamos
        if len(sets) == 1:
            break

    # Devolvemos el laberinto y las celdas de entrada y salida
    return grid, entrance, exit


grid, entrance, exit = build_maze(6, 6)


def print_maze(grid, entrance, exit):
    # Imprimir la fila superior de la matriz
    top_row = "+"
    for j in range(len(grid[0])):
        top_row += "---+"
    print(top_row)

    # Imprimir cada fila de la matriz
    for i in range(len(grid)):
        row1 = "|"
        row2 = "+"
        for j in range(len(grid[0])):
            # Imprimir la celda de entrada
            if (i, j) == (entrance.x, entrance.y):
                row1 += " E "
            else:
                row1 += "   "

            # Imprimir las paredes derecha e inferior
            if grid[i][j].walls["right"]:
                row1 += "|"
            else:
                row1 += " "
            if grid[i][j].walls["bottom"]:
                row2 += "---+"
            else:
                row2 += "   +"
        print(row1)
        print(row2)

    # Imprimir la celda de salida
    last_row = "+"
    for j in range(len(grid[0])):
        if (len(grid) - 1, j) == (exit.x, exit.y):
            last_row += " S "
        else:
            last_row += "---+"
    print(last_row)


grid, entrance, exit = build_maze(20, 20)

print_maze(grid, entrance, exit)
