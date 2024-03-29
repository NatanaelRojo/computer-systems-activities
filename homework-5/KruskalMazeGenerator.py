"""
Maze generator based on Krushkal algorithm
"""
from typing import List, Any, Tuple, Set

import random

from MazeGenerator import MazeGenerator


class KruskalMazeGenerator(MazeGenerator):
    def __init__(
        self,
        num_rows: int,
        num_cols: int,
        neighborhood: List[Tuple[int, int]] = [
            (0, -1), (1, 0), (0, 1), (-1, 0)],
    ) -> None:
        super().__init__(num_rows, num_cols, neighborhood)
        self.entrance_index = self.__compute_index(
            *(random.randint(0, self.num_cols - 1), 0))
        self.exit_index = self.__compute_index(
            *(random.randint(0, self.num_cols - 1), self.num_rows - 1))

    def _init_walls(self) -> None:
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                current_index = self.__compute_index(j, i)
                for offset_i, offset_j in self.neighborhood:
                    n_i, n_j = i + offset_i, j + offset_j
                    if not ((0 <= n_i < self.num_rows) and (0 <= n_j < self.num_cols)):
                        continue
                    neighbor_index = self.__compute_index(n_j, n_i)
                    if (current_index, neighbor_index) in self.walls or (
                        neighbor_index,
                        current_index,
                    ) in self.walls:
                        continue
                    self.walls.add((current_index, neighbor_index))

    def generate(self) -> Set[Tuple[int, int]]:
        self._init_walls()
        parent = [i for i in range(self.num_rows * self.num_cols)]
        rank = [0 for i in range(self.num_rows * self.num_cols)]

        walls = list(self.walls)
        random.shuffle(walls)

        for i, j in walls:
            if self.__find(i, parent) != self.__find(j, parent):
                self.__union(i, j, parent, rank)
                self.walls.remove((i, j))

        t1 = True if (self.entrance_index, self.entrance_index +
                      self.num_cols) in self.walls else False
        t2 = True if (self.entrance_index + self.num_cols,
                      self.entrance_index) in self.walls else False

        if t1:
            self.walls.remove(
                (self.entrance_index, self.entrance_index + self.num_cols))
        elif t2:
            self.walls.remove(
                (self.entrance_index + self.num_cols, self.entrance_index))

        t1 = True if (self.exit_index, self.exit_index -
                      self.num_cols) in self.walls else False
        t2 = True if (self.exit_index - self.num_cols,
                      self.exit_index) in self.walls else False

        # self.walls.remove((self.entrance_index, self.entrance_index + self.num_cols)) if ((self.entrance_index, self.entrance_index +
        # self.num_cols) in self.walls) else self.walls.remove(self.entrance_index + self.num_cols, self.entrance_index)
        # self.walls.remove((self.exit_index, self.exit_index - self.num_cols)) if ((self.exit_index, self.exit_index -
        # self.num_cols) in self.walls) else self.walls.remove(self.exit_index - self.num_cols, self.exit_index)

        if t1:
            self.walls.remove(
                (self.exit_index, self.exit_index - self.num_cols))
        elif t2:
            self.walls.remove(
                (self.exit_index - self.num_cols, self.exit_index))

        # self.walls = self.__get_walls()
        return self.walls

    def __get_walls(self):
        walls_list = []
        for wall in self.walls:
            walls_list.append(wall)
            walls_list.append((wall[1], wall[0]))
        return walls_list

    def render(self):
        # render the top wall
        print("-" * int(self.num_cols * 2 + 1))

        for i in range(self.num_rows):
            for j in range(self.num_cols):
                # evaluate if there is a left wall
                current_index = i * self.num_cols + j
                left_index = i * self.num_cols + j - 1
                has_left_wall = (
                    j == 0
                    or (current_index, left_index) in self.walls
                    or (left_index, current_index) in self.walls
                )

                # render the left wall if exists
                if has_left_wall:
                    print("|", end="")
                else:
                    # space if there is no a left wall
                    print(" ", end="")

                # render the cell
                if current_index == self.entrance_index:
                    print('e', end="")
                elif current_index == self.exit_index:
                    print('s', end="")
                else:
                    print(current_index, end="")

            # render the right wall for the current row
            print("|")

            # render the first bottom wall
            print("-", end="")

            # render the bottom wall when if exists
            for j in range(self.num_cols):
                current_index = i * self.num_cols + j
                bottom_index = (i + 1) * self.num_cols + j
                has_bottom_wall = (
                    i == self.num_rows - 1
                    or (current_index, bottom_index) in self.walls
                    or (bottom_index, current_index) in self.walls
                )
                if has_bottom_wall:
                    print("-", end="")
                else:
                    # space if there is not a bottom wall
                    print(" ", end="")

                # render the next bottom wall
                print("-", end="")

            # finally, end of line
            print("")

    def __compute_index(self, x, y):
        return y * self.num_cols + x

    def __find(self, i, parent):
        if parent[i] != i:
            parent[i] = self.__find(parent[i], parent)
        return parent[i]

    def __union(self, i, j, parent, rank):
        root_i = self.__find(i, parent)
        root_j = self.__find(j, parent)
        if root_i != root_j:
            if rank[root_i] < rank[root_j]:
                parent[root_i] = root_j
            elif rank[root_i] > rank[root_j]:
                parent[root_j] = root_i
            else:
                parent[root_j] = root_i
                rank[root_i] += 1


m = KruskalMazeGenerator(5, 5)
m.generate()
m.render()
print(m.walls)
