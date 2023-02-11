import settings
from battery_maze import BatteryMaze
from KruskalMazeGenerator import KruskalMazeGenerator
from helpers import

env = BatteryMaze(rows=3, cols=3)
walls = env.walls


def __get_current_state(row, col):
    return settings.COLS * row + col


def generate_P():
    finish_state = (settings.ROWS * settings.COLS) - 1
    P = {current_state: {action: [] for action in range(
        settings.NUM_ACTIONS)} for current_state in range(settings.NUM_TILES)}
    for row in range(settings.ROWS):
        for col in range(settings.COLS):
            current_state = __get_current_state(row, col)
            for action in range(settings.NUM_ACTIONS):
                if (action == 0):
                    next_state = __get_current_state(
                        row, col - 1) if (col > 0) else current_state
                elif (action == 1):
                    next_state = __get_current_state(
                        row + 1, col) if (row < settings.ROWS - 1) else current_state
                elif (action == 2):
                    next_state = __get_current_state(
                        row, col + 1) if (col < settings.COLS - 1) else current_state
                else:
                    next_state = (row - 1, col) if (row > 0) else current_state
                reward = 1.0 if (
                    next_state == finish_state and current_state != finish_state) else 0.0
                next_state = next_state if (
                    current_state != finish_state) else current_state
                terminated = True if (next_state == finish_state) else False
                probability = 1.0
                # P[current_state][action].append(
                # (probability, next_current_state, reward, terminated))
                set_transition(P, action, current_state, next_state,
                               probability, reward, terminated)

    return P


# print("                                     ")
# print(generate_P())
P = generate_P()


print(env.walls)
for key, value in P.items():
    print(f'{key}: {value}')
