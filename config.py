from shutil import get_terminal_size


class Colors:
    WHITE = '\033[97m'
    NORMAL = '\033[0m'


DEFAULT_EXERCISE_AMOUNT = 4
DEFAULT_EXERCISE_TIME = 30
DEFAULT_REST_TIME = 10
DEFAULT_REPETITIONS = 4
TERMINAL_HEIGHT = get_terminal_size()[1]