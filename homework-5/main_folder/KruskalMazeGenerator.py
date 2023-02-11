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

    def _init_walls(self) -> None:
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                current_index = i * self.num_cols + j
                for offset_i, offset_j in self.neighborhood:
                    n_i, n_j = i + offset_i, j + offset_j
                    if not ((0 <= n_i < self.num_rows) and (0 <= n_j < self.num_cols)):
                        continue
                    neighbor_index = n_i * self.num_cols + n_j
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

        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                if rank[root_i] < rank[root_j]:
                    parent[root_i] = root_j
                elif rank[root_i] > rank[root_j]:
                    parent[root_j] = root_i
                else:
                    parent[root_j] = root_i
                    rank[root_i] += 1

        walls = list(self.walls)
        random.shuffle(walls)

        for i, j in walls:
            if find(i) != find(j):
                union(i, j)
                self.walls.remove((i, j))

        # print(self.walls)

        self.walls = self.__get_walls()
        return self.walls

    def __get_walls(self):
        walls_list = []
        for wall in self.walls:
            walls_list.append(wall)
            walls_list.append((wall[1], wall[0]))
        return walls_list
