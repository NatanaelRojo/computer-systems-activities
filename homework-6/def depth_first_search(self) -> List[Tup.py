def depth_first_search(self) -> List[Tuple[int, int]]:
    visited = set()
    stack = [(self.entrance_index, None)]
    while stack:
        current, parent = stack.pop()
        if current == self.exit_index:
            break
        visited.add(current)
        for neighbor in self.neighbors(current):
            if neighbor not in visited:
                stack.append((neighbor, current))
                self.parent[neighbor] = current
    path = []
    current = self.exit_index
    while current is not None:
        path.append(self.coordinates(current))
        current = self.parent[current]
    return path[::-1]
