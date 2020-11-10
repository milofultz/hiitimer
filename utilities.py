import os
from time import sleep, time

from config import *


def clear_screen():
    print('\n' * TERMINAL_HEIGHT)


def load_data(filepath):
    with open(filepath, 'r') as f:
        data = f.read()
    return data


def does_file_exist(filepath):
    try:
        data = load_data(filepath)
    except FileNotFoundError:
        return False
    return True


def load_routine_data(filepath):
    try:
        data = load_data(filepath)
    except FileNotFoundError:
        print('Routine Not Found')
        return
    data = data.split('\n')

    routine = {}
    current_field = ''
    for line in data:
        line = line.strip()
        if line == '' or line[0] == '#':
            continue
        elif line[-1] == ':':
            current_field = line[:-1]
            routine[current_field] = []
        elif ':' in line and ':' != line[-1]:
            current_field, value = line.split(':')
            routine[current_field] = int(value.strip())
        else:
            item = line.strip()
            routine[current_field].append(line.strip())

    print('Routine loaded.')
    return routine


def print_loaded_routine(routine):
    print()
    for i, exercise in enumerate(routine['exercises']):
        print(f"Exercise {i+1}: {Colors.WHITE}{exercise}{Colors.NORMAL}")
    print()
    print(f"Exercise Time: {Colors.WHITE}{routine['exercise_time']}{Colors.NORMAL}")
    print(f"Rest Time: {Colors.WHITE}{routine['rest_time']}{Colors.NORMAL}")
    print(f"Reps: {Colors.WHITE}{routine['reps']}{Colors.NORMAL}")
    print()


def get_routine_data():
    exercises = get_exercises()
    exercise_time = get_exercise_time()
    rest_time = get_rest_time()
    reps = get_reps()

    return {'exercises': exercises,
            'exercise_time': exercise_time,
            'rest_time': rest_time,
            'reps': reps}


def get_exercises(number_of_exercises: int = DEFAULT_EXERCISE_AMOUNT):
    exercises = []
    for i in range(number_of_exercises):
        exercise = input(f'Exercise {i+1} of {number_of_exercises}: ')
        exercises.append(exercise)
    return exercises


def get_exercise_time():
    ex_time = input(
        f'Exercise Time in Seconds (Default is {DEFAULT_EXERCISE_TIME}): '
        )
    if ex_time == '':
        return DEFAULT_EXERCISE_TIME
    return int(ex_time)


def get_rest_time():
    rest_time = input(
        f'Rest Time in Seconds (Default is {DEFAULT_REST_TIME}): '
        )
    if rest_time == '':
        return DEFAULT_REST_TIME
    return int(rest_time)


def get_reps():
    reps = input(
        f'Circuit Repetitions (Default is {DEFAULT_REPETITIONS}): '
        )
    if reps == '':
        return DEFAULT_REPETITIONS
    return int(reps)


def get_current_time():
    return round(time())


def start_period(name, length):
    print(f'{Colors.WHITE}{name}{Colors.NORMAL}\n')
    say(name)
    countdown_timer(length)


def start_routine(exercises, exercise_time, rest_time, reps):
    clear_screen()
    start_period(f"Get ready! First is {exercises[0]}", 10)
    for rep in range(reps):
        for i, exercise in enumerate(exercises):
            start_period(exercise, exercise_time)
            clear_screen()
            if rest_time != 0:
                if i == len(exercises) - 1:
                    next_exercise = exercises[0]
                else:
                    next_exercise = exercises[i+1]
                if rep != reps-1 or i != len(exercises)-1:
                    start_period(f'Rest. Next is {next_exercise}', rest_time)
                clear_screen()
    say('Complete')


def say(msg: str):
    os.system(f'say {msg} &')


def countdown_timer(period_time: int):
    sleep(period_time-5)
    for sec in range(5, 0, -1):
        say(sec)
        sleep(1)
