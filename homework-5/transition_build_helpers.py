import settings
from battery_maze import BatteryMaze
from KruskalMazeGenerator import KruskalMazeGenerator


env = BatteryMaze(rows=settings.ROWS, cols=settings.COLS)
walls = env.walls


def __get_current_state(row, col):
    return settings.COLS * row + col


def get_opposite_action(action):
    if (action == 0):
        return 2
    elif (action == 1):
        return 3
    elif (action == 2):
        return 0
    else:
        return 1


def check_wall_exists(current_state, next_state):
    return (current_state, next_state) in walls


def set_transition(P, action, current_state, next_state, probability, reward, terminated):
    wall_exists = check_wall_exists(current_state, next_state)
    if (wall_exists):
        opposite_action = get_opposite_action(action)
        P[current_state][action] = [
            (probability, current_state, reward, terminated)]
        return
    else:
        P[current_state][action] = [
            (probability, next_state, reward, terminated)]
        return


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
                    next_state = __get_current_state(
                        row - 1, col) if (row > 0) else current_state
                reward = 1.0 if (
                    next_state == finish_state and current_state != finish_state) else 0.0
                next_state = next_state if (
                    current_state != finish_state) else current_state
                terminated = True if (next_state == finish_state) else False
                probability = 1
                set_transition(P, action, current_state, next_state,
                               probability, reward, terminated)

    return P


P = generate_P()


# print(env.walls)
# for key, value in P.items():
# print(f'{key}: {value}')
